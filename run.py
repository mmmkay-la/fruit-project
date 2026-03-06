#!/usr/bin/env python3

"""
(1) update cataglog with data form suppliers (image + description)
(2) image & description uploaded separately
(3) send report to supplier about the updates made

(1) monitor system health
(2) send email once system is unhealthy


"""

from pathlib import Path
import requests

def upload_fruit_details(upload_url, src_dir):

	for txt_path in Path(src_dir).iterdir():
		try:
			with open(txt_path , "r") as txt_file:
				fruit_data = {}
				read_fruit = []

				read_fruit = txt_file.readlines()
				fruit_data["name"] = read_fruit[0].strip()
				fruit_data["weight"] = int(read_fruit[1].strip(" lbs\n"))
				fruit_data["description"] = read_fruit[2].strip()
				fruit_data["image_name"] = Path(txt_file.name).stem + ".jpeg"
				
				print(fruit_data)
				response = requests.post(upload_url, json=fruit_data)
				print(f"{response.status_code} status code : {response.reason} for file: {txt_file.name}\n")
		except Exception as e:
			print(f"Error encountered: {e}\n")
			print(txt_file)

if __name__ == "__main__":
	upload_fruit_details("http://34.45.33.144/fruits/", 'supplier-data/descriptions/')