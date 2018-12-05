# QR-code
Given a PDF, split into smaller PDFs by a QR code. <br>
Written in python using the Zbar library

Things needed:
     
     sudo apt-get install libzbar0

     pip3 install pyzbar
     pip3 install Py2PDF
     pip3 install pdf2image
Zbar and pyzbar must both be installed since pyzbar is a python wrapper that requires the DLLs from zbar

(Optional for generating QR codes)
		
	pip3 install qrcode	
	pip3 install Pillow  	 

## Usage
In a terminal:
	
	python3 scanQr.py

The script will then take the PDF named `test.pdf` and dump the split PDFs into the `output` folder

## Generating QR codes

For making PDF's with QR codes, a qr code can be generated from a string using the `generateQr.py` script<br>
Run by:

	python3 generateQr.py

Then enter a string after the promp and a qr code image will be made in the `output` folder	

