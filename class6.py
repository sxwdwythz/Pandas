import pandas as pd

books = pd.read_excel("C:/Users/Administrator/PycharmProjects/test/class6.xlsx", index_col='ID')

books['ListPrice'] = books['ListPrice'].apply(lambda x: x+2)
# books['Price'] = books['ListPrice'] * books['Discount']

'''
for i in range(5, 16):
    books.at[i, 'Price'] = books.at[i, 'ListPrice'] * books.at[i, 'Discount']
'''

print(books)
