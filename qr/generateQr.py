#!/usr/bin/python

#pip install qrcode
from sys import argv
import qrcode
import os
import sys
from PIL import Image

data = input("enter a string to encode\n")
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 4,
)
qr.add_data(data)
img = qr.make_image()
img.save('output/' + data + '.png') #can also be .bmp, .jpeg
sys.exit