#!/usr/bin/env python3

from datetime import date
from pathlib import Path
import reports
import emails


def process_data(src_dir):

	report_title = (f"Processed Updated on {date.today():%B %d, %Y}")
	
	fruit_data = []

	for fruit_item in Path(src_dir).iterdir():
		with open(fruit_item, "r") as txt_file:
			fruit = txt_file.readlines()
			fruit_data.append("<br/>")
			fruit_data.append(f"name: {fruit[0].rstrip()}")
			fruit_data.append(f"weight: {fruit[1].rstrip()}")

	report_data = "<br/>".join(fruit_data)

	reports.generate_report("processed.pdf", report_title, report_data)


if __name__ == "__main__":
		process_data("supplier-data/descriptions/")

		email_sender = "automation@example.com"
		email_receipient = "student@example.com"
		email_subject = "Upload Complete - Online Fruit Store"
		email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
		email_attach = "processed.pdf"

		email_message = emails.generate_email(email_sender, email_receipient, email_subject, email_body, email_attach)

		emails.send_email(email_message)