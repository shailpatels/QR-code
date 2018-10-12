#!/usr/bin/python

#pip install qrcode
from sys import argv
import qrcode
import os
import sys
from PIL import Image

data = raw_input("enter a string to encode\n")
qr = qrcode.QRCode(
    version = 1,
    #error_correction = qrcode.constants.ERROR_CORRECT_H, _L, _M, _Q, _H
    box_size = 10,
    border = 4,
)
qr.add_data(data)
img = qr.make_image()
img.save('output/' + data + 'qr.png') #can also be .bmp, .jpeg
sys.exit