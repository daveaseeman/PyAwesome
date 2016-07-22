#!/home/vagrant/miniconda3/bin/python

import PyPDF2

doc = open("triz.pdf", "rb")

pdffile = PyPDF2.PdfFileReader(doc)


pdf_writer = PyPDF2.PdfFileWriter()

for i in range(0, pdffile.numPages, 2):
    page = pdffile.getPage(i)

    pdf_writer.addPage(page)

outfile = open("triz2.pdf", "wb")
pdf_writer.write(outfile)

outfile.close()
doc.close()