#!/usr/bin/env python3

"""
(1) update cataglog with data form suppliers (image + description)
(2) image & description uploaded separately
(3) send report to supplier about the updates made

(1) monitor system health
(2) send email once system is unhealthy


"""

from PIL import Image
from pathlib import Path

def modify_image(src_dir):

	img_type = ('.jpeg', 'jpg')

	for img_file in Path(src_dir).iterdir():
		try:
			if img_file.suffix.lower() not in img_type:
				with Image.open(img_file) as img:
					img.resize((600,400)).convert("RGB").save(src_dir + Path(img.filename).stem.split(".")[0] + ".jpeg", "JPEG")
		except Exception as e:
			print(f"Error opening image: {e}\n")

if __name__ == "__main__":
	modify_image("supplier-data/images/")