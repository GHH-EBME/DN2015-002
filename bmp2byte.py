#!/usr/bin/env python
"""
bmp2byte.py - Convert a *.bmp image into a byte array
"""

from __future__ import print_function
import sys
from PIL import Image
import numpy as np

def main():
    page_height = 8 # Page is 8 pixels high

    im = Image.open("test_image2.bmp")
    #p = np.array(im)
    #print(p)
    print("File Format: " + im.format)
    print("Image Size [W,H]: " + str(im.size))
    width,height =im.size
    page_count = height/page_height # Work out the number of pages
    print("Image Palette: " + str(im.palette))

    # 1 = (1-bit pixels, black and white, stored with one pixel per byte)
    # L = (8-bit pixels, black and white)
    print("Image Mode: " +im.mode)

    # Need to convert array from mode = 1 to obtain usable data.
    data = np.array(im.convert("L"))
    #print(data)
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
    print(data3) # Converting correctly.

    """
    # With a large image there is alot of data to process. Let's split it up into pages before we go any furthur.
    pages = []
    bits_per_page = page_height * width
    i = 0
    for p in data3:
        page = []

        while (i < bits_per_page):
            page.append(p)
            i = i + 1
        i = 0
        pages.append(page)
    #print("Pages: ")
    print(pages)
    ####################################################################
    """
    page_cols = []
    #for each_page in pages:

        # Next step. Convert pixel data into hex format.
        # Assume data is going to be written to a page of 8 pixels high and
        # written from left to right.Each block of 8 pixels make up one column of the image.

    columns= []
    col_count = 0

    while (col_count < width):
        cols = []
        for col in range(0,width):
            column = []
            for pixel in range(0,8):
                x = data3[col + (pixel * width)]
                column.append(x)
            cols.append(column)
            col_count = col_count + 1
        columns.append(cols)

    #page_cols.append(columns)

        #print("\n Columns \n")
    print(cols)
    #print(page_cols)
########################################################################
"""
    # The columns array contains 8 pixel arrays for each column. The values in each sub array need to be converted first into binary then into hex.
    page_hex = []
    for page in page_cols:
        hex_values = []
        for c in columns:
            ##print(c)
            d = 0
            #for c in cmn:
            if c[0] == 1:
                d = d + 128
            if c[1] == 1:
                d = d + 64
            if c[2] == 1:
                d = d +32
            if c[3] == 1:
                d = d + 16
            if c[4] == 1:
                d = d + 8
            if c[5] == 1:
                d = d + 4
            if c[6] == 1:
                d = d + 2
            if c[7] == 1:
                d = d + 1
            h = hex(d)
            hex_values.append(h)
        page_hex.append(hex_values)
    #rint(len(page_hex))
        #print(hex_values)


    f = open('output.txt','wb')
    for c in range(0,page_count):
        for h in page_hex[c]:
            f.write(str(h) + ' ,')
        f.write('\n')
    f.close()
"""
"""
    for page[0] in page_hex:

    # Next step - reformat hex_value array into comma seperated sting of 2 digit hex byte values eg: 0F, 12, E3, ...

        for h in hex_values:
            if h == '0x0':
                print("0x00, ",end="")
                #f.write('0x00, ')
            elif h == '0x1':
                print("0x01, ",end="")
                #f.write('0x01, ')
            elif h == '0x2':
                print("0x02, ",end="")
                #f.write('0x02, ')
            elif h == '0x3':
                print("0x03, ",end="")
                #f.write('0x03, ')
            elif h == '0x4':
                print("0x04, ",end="")
                #f.write('0x04, ')
            elif h == '0x5':
                print("0x05, ",end="")
                #f.write('0x05, ')
            elif h == '0x6':
                print("0x06, ",end="")
                #f.write('0x06, ')
            elif h == '0x7':
                print("0x07, ",end="")
                #f.write('0x07, ')
            elif h == '0x8':
                print("0x08, ",end="")
                #f.write('0x08, ')
            elif h == '0x9':
                print("0x09, ",end="")
                #f.write('0x09, ')
            elif h == '0xa':
                print("0x0a, ",end="")
                #f.write('0x0a, ')
            elif h == '0xb':
                print("0x0b, ",end="")
                #f.write('0x0b, ')
            elif h == '0xc':
                print("0x0c, ",end="")
                #f.write('0x0c, ')
            elif h == '0xd':
                print("0x0d, ",end="")
                #f.write('0x0d, ')
            elif h == '0xe':
                print("0x0e, ",end="")
                #f.write('0x0e, ')
            elif h == '0xf':
                print("0x0f, ",end="")
                #f.write('0x0f, ')
            else:
                #f.write(h + ', ')
                print(str(h) + ', ')
        #print("\n")
    #f.close()
"""

if __name__ == "__main__":
    main()
