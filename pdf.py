#!/home/vagrant/miniconda3/bin/python
import PyPDF2

# Open our file
file_to_open = open("triz.pdf", "rb")

pdf_file = PyPDF2.PdfFileReader(file_to_open)

print("The number of pages = {}".format(pdf_file.numPages))

# Print 1st page
page = pdf_file.getPage(0)
text = page.extractText()
print(text)


# Let's print the first 4 pages to a text file

with open("triz.txt", "w") as f:
    for i in range(4):
        page = pdf_file.getPage(i)
        text = page.extractText()
        f.write(text)


pdf_writer = PyPDF2.PdfFileWriter()


for page_num in range(0, pdf_file.numPages, 2):
    page = pdf_file.getPage(page_num)
    pdf_writer.addPage(page)

# Open our file
file_to_open2 = open("triz2.pdf", "wb")

pdf_writer.write(file_to_open2)

file_to_open.close()
file_to_open2.close()