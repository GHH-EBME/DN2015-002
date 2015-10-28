#!/usr/bin/env python
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
    width,height =im.size
    print("Image Palette: " + str(im.palette))

    # 1 = (1-bit pixels, black and white, stored with one pixel per byte)
    # L = (8-bit pixels, black and white)
    print("Image Mode: " +im.mode)

    # Need to convert array from mode = 1 to obtain usable data.
    data = np.array(im.convert("L"))
    print(data)
    #print(np.array(im.convert("L"))) # Looks good at this point,

    # Next step. Read each value in the array.
    data2 = []
    for dat in data:
        for d in dat:
            data2.append(d)
    #print(data2)

    # Next step. If 255 then convert to 0, If zero convert to 1.
    # Round up or down other values.
    data3 = []
    for d in data2:
        if (d >=127):
            data3.append(0)
        else:
            data3.append(1)

    # data3 contains a list of pixels that make up the image.
    #If the pixel is set then it is '1' and '0' if it is clear.
    #print(data3)

    # Next step. Convert pixel data into hex format.
    # Assume data is going to be written to a page of 8 pixels high and
    # written from left to right.Each block of 8 pixels make up one column of the image.

    columns= []
    col_count = 0
    offset = 0
    while (col_count < width):
        col = []
        for p in range(0,8):
            x = data3[p + offset]
            col.append(x)
            #pixel = pixel+1
        columns.append(col)
        col_count = col_count + 1
        offset = offset + 8


    print("\n Columns \n")
    print(columns)



    # Next step. Read vertically, 8 lines of the array (1 page height)


if __name__ == "__main__":
    main()
