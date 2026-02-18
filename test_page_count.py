"""
Simple test script to check how many pages are generated
Run this to debug the PDF generation issue
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from pypdf import PdfReader
import io

# Create a test PDF
buffer = io.BytesIO()
doc = SimpleDocTemplate(buffer, pagesize=letter)
elements = []
styles = getSampleStyleSheet()

# Page 1 - Cover
elements.append(Paragraph("PAGE 1: COVER", styles['Title']))
elements.append(PageBreak())

# Pages 2-9 (will become pages 5-12 in final)
for i in range(2, 10):
    elements.append(Paragraph(f"PAGE {i}: Content for page {i+3} in final", styles['Title']))
    elements.append(Spacer(1, 2*inch))
    elements.append(PageBreak())

# Page 10 (will become page 13 in final)
elements.append(Paragraph("PAGE 10: Transfer Pricing (final page 13)", styles['Title']))
elements.append(PageBreak())

# Page 11 (will become page 21 in final)
elements.append(Paragraph("PAGE 11: Contact Page (final page 21)", styles['Title']))

# Build
doc.build(elements)

# Check pages
buffer.seek(0)
pdf = PdfReader(buffer)
print(f"Total pages generated: {len(pdf.pages)}")
print("\nPage breakdown:")
for i, page in enumerate(pdf.pages):
    print(f"  Index {i}: {page}")

print("\n✅ Test complete!")
print(f"Expected: 11 pages (indices 0-10)")
print(f"Got: {len(pdf.pages)} pages")