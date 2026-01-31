from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(summary, filename="contract_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(50, 750, "Contract Risk Analysis Report")

    y = 700
    for line in summary:
        c.drawString(50, y, line)
        y -= 20

    c.save()
