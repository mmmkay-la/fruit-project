#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import smtplib
import os


def generate_email(sender, recepient, subject, email_body, attachment):
	email_message = EmailMessage()

	email_message["From"] = sender
	email_message["To"] = recepient
	email_message["Subject"] = subject
	email_message.set_content(email_body)

	mime_type, _ = mimetypes.guess_type(attachment)
	attach_filename = os.path.basename(attachment)
	mimetype, subtype = mime_type.split("/", 1)

	with open(attachment, "rb") as attach_file:
		email_message.add_attachment(attach_file.read(), maintype = mimetype, subtype=subtype, filename=attach_filename)

	return email_message

def generate_email_error(sender, recepient, subject, email_body):
	email_message = EmailMessage()

	email_message["From"] = sender
	email_message["To"] = recepient
	email_message["Subject"] = subject
	email_message.set_content(email_body)

	return email_message

def send_email(message):
	mail_server = smtplib.SMTP("localhost") 
	mail_server.send_message(message)
	mail_server.quit()

