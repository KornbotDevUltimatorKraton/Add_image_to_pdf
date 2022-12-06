import cv2
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
im = cv2.imread('table.jpg')
def gen_pdf():
    # there are 66 slides (1.jpg, 2.jpg, 3.jpg...)
    path = 'table.jpg'
    pdf = PdfFileWriter()

    for num in range(0,1):  # for each slide
        # Using ReportLab Canvas to insert image into PDF
        imgTemp = BytesIO()
        imgDoc = canvas.Canvas(imgTemp, pagesize=A4)
        # Draw image on Canvas and save PDF in buffer
        imgDoc.drawImage(path.format(num), -25, -45)
        # x, y - start position
        # in my case -25, -45 needed
        imgDoc.save()
        # Use PyPDF to merge the image-PDF into the template
        pdf.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))

    pdf.write(open("output_2.pdf","wb"))

#im = cv2.imread('table.jpg')
print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))

if __name__ == '__main__':
    gen_pdf()
