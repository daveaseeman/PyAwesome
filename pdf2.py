#!/usr/bin/python3

import PyPDF2

# Open our file
file_to_open = open("bitcoin.pdf", "rb")

pdf_file = PyPDF2.PdfFileReader(file_to_open)

print("The number of pages = {}".format(pdf_file.numPages))


for i in range(pdf_file.numPages):
    page = pdf_file.getPage(i)
    text = page.extractText()
    print(text)

file_to_open.close()

