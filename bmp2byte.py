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
output_file = "output.txt"

def main():
    ####################################################################
    # Stage 1: Extract Pixel Data From Image
    ####################################################################
    data = get_data(img_file)
    width,height = extract_img_data(data)
    # TODO: Check image size. The script is designed around images where
    #       the height and width are multiples of 8. If the image does
    #       not meet this criteria then an extra stage of padding the
    #       image with additional data will be required.
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
    # Calculate the number of display pages based on image size
    page_count = calculate_pages(width,height,page_height_px)
    pixels_per_page = page_height_px * width
    # With a large image there is alot of data to process. Let's split it up into pages before we go any furthur.
    pages = get_pages(page_count,pixels_per_page,data4)

    ####################################################################
    # Stage 3: Reformat Display Page into Vertical Columns
    ####################################################################
    #TODO: change width variable as this is taken from the original
    #      image. If this value is not a multiple of 8 then the code
    #      might not work. Once image padding is implemented for images
    #      that require padding, the width variable should refer to the
    #      padded value.
    converted_pages = convert_pages(pages,width,page_height_px)
    image_data = converted_image(converted_pages)
    #print(image_data)

    ####################################################################
    # Stage 4: Store Output in a file
    ####################################################################
    save_to_file(output_file, image_data)

    ####################################################################
    # End
    ####################################################################
    sys.exit("Conversion Complete")
    ####################################################################

# Functions
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
def get_pages(page_count,pixels_per_page,data):
    pages = []
    array_pointer = 0
    i = 0
    while (len(pages) < 8):
        page = []

        while (i < pixels_per_page):
            page.append(data[array_pointer])
            array_pointer = array_pointer + 1
            i = i + 1
        i = 0
        pages.append(page)

    #print(pages)
    return pages
def convert_pages(pages, page_width, page_height):
    # Convert the data for each page into column data
    converted_pages = []
    for page in pages:
        # Change the data format from rows into columns
        p = page2col(page, page_width, page_height)
        # p now contains lists of the data within each column [MSB ... LSB]
        # The column data is in binary. We want to convert it to hex.
        hex_page = col2hex(p)
        converted_pages.append(hex_page)
    return converted_pages
def page2col(page_data, page_width, page_height):
    cols = []
    column_count = 0
    # Reuse the get_pages() function to split the page down into rows
    rows = get_pages(page_height, page_width, page_data)
    while (column_count < page_width):
        column_binary = []
        for row in rows:
            column_binary.append(row[column_count])
        column_binary.reverse()
        cols.append(column_binary)
        column_count = column_count + 1
    # cols now contains lists of the data within each column [MSB ... LSB]
    return cols
def col2hex(col_data):
    # col_data contains 8 pixel lists for each column MSB..LSB. The values
    # in each list need to be converted first into decimal then into hex.
    col_hex = []
    for c in col_data:
        d = 0           # Decimal Value
        # Apply binary weighting to each bit
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
        h = hex(d)      # Decimal to Hex Conversion
        col_hex.append(h)
    return col_hex
def converted_image(converted_pages):
    image_hex= []
    for page in converted_pages:
        for col in page:
            image_hex.append(col)
    return image_hex
def save_to_file(output_file, image_data):
    f = open(output_file,'wb')
    #for c in range(0,page_count):
    row_count = 0
    row_count2 = 0
    for h in image_data:

        if (len(h) == 4):
            pass
            #f.write(str(h) + ' ,')
        else: #Add missing leading zero
            h = h[:2] + '0' + h[2:]
        f.write(str(h) + ', ')

        row_count = row_count + 1

        # Add additional separators to output
        if row_count == 16:
            f.write('\n')
            row_count = 0
            row_count2 = row_count2 + 1
        if row_count2 == 8:
            f.write('\n')
            row_count2 = 0

    f.close()
if __name__ == "__main__":
    main()
