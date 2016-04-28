#!/usr/bin/python3

import pandas

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

