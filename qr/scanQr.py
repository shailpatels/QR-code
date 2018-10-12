#!/usr/bin/python


#linux install:
#sudo apt-get install libzbar-dev
#pip install zbar
#pip install pypdf2


from sys import argv
import zbar
import os
import sys
from PIL import Image


#this file looks in the src folder for image files and looks for
#a QR code to decode
scanner = zbar.ImageScanner()
scanner.parse_config('enable')

for file in os.listdir('src'):
     pil_img = Image.open('src/' + file).convert('L')

     width, height=pil_img.size
     raw = pil_img.tobytes()

     image=zbar.Image(width, height, 'Y800', raw)

     #scan the image for barcodes
     scanner.scan(image)
     #get decoded strings
     decoded_strings = []
     i = 0
     for result in image:
          decoded_strings.append(result.data)

     if len(decoded_strings) == 0:
          print('could not find QR code in ' + file)
     else:    
          print('found ' + str(len(decoded_strings)) + ' qr code(s) in ' + file)
          for string in decoded_strings:
               print(string)

     print("")
     del(image)

sys.exit