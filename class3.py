import pandas as pd


'''
d = {'x':100, 'y':200, 'z':300}
print(d.keys())
print(d.values())
print(d['x'])
s1 = pd.Series(d)                                   #组，类似于字典
print(s1)
print(s1.index)
'''

'''
L1 = [100, 200, 300]
L2 = ['x', 'y', 'y']
s2 = pd.Series(L1, index=L2)
print(s2)
'''

s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
print(s1)
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

df1 = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df1)
df1.to_excel("c:/1.xls")

df2 = pd.DataFrame([s1, s2, s3])
print(df2)
