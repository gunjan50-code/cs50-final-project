from pdf_generator import create_redacted_pdf
import streamlit as st
from file_handler import extract_text_from_pdf, extract_text_from_docx
import io
import matplotlib.pyplot as plt
import time

# --- Page setup ---
st.set_page_config(page_title="Privy – Privacy Checker", layout="wide")

st.title("Privy – Privacy Checker")
st.write("Upload a PDF/DOCX file or paste text to detect personal information.")

# --- Load Model with Spinner ---
with st.spinner("Initializing AI model... please wait"):
    from detector import detect_sensitive_info
    time.sleep(1.5)  # optional delay for smoother UI feedback
st.success("Model loaded")

# --- Option to upload OR paste text ---
input_choice = st.radio("Choose input method:", ("Upload File", "Paste Text"))

text = ""

if input_choice == "Upload File":
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        if file_type == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)
else:
    st.markdown("### Enter text to analyze")
    text = st.text_area("Paste your text below:", height=150, placeholder="Type or paste text here...")
    analyze_clicked = st.button("Analyze Text")

# --- Continue only if text is available and button is pressed ---
if (input_choice == "Upload File" and text.strip()) or (input_choice == "Paste Text" and analyze_clicked and text.strip()):
    st.subheader("Extracted Text Preview")
    st.text_area("Text Preview", text[:3000], height=200)

    # Detect sensitive information with spinner
    with st.spinner("Scanning text for sensitive information... 🔍"):
        sensitive = detect_sensitive_info(text)

    st.subheader("Detected Information")
    for key, values in sensitive.items():
        if values:
            st.markdown(f"**{key.capitalize()}**: {', '.join(values)}")
        else:
            st.markdown(f"**{key.capitalize()}**: None found")

    # Redact only emails and phones
    clean_text = text
    for value in sensitive["emails"] + sensitive["phones"]:
        clean_text = clean_text.replace(value, "[REDACTED]")

    # --- Download Clean Text Option ---
    clean_bytes = io.BytesIO(clean_text.encode())
    st.download_button(
        label="Download Clean Text",
        data=clean_bytes,
        file_name="clean_text.txt",
        key="text_download"
    )

    # --- Generate Redacted PDF ---
    pdf_filename = create_redacted_pdf(clean_text)
    with open(pdf_filename, "rb") as pdf_file:
        st.download_button(
            label="Download Redacted PDF",
            data=pdf_file,
            file_name="redacted_output.pdf",
            mime="application/pdf",
            key="pdf_download"
        )

    # --- Compact Bar Chart ---
    counts = {
        "Emails": len(sensitive["emails"]),
        "Phones": len(sensitive["phones"]),
        "Others": len(sensitive["names"])
    }

    st.subheader("Information Detected Summary")
    fig, ax = plt.subplots(figsize=(1, 0.7))  # very small graph
    ax.bar(counts.keys(), counts.values(), color="#014421", width=0.25)
    ax.tick_params(axis='both', labelsize=4)
    plt.tight_layout(pad=0.1)
    st.pyplot(fig, clear_figure=True)
