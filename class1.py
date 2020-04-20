import pandas as pd


df = pd.read_excel("E:/共享/15.湾海大厦/塔楼/3.订单/2.铝型材订单/铝材-001 4F~8F立柱横梁铝材订单.xls",
                   header=5, index_col='序号')
df.to_excel("E:/共享/15.湾海大厦/塔楼/3.订单/2.铝型材订单/铝型材总订单.xls")
