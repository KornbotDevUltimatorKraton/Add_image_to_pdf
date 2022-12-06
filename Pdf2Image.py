from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (PDFInfoNotInstalledError,PDFPageCountError,PDFSyntaxError)
#images = convert_from_bytes(open('/home/kornbotdev/Create_table_pdf_fpdf2/Report-Mockup-EN-Blank.pdf-page14.pdf', 'rb').read())
#print(images)
#images.save("Report-Mockup-EN-Blank.pdf-page14.jpg")
images = convert_from_path('/home/kornbotdev/Create_table_pdf_fpdf2/Report-Mockup-EN-Blank.pdf-page14.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

df.index = [item.strftime('%Y-%m-%d') for item in df.index] # Format date

fig, ax = plt.subplots(figsize=(12, 2)) # set size frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
tabla = table(ax, df, loc='upper right', colWidths=[0.17]*len(df.columns))  # where df is your data frame
tabla.auto_set_font_size(False) # Activate set fontsize manually
tabla.set_fontsize(12) # if ++fontsize is necessary ++colWidths
tabla.scale(1.2, 1.2) # change size table
plt.savefig('table.jpg', transparent=True)
