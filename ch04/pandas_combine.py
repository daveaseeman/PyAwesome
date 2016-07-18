#!/home/vagrant/miniconda3/bin/python

import pandas as pd
import re

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

product_data = pd.read_excel("product.xls")
print(product_data)


product_data.dropna(how = 'all', inplace = True)
print(product_data)

product_data = product_data[pd.notnull(product_data['Price'])]
print(product_data)

product_data['Price in'].fillna('dollars', inplace = True)
print(product_data)


currency_file = pd.read_excel('currency.xls')
print(currency_file)


currency_file.dropna(inplace=True)
print(currency_file)

product_data['Price in dollars'] = product_data['Price']
print(product_data)

# A bit of complicated code
for column, row in product_data.iterrows():
    if row['Price in'] == "Pounds":
        product_data.loc[column, 'Price in dollars'] = row['Price'] * currency_file['Pounds'][1]

    if row['Price in'] == "Euros":
        product_data.loc[column, 'Price in dollars'] = row['Price'] * currency_file['Euros'][1]

print(product_data)        


sales_data = pd.read_csv('sales_data.csv')
print(sales_data)

combined_data = pd.merge(product_data, sales_data)
print(combined_data)

with open('return_report.txt', 'r') as f:
    returns = f.read()


returned_products = re.findall("(Widget [\w]*)\\nUnits Returned: ([\d]*)", returns)

print(returned_products)


#Another bit of complicated code!

for return_prod in returned_products:
    if any(combined_data[combined_data['Product Name'].str.contains(return_prod[0])]):
        index_found = combined_data[combined_data['Product Name'].str.contains(return_prod[0])].index[0]

        combined_data.loc[index_found, "Returns"] = int(return_prod[1])

print(combined_data)        

combined_data.to_csv("Combined.csv", index=False)

writer = pd.ExcelWriter("Combined.xlsx")

combined_data.to_excel(writer, index=False)
writer.save()


print("\n\n-----------\n")
combined_data_new = combined_data[['Product Name', 'Sales', 'Returns']]

combined_data_new.set_index('Product Name', inplace=True)

combined_data_new.plot(kind = 'bar', figsize=(15,12))
plt.savefig("products.png")