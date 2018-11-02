#!/usr/bin/python

#sudo apt-get install libzbar0
#pip3 install pyzbar
#pip3 install pdf2imgage
#
from sys import argv
import os
import sys
import pyzbar.pyzbar as pyzbar
from PyPDF2 import PdfFileReader, PdfFileWriter

from pdf2image import convert_from_bytes

#this file looks in the src folder for image files and looks for
#convert to images
pdfPages = PdfFileReader('src/test.pdf')
pages = convert_from_bytes(open('test.pdf', 'rb').read())
writer = PdfFileWriter()

i = 0
output = []
for page in pages:
     val = pyzbar.decode(page)
     if val != []:
          #found a qr code
          data = val[0][0]
          if i != 0:
               #print out whats been collected so far
               output.append(data)
               with open('output' + str(i) + '.pdf','wb') as outfile:
                    writer.write(outfile)
          #grab first page
          writer = PdfFileWriter()
          writer.addPage(pdfPages.getPage(i))
     else:
          writer.addPage(pdfPages.getPage(i))
     i += 1

#save whatever's left
with open('output' + str(i) + '.pdf','wb') as outfile:
     writer.write(outfile)
output.append(data)

for name in output:
     print(name)

sys.exit