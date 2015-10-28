#! /usr/bin/env python
"""
bmp2byte.py - Convert a *.bmp image into a byte array
"""

from __future__ import print_function
import sys
from PIL import Image
import numpy as np

def main():
	im = Image.open("test_image.bmp")
	#p = np.array(im)
	#print(p)
	print("File Format: " + im.format)
	print("Image Size [W,H]: " + str(im.size))
	print("Image Palette: " + str(im.palette))
	
	# 1 = (1-bit pixels, black and white, stored with one pixel per byte)
	# L = (8-bit pixels, black and white)
	print("Image Mode: " +im.mode)
	
	# Need to convert array from mode = 1 to obtain usable data.
	print(np.array(im.convert("L"))) # Looks good at this point, 
	
	# Next step. Read each value in the array. If 255 then convert to 0, If zero convert to 1.
	# Next step. Read vertically, 8 lines of the array (1 page height)
	
	
if __name__ == "__main__":
	main()