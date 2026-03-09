#!/usr/bin/env python3

"""
NAME : changeImage.py
FUNCTIONALITY:
  > resizes image to 600x400 and converting them to JPEG

HOW TO USE:
1. Run chmod +x changeImage.py
2. Run Program
3. Prompt will be displayed asking for a Valid Existing Source Directory (Absolute or Relative path)
4. Prompt will be displayed asking for Image size (in px). Follow format: width x height
5. Upon successful run, modified images will be stored in the same source directory.
	** note: will overwrite existing images.
"""

from PIL import Image
from pathlib import Path
import re

def modify_image(src_dir: str, img_size: tuple) -> None:

# Get files from Source Directory

	for img_file in Path(src_dir).iterdir():
		try:
			# Open each image to resize and save as jpeg
			with Image.open(img_file) as img:
				img.resize(img_size).convert("RGB").save(src_dir + Path(img.filename).stem.split(".")[0] + ".jpeg", "JPEG")
		except Exception as e:
			# Throw Exception if error encountered when opening file
			print(f"\nError opening image: {e}")

if __name__ == "__main__":

	# (1) Ask for user input for source directory
	src_dir = Path(input("\nEnter Source Directory: "))
	path_exists = src_dir.is_dir()

	# Validate entered source directory
	while path_exists == False:
		src_dir = Path(input("No existing Source Directory. Please enter a Valid Source Directory: "))
		if src_dir.is_dir():
			path_exists = True

	# Validate entered image size
	pattern = r"\d{,4} *x *\d{,4}"
	img_size = input("Enter image size (in px) [width x height]: ")
	result = re.search(pattern, img_size)

	while result is None:
		img_size = input("Please follow the format (upto 9999x9999): [width x height]: ")
		result = re.search(pattern, img_size)

	img_size = tuple(int(i) for i in img_size.split("x"))

	# Function call to modify image
	modify_image(str(src_dir)+"/", img_size)

