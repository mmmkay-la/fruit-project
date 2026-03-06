#!/usr/bin/env python3


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from datetime import date
from pathlib import Path


def generate_report(src_dir):

	fruit_report = SimpleDocTemplate("processed.pdf")
	report_style = getSampleStyleSheet()

	report_title = Paragraph(f"Processed Updated on {date.today():%B %d, %Y}", report_style["h1"])
	
	fruit_data = []

	for fruit_item in Path(src_dir).iterdir():
		with open(fruit_item, "r") as txt_file:
			fruit = txt_file.readlines()
			fruit_data.append("<br/>")
			fruit_data.append(f"name: {fruit[0].rstrip()}")
			fruit_data.append(f"weight: {fruit[1].rstrip()}")


	report_data = Paragraph("<br/>".join(fruit_data))
	
	fruit_report.build([report_title, report_data])

if __name__ == "__main__":
		generate_report("supplier-data/descriptions/")