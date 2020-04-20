import pandas as pd

'''
def age_18_to_30(a):
    return 18 <= a < 30


def level_a(s):
    return 85 <= s <= 100
'''

students = pd.read_excel("C:/Users/Administrator/PycharmProjects/test/class8.xlsx", index_col='ID')
students = students.loc[students['Age'].apply(lambda a:18 <= a < 30)].\
    loc[students['Score'].apply(lambda s: 85 <= s <= 100)]


print(students)