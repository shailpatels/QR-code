#!/usr/bin/python

#this file looks in the src folder for image files and looks for
#a QR code to decode
#!/usr/bin/python

#linux install:
#sudo apt-get install libzbar-dev
#pip install zbar
#pip install pypdf2
#pip install pyzbar (for python3)

#sudo pip3 install zbar-py

from sys import argv
import os
import sys
import pyzbar.pyzbar as pyzbar
from PyPDF2 import PdfFileReader, PdfFileWriter

#this file looks in the src folder for image files and looks for

from pdf2image import convert_from_bytes

#convert to images
pdfPages = PdfFileReader('src/test.pdf')
pages = convert_from_bytes(open('test.pdf', 'rb').read())
writer = PdfFileWriter()

i = 0
for page in pages:
     val = pyzbar.decode(page)
     if val != []:
          if i != 0:
               with open('output' + str(i) + '.pdf','wb') as outfile:
                    writer.write(outfile)
          writer = PdfFileWriter()
          writer.addPage(pdfPages.getPage(i))
     else:
          writer.addPage(pdfPages.getPage(i))
     i += 1

with open('output' + str(i) + '.pdf','wb') as outfile:
     writer.write(outfile)

sys.exit