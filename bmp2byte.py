#!/usr/bin/env python
"""
bmp2byte.py - Convert a *.bmp image into a byte array
"""
# Imports
from __future__ import print_function
import sys
from PIL import Image
import numpy as np

# Configuration
page_height_px = 8 # Page is 8 pixels high
img_file = "test_image2.bmp"

def main():
    ####################################################################
    # Stage 1: Extract Pixel Data From Image
    ####################################################################
    data = get_data(img_file)
    width,height = extract_img_data(data)
    page_count = calculate_pages(width,height,page_height_px)
    data2 = convert_mode(data)
    data3 = create_data_array(data2)
    checked_data = check_data_len(data3,8192)
    data4 = modify_data_values(checked_data)
    # data4 contains a list of pixels that make up the image.
    #If the pixel is set then it is '1' and '0' if it is clear.
    #print(data4) # Converting correctly.
    ####################################################################
    # Stage 2: Split Pixel Data into Display Pages
    ####################################################################

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
    # Stage 3: Reformat Display Page into Verticle Columns
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
    """
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
def get_data(data_file):
    f = Image.open(data_file)
    return f
def extract_img_data(img_file):
    print("File Format: " + img_file.format)
    print("Image Size [W,H]: " + str(img_file.size))
    print("Image Palette: " + str(img_file.palette))
    # 1 = (1-bit pixels, black and white, stored with one pixel per byte)
    # L = (8-bit pixels, black and white)
    print("Image Mode: " +img_file.mode)
    img_width,img_height = img_file.size
    return img_width,img_height
def convert_mode(data_to_convert):
    # Need to convert array from mode = 1 to obtain usable data.
    converted_data = np.array(data_to_convert.convert("L"))
    print("Image Mode Converted to 'L'")
    return converted_data
def calculate_pages(img_width, img_height, page_height):
    # Dimensions all in pixels
    page_count = img_height/page_height
    return page_count
def check_data_len(data,expected_length):
    x = len(data)
    if (x == expected_length):
        print("Data Length Check: Pass")
    else:
        print("Data Length Check: Failed")
        print("Expected Length: " + str(expected_length))
        print("Actual Length: " + str(x))
        sys.exit("Invalid Data")
    return data
def create_data_array(data):
    # Read each value into array.
    data_array = []
    for dat in data:
        for d in dat:
            data_array.append(d)
    return data_array
def modify_data_values(data):
    # If 255 then convert to 0, If zero convert to 1.
    # Round up or down other values.
    data_array = []
    for d in data:
        if (d >=127):
            data_array.append(0)
        else:
            data_array.append(1)
    return data_array



if __name__ == "__main__":
    main()
