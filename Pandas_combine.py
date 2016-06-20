#!/usr/bin/python3

import pandas
import re
import matplotlib.pyplot as plt

a=pandas.read_excel("product.xls")
a.dropna(how='all')

a = a[pandas.notnull(a['Price'])]

a['Price in'].fillna('dollars', inplace = True)

b = pandas.read_excel("currency.xls")

b.dropna(inplace=True)


for index, row in a.iterrows():
    if row['Price in'] == 'Pounds':
       a.loc[index,'Price'] = row['Price'] * b['Pounds'][1]
    if  row['Price in'] == 'Euros':
       a.loc[index,'Price'] = row['Price'] * b['Euros'][1]

c=pandas.read_csv('sales_data.csv')

d=pandas.merge(a,c)

with open("return_report.txt", "r") as f:
    returns = f.read()


g = re.findall("(Widget [\w]*)\\nUnits Returned: ([\w]*)", returns)

with open("return_report2.txt", "r") as f:
    returns2 = f.read()

h = re.findall('(Widget [\w]*)\\n([\w]*)', returns2)
for hh in h:
    g.append(hh)


for gg in g:
    if any(a[a['Product Name'].str.contains(gg[0])]):
        local_index = a[a['Product Name'].str.contains(gg[0])].index[0]
        #print("local_index = {}, gg = {} {}".format(local_index,gg[0],gg[1]))
        a.loc[local_index, 'Returns'] = gg[1]

a.fillna(0, inplace = True)

new_a = a[['Product Name','Price','Returns']]

new_a.set_index('Product Name', inplace=True)

new_a = new_a.astype(float)

#ax = new_a.plot(kind='bar', figsize=(12, 8))
#fig = ax.get_figure()
#fig.savefig('asdf.png', dpi = (600))
#fig.show()



new_a.plot(kind='bar',figsize=(12, 8))
plt.savefig("a.png",  dpi = (600))