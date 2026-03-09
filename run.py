#!/usr/bin/env python3

"""
NAME : run.py

FUNCTIONALITY:
  (1) Upload Fruit Image and Description to external IP server
  (2) Status Code aand Message displayed

HOW TO USE:
1. Modify upload_url for Fruit Upload and src_dir for target source directory
2. Run chmod +x run.py
2. Run Program
3. Program will read through text files to get the Fruit details and POST each to upload url
"""

from pathlib import Path
import requests

def upload_fruit_details(upload_url: str, src_dir:str) -> None:

	for txt_path in Path(src_dir).iterdir():
		if txt_path.name.endswith(".txt"):
			try:
				with open(txt_path , "r") as txt_file:
					fruit_data = {}
					read_fruit = []

					read_fruit = txt_file.readlines()
					fruit_data["name"] = read_fruit[0].strip()
					fruit_data["weight"] = int(read_fruit[1].strip(" lbs\n"))
					fruit_data["description"] = read_fruit[2].strip()
					fruit_data["image_name"] = Path(txt_file.name).stem + ".jpeg"
					
					response = requests.post(upload_url, json=fruit_data)
					print(f"{response.status_code} status code : {response.reason} for file: {txt_file.name}\n")

			except Exception as e:
				print(f"Error encountered at upload_fruit_details(): {e}\n")

if __name__ == "__main__":

	upload_fruit_details("http://34.82.173.147/fruits/", 'supplier-data/descriptions/')