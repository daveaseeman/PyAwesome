#!/home/vagrant/miniconda3/bin/python

import requests
import bs4

r = requests.get("http://pythonforengineers.com/secret/")

soup = bs4.BeautifulSoup(r.text, "lxml")


for elem in soup.find_all('p'):
    print(elem.text)