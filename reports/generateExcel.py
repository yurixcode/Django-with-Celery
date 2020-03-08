# Django
from django.contrib.auth import get_user_model

# Excel Module
import xlsxwriter

workbook = xlsxwriter.Workbook('./files/hello.xlsx')

worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('Segunda hoja')

worksheet.write('A1', 'Hello world')

worksheet2.write('A1', 'Hello world')

workbook.close()