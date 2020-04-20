import pandas as pd
from datetime import date, timedelta


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


books = pd.read_excel("C:/Users/Administrator/PycharmProjects/test/class4.xlsx",
                      skiprows=3, usecols="C:F", index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})
start = date(2018, 1, 1)

for i in books.index:
    # books['ID'].at[i] = i + 1
    books.at[i, 'ID'] = i + 1
    # books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = start + timedelta(days=i)           #日
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)   #年
    # books['Date'].at[i] = add_month(start, i)            #月
    books.at[i, 'Date'] = add_month(start, i)

books.set_index('ID', inplace=True)
print(books)
books.to_excel("C:/Users/Administrator/PycharmProjects/test/class4_result.xlsx")
print("Done!")