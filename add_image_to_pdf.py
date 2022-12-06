from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("prototype2.jpg", ...)
with pdf.local_context(blend_mode="ColorBurn"):
    pdf.image("Prototype2.jpg", ...)
pdf.output("blended-images.pdf")


