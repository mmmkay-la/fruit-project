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
import requests

def img_upload(upload_url, src_dir):

	img_type = ('.jpg','.jpeg')

	for img_path in Path(src_dir).iterdir():
		try:
			if img_path.suffix.lower() in img_type:
				with open(img_path , "rb") as img:
					img_file = { "file":img }

					response = requests.post(upload_url, files=img_file)
					print(f"{response.status_code} status code : {response.reason} for image: {img}\n")
		except Exception as e:
			print(f"Error encountered: {e}\n")

if __name__ == "__main__":
	img_upload("http://34.45.33.144/upload/", 'supplier-data/images/')