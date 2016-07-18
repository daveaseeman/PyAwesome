#!/home/vagrant/miniconda3/bin/python

import pandas
import re

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


#import pdb
#pdb.set_trace()

aa=pandas.read_excel("product.xls")
aa.dropna(how='all')

aa = aa[pandas.notnull(aa['Price'])]

aa['Price in'].fillna('dollars', inplace = True)

bb = pandas.read_excel("currency.xls")

bb.dropna(inplace=True)


for index, row in aa.iterrows():
    if row['Price in'] == 'Pounds':
       aa.loc[index,'Price'] = row['Price'] * bb['Pounds'][1]
    if  row['Price in'] == 'Euros':
       aa.loc[index,'Price'] = row['Price'] * bb['Euros'][1]

c=pandas.read_csv('sales_data.csv')

d=pandas.merge(aa,c)

with open("return_report.txt", "r") as f:
    returns = f.read()


g = re.findall("(Widget [\w]*)\\nUnits Returned: ([\w]*)", returns)

with open("return_report2.txt", "r") as f:
    returns2 = f.read()

h = re.findall('(Widget [\w]*)\\n([\w]*)', returns2)
for hh in h:
    g.append(hh)


for gg in g:
    if any(aa[aa['Product Name'].str.contains(gg[0])]):
        local_index = aa[aa['Product Name'].str.contains(gg[0])].index[0]
        #print("local_index = {}, gg = {} {}".format(local_index,gg[0],gg[1]))
        aa.loc[local_index, 'Returns'] = gg[1]

aa.fillna(0, inplace = True)

new_a = aa[['Product Name','Price','Returns']]

new_a.set_index('Product Name', inplace=True)

new_a = new_a.astype(float)

#ax = new_a.plot(kind='bar', figsize=(12, 8))
#fig = ax.get_figure()
#fig.savefig('asdf.png', dpi = (600))
#fig.show()



new_a.plot(kind='bar',figsize=(12, 8))
plt.savefig("aa.png",  dpi = (600))