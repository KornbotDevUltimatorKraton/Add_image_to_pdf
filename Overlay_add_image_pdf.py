from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, Image


def create_pdf():
    pdf_file = 'Report-Mockup-EN-Blank.pdf-page14.pdf'

    #can = canvas.Canvas(pdf_file)

    #can.drawString(20, 800, "First Page")
    # can.showPage()
    # can.save()


def add_image():

    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io

    in_pdf_file = 'Report-Mockup-EN-Blank.pdf-page14.pdf'
    out_pdf_file = 'Report_output_lab.pdf'
    img_file = 'table.jpg'
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    #can.drawString(10, 100, "Hello world")
    x_start = -80
    y_start = 520
    can.drawImage(img_file,x_start, y_start, width=700, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)

    new_pdf = PdfFileReader(packet)

    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()


create_pdf()
add_image()
