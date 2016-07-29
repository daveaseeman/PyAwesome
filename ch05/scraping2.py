#!/home/vagrant/miniconda3/bin/python

import requests
import bs4
import re

r = requests.get("http://pythonforengineers.com/dummy-sales-page/")

soup = bs4.BeautifulSoup(r.text, "lxml")

prices = []
for elem in soup.find_all('p'):
    #print(elem.text)
    price_found = re.findall("Price for Item ([\w]*): \$([\w]*)", elem.text)
    if price_found:
        #print(price_found)
        prices.append(price_found)

print(prices)
print(prices[0])
