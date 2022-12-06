from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from StringIO import StringIO


# Using ReportLab to insert image into PDF
imgTemp = StringIO()
imgDoc = canvas.Canvas(imgTemp)

# Draw image on Canvas and save PDF in buffer
imgPath = "table.jpg"
imgDoc.drawImage(imgPath, 399, 760, 160, 160)    ## at (399,760) with size 160x160
imgDoc.save()

# Use PyPDF to merge the image-PDF into the template
page = PdfFileReader(file("Report-Mockup-EN-Blank.pdf-page14.pdf","rb")).getPage(0)
overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)
page.mergePage(overlay)

#Save the result
output = PdfFileWriter()
output.addPage(page)
output.write(file("output.pdf","w"))
