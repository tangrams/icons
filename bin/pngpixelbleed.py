# USAGE
# python pngpixelbleed.py input_file [output_file]
#
# input_file: path from the call site to the input image file; supports
#     png, jpg, tiff, gif, and psd formats
# output_file: optional path from the call site to the desired output
#     image file; supports all input formats except psd; if omitted,
#     output will be written to the input file
#
# This script requires the the Pillow python module:
#     http://pillow.readthedocs.org/en/3.1.x/installation.html

import sys, os
from PIL import Image

input_file = sys.argv[1]

output_file = input_file
if len(sys.argv) > 2:
    output_file = sys.argv[2]

input_image = Image.open(input_file)

(width, height) = input_image.size

for x in range(width):
    for y in range(height):
        if x == 0 or x == width - 1 or y == 0 or y == height - 1:
            continue
        input_pixel = input_image.getpixel((x, y))
        if (input_pixel[3] != 0):
            continue
        neighbors = []
        neighbors.append(input_image.getpixel((x + 1, y + 0)))
        neighbors.append(input_image.getpixel((x + 1, y + 1)))
        neighbors.append(input_image.getpixel((x + 0, y + 1)))
        neighbors.append(input_image.getpixel((x - 1, y + 1)))
        neighbors.append(input_image.getpixel((x - 1, y + 0)))
        neighbors.append(input_image.getpixel((x - 1, y - 1)))
        neighbors.append(input_image.getpixel((x + 0, y - 1)))
        neighbors.append(input_image.getpixel((x + 1, y - 1)))
        neighbor_colors = [n for n in neighbors if n[3] != 0]
        (r_avg, g_avg, b_avg, a_avg) = (0, 0, 0, 0)
        for n in neighbor_colors:
            r_avg += n[0] / len(neighbor_colors)
            g_avg += n[1] / len(neighbor_colors)
            b_avg += n[2] / len(neighbor_colors)
        if (len(neighbor_colors) > 0):
            input_image.putpixel((x, y), (r_avg, g_avg, b_avg, a_avg))

with open(output_file, 'wb') as f:
    input_image.save(f)
