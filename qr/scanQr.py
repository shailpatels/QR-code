#!/usr/bin/python

#sudo apt-get install libzbar0
#sudo apt-get install python-poppler    (might need this?)
#pip3 install pyzbar
#pip3 install pdf2imgage
#
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
output = []
for page in pages:
     val = pyzbar.decode(page)
     if val != []:
          data = val[0][0]
          if i != 0:
               output.append(data)
               with open('output' + str(i) + '.pdf','wb') as outfile:
                    writer.write(outfile)
          writer = PdfFileWriter()
          writer.addPage(pdfPages.getPage(i))
     else:
          writer.addPage(pdfPages.getPage(i))
     i += 1

with open('output' + str(i) + '.pdf','wb') as outfile:
     writer.write(outfile)
output.append(data)

for name in output:
     print(name)

sys.exit