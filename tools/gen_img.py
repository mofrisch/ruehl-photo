#!/usr/bin/env python3

# Generate images in different formats and sizes

# © 2024 Moritz Frisch.
# All rights reserved.

# This file is licensed under the MIT License.
# License text is available at https://opensource.org/licenses/MIT

# Usage: python3 gen_img.py <name>
# Example: python3 gen_img.py image

# This script generates images in different formats and sizes.
# It is useful for generating images for responsive web design.
# The script requires Python 3 and the Pillow library.
# Install Pillow with pip install pillow.
# Install the AVIF plugin with pip install pillow-avif-plugin.
# The original image should be in the static/img directory.
# The generated images will be saved in the static/img/gen directory.


import sys
import argparse
import pillow_avif  # Have to import this before importing PIL
from PIL import Image

ver = "1.1.0"


widths = range(100, 2100, 100)
extra_widths = range(2200, 4001, 200)


sizes = [(width, width) for width in widths]

formats = ["jpg", "avif", "webp"]

parser = argparse.ArgumentParser(
    description="Generate images in different formats and sizes"
)
parser.add_argument("name", help="Name of the image file")
parser.add_argument(
    "-l", "--large", action="store_true", help="Generate extra large images"
)
parser.add_argument(
    "--formats",
    help="Comma-separated list of formats (default: " + ", ".join(formats) + ")",
)
parser.add_argument(
    "--sizes",
    help="Comma-separated list of sizes (default: " + ", ".join(map(str, widths)) + ")",
)
parser.add_argument(
    "-v", "--version", action="version", version="%(prog)s " + ver + " by Moritz Frisch"
)

name = parser.parse_args().name
if parser.parse_args().large:
    widths = [*widths, *extra_widths]

original = Image.open("../static/img/" + name + ".jpg")
ratio = original.height / original.width
sizes = [(width, int(width * ratio)) for width in widths]

for size in sizes:
    image = original.copy()
    image = image.resize(size)
    for format in formats:
        image.save("../static/img/gen/" + name + "-" + str(size[0]) + "." + format)
