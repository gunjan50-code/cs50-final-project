from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_redacted_pdf(text, filename="cleaned_output.pdf"):
    """
    Generates a PDF where '[REDACTED]' is highlighted/blurry-like to show masked info.
    """

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    text_object = c.beginText(0.75 * inch, height - 1 * inch)
    text_object.setFont("Helvetica", 11)

    # Split text into lines for writing on PDF
    lines = text.split("\n")
    for line in lines:
        # Replace [REDACTED] with a masked look
        if "[REDACTED]" in line:
            masked_line = line.replace("[REDACTED]", "███████")
            text_object.textLine(masked_line)
        else:
            text_object.textLine(line)

    c.drawText(text_object)
    c.save()

    return filename
