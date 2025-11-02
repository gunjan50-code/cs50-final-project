## Privy – Privacy Checker

A Streamlit-based app that detects and hides personal information (like emails, phone numbers, and names) from PDF, DOCX, or pasted text files.
🔗 Live App: [Click here to try Privy](https://cs50-final-project-oqkjakmnxjja.streamlit.app/)

📸 Screenshots: (Added below in the Images section)

## 🌸 About the Project

Privy – Privacy Checker is my final project for CS50. It’s designed to help users protect sensitive information before sharing documents or text online. The app automatically scans uploaded files (PDF/DOCX) or pasted text, finds personal details such as names, phone numbers, and email addresses, and then generates a clean version with those details removed (or replaced with [REDACTED]).

This idea came from a real-world problem: sometimes we need to share documents publicly but forget that our personal info might still be visible. I wanted to build a tool that makes it simple and safe for anyone to quickly clean up their files.

## 🧠 Features

Upload PDF or Word (DOCX) files.

Or simply paste text directly into the app.

Detects and highlights:

📧 Email addresses

📞 Phone numbers

👤 Names (basic pattern detection)

Automatically replaces detected data with [REDACTED].
Generates a clean text file and a redacted PDF for download.
Shows a visual bar chart summary of detected information.

## ⚙️ How It Works

The user uploads a document or pastes text.
The app extracts text using:
pdfplumber for PDFs
python-docx for Word files

It sends the text to a detection function that uses pattern matching and AI logic to find sensitive info.
Detected items are listed for the user.
Redacted versions (with [REDACTED]) are created using:
fpdf and reportlab libraries.
The final results are displayed in a neat Streamlit interface, including graphs built with matplotlib.

## 🧩 Tech Stack & Libraries
| Category                | Tools Used              |
| ----------------------- | ----------------------- |
| **Frontend/UI**         | Streamlit               |
| **Backend**             | Python                  |
| **PDF/Text Processing** | pdfplumber, python-docx |
| **PDF Generation**      | reportlab, fpdf         |
| **Visualization**       | matplotlib              |
| **AI/Text Detection**   | transformers, torch     |
| **Helper Functions**    | fitz (PyMuPDF)          |

## 🗂️ Project Structure

```
📁 cs50-final-project
│
├── main.py              # Streamlit main file
├── detector.py          # Contains sensitive info detection logic
├── file_handler.py      # Handles text extraction from PDFs/DOCX
├── pdf_generator.py     # Creates redacted PDF output
├── requirements.txt     # Libraries required for deployment
├── README.md            # Project documentation (this file)
└── 📁 screenshots        # Folder for project screenshots
```

### 📸 Screenshots  

Here’s how the app looks in action:

[Home Page](screenshots/Screenshot1.png)
[Detection Example](screenshots/screenshot2.png)
[Redacted PDF Download](screenshots/Screenshot3.png)
