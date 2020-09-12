
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate(filename, title, addional_info, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(addional_info, styles["Bodytext"])
    table_style = [("GRID", (0,0), (-1,-1), 1, colors.black),
                   ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                   ("ALGIN", (0, 0), (-1, -1), "CENTER")]
    report_table = Table(data=table_data, style=table_style, hAlign="lEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])    