#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

email_sender = "automation@example.com"
email_receipient = "student@example.com"
email_body = "Please check your system and resolve the issue as soon as possible"

usage = psutil.cpu_percent(1)
if usage > 80:
	email_subject = "Error - CPU usage is over 80%"
	email_message = emails.generate_email_error(email_sender, email_receipient, email_subject, email_body)
	emails.send_email(email_message)

du = shutil.disk_usage(disk)
free = du.free / du.total * 100
if free < 20:
	email_subject = "Error - Availble disk space is less than 20%"
	email_message = emails.generate_email_error(email_sender, email_receipient, email_subject, email_body)
	emails.send_email(email_message)
 
mem = psutil.virtual_memory()
trsh = 100 * 1024 * 1024 
if mem < trsh:
	email_subject = "Error - Availble memory is less than 100MB"
	email_message = emails.generate_email_error(email_sender, email_receipient, email_subject, email_body)
	emails.send_email(email_message)

if socket.gethosbyname("localhost") != "127.0.0.1":
	email_subject = "Error - localhost cannot be resolved to 127.0.0.1"
	email_message = emails.generate_email_error(email_sender, email_receipient, email_subject, email_body)
	emails.send_email(email_message)
