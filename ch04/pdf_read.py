#!/home/vagrant/miniconda3/bin/python

import PyPDF2

doc = open("triz.pdf", "rb")

pdffile = PyPDF2.PdfFileReader(doc)

print("Number of pages is: ", pdffile.numPages)

print("The first page is: ", pdffile.getPage(0).extractText())

with open("triz.txt", "w") as f:
    for i in range(pdffile.numPages):
        text = pdffile.getPage(i).extractText()
        f.write(text)

doc.close()        