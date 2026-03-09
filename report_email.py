#!/usr/bin/env python3

"""
NAME : report_email.py
FUNCTIONALITY:
  (1) Process data for PDF Report and
  (2) Send Email with PDF Report as attachment

HOW TO USE:
1. Run chmod +x report_email.py
2. Run Program
3. Prompt will be displayed asking for a Valid Existing Source Directory (Absolute or Relative path)
4. Prompt will be displayed asking for Report Filename (pdf format)
5. Upon successful PDF report generation, email wil be sent to target recipient with the PDF report as attachment
  ** note: existing report will be overwritten
"""

from datetime import date
from pathlib import Path
import reports
import emails


def process_data(src_dir: str, filename: str) -> None:

	report_title = (f"Processed Updated on {date.today():%B %d, %Y}")
	
	fruit_data = []

	# Read Fruit Details, name & weight, from their corresponding text file
	try:
		for fruit_item in Path(src_dir).iterdir():
			if fruit_item.name.endswith(".txt"):
				with open(fruit_item, "r") as txt_file:
					fruit = txt_file.readlines()
					fruit_data.append("<br/>")
					fruit_data.append(f"name: {fruit[0].rstrip()}")
					fruit_data.append(f"weight: {fruit[1].rstrip()}")

		report_data = "<br/>".join(fruit_data)

		# Generated report will be saved in filename (includes filepath)
		reports.generate_report(filename, report_title, report_data)
		if Path(filename).is_file():
			print(f"\nPDF Report created and saved: {filename}")
		else:
			print("\nPDF Report creation failed.")

	except Exception as e:
		print(f"\nError encountered at process_data(): {e}")

if __name__ == "__main__":
	
	# (1) Ask user input for source directory
	src_dir = Path(input("\nEnter Source Directory: "))
	path_exists = src_dir.is_dir()

	# Validate entered source directory 
	while path_exists == False:
		src_dir = Path(input("No existing Source Directory. Please enter a Valid Source Directory: "))
		if src_dir.is_dir():
			path_exists = True
	
	# (2) Ask for report filename for the PDF report
	filename = input("\nEnter report filename (filepath/filename.pdf): ")
	if not filename.endswith(".pdf"):
		filename += ".pdf"
	
	src_dir = str(src_dir)+"/"

	process_data(src_dir,filename)

	# Setup email variables for sending report
	email_sender = "automation@example.com"
	email_recipient = "student@example.com"
	email_subject = "Upload Complete - Online Fruit Store"
	email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	try:
		email_message = emails.generate_email(sender=email_sender, recipient=email_recipient, subject=email_subject, body=email_body, attachment=filename) 
		emails.send_email(email_message)
	except Exception as e:
		print(f"\nError encountered at main(): {e}")


