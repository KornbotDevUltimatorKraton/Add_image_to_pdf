from fpdf import FPDF, HTML2FPDF

class CustomHTML2FPDF(HTML2FPDF):
    def render_toc(self, pdf, outline):
        pdf.cell(txt='Table of contents:', new_x="LMARGIN", new_y="NEXT")
        for section in outline:
            pdf.cell(txt=f'* {section.name} (page {section.page_number})', new_x="LMARGIN", new_y="NEXT")

class PDF(FPDF):
    HTML2FPDF_CLASS = CustomHTML2FPDF

pdf = PDF()
pdf.add_page()
pdf.write_html("""<toc></toc>
    <h1>Level 1</h1>
    <h2>Level 2</h2>
    <h3>Level 3</h3>
    <h4>Level 4</h4>
    <h5>Level 5</h5>
    <h6>Level 6</h6>
    <p>paragraph<p>""")
pdf.output("html_toc.pdf")
