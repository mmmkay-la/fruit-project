#!/usr/bin/env python3

"""
NAME : reports.py

FUNCTIONALITY:
  > Generates PDF reports

HOW TO USE:
1. Import as a module
2. Report created will be saved in current working directory or filepath used in "attachment"
  ** note: existing report will be overwritten
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment: str , report_title: str, paragraph: str) -> None:

	fruit_report = SimpleDocTemplate(filename=attachment)
	report_style = getSampleStyleSheet()

	title = Paragraph(text=report_title, style=report_style["h1"])
	report_data = Paragraph(text=paragraph, style=report_style["BodyText"])

	fruit_report.build(flowables=[title, report_data])