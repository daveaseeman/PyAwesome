#!/home/vagrant/miniconda3/bin/python

import requests
import bs4

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")

print(r.status_code)

#print(r.text)

soup = bs4.BeautifulSoup(r.text, "lxml")

print(soup.title)

for pelem in soup.find_all('p'):
    print(pelem.get_text())


print("\n-------------------------------------\n\n")
for pelem in soup.find_all('a'):
    print(pelem.get('href'))