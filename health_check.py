#!/usr/bin/env python3

"""
NAME : health_check.py

FUNCTIONALITY:
  > Performs system health checks and sends email

HOW TO USE:
1. chmod +x health_check.py
2. Run Program
"""

import shutil
import psutil
import socket
import emails

email_sender = "automation@example.com"
email_recipient = "student@example.com"
email_body = "Please check your system and resolve the issue as soon as possible"

sys_check = []

usage = psutil.cpu_percent(1)
if usage > 80:
	email_subject = "Error - CPU usage is over 80%"
	sys_check.append(email_subject)

du = shutil.disk_usage("/")
free = du.free / du.total * 100
if free < 20:
	email_subject = "Error - Availble disk space is less than 20%"
	sys_check.append(email_subject)
 
mem = psutil.virtual_memory()
trsh = 100 * 1024 * 1024 
if mem.free < trsh:
	email_subject = "Error - Availble memory is less than 100MB"
	sys_check.append(email_subject)

if socket.gethostbyname("localhost") != "127.0.0.1":
	email_subject = "Error - localhost cannot be resolved to 127.0.0.1"
	sys_check.append(email_subject)

if len(sys_check) == 0: print("Everything looks good!")
else:
	print("Following issues found. Please check: ")
	for error_subj in sys_check:
		print(f"\t{error_subj}")
		email_message = emails.generate_email(sender=email_sender, recipient=email_recipient, subject=error_subj, body=email_body, attachment=None)
		#emails.send_email(email_message)

