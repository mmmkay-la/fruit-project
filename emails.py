#!/usr/bin/env python3

"""
NAME : emails.py

FUNCTIONALITY:
  > Generates and sends email (with or without attachment)

HOW TO USE:
1. Import as a module
2. Call generate_email first to build email body (with or without attachment)
3. Call send_email to send email
"""

from email.message import EmailMessage
import mimetypes
import smtplib
import os

def generate_email(sender:str, recipient:str, subject:str, body:str, attachment:str) -> EmailMessage:
	email_message = EmailMessage()

	email_message["From"] = sender
	email_message["To"] = recipient
	email_message["Subject"] = subject
	email_message.set_content(body)

	try:
		if attachment is not None:
			mime_type, _ = mimetypes.guess_type(attachment)
			attach_filename = os.path.basename(attachment)
			mimetype, subtype = mime_type.split("/", 1)

			with open(attachment, "rb") as attach_file:
				email_message.add_attachment(attach_file.read(), maintype = mimetype, subtype=subtype, filename=attach_filename)
	except Exception as e:
		print(f"\nError encountered at generate_email(): {e}")
	return email_message

def send_email(message: EmailMessage):
	try:
		mail_server = smtplib.SMTP("localhost") 
		mail_server.send_message(message)
		mail_server.quit()
	except Exception as e:
		print(f"\nError encountered at send_email(): {e}")

