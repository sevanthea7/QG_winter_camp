import pandas as pd
import numpy as np

t1 = pd.Series([1,2,3,4])
print(t1)
t2 = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
print(t2)
t3 = pd.Series([1, 2, 3, 4, 5], dtype='float64')
print(t3)

tmp_dict1 = {"name":"xxx", "age":18, "school":"GDUT" }
t4 = pd.Series(tmp_dict1)
print(t4)
import string
tmp_dict2 = {string.ascii_uppercase[i]:i for i in range(10)}	# 推导式创建 大写字母对应其顺序
t5 = pd.Series(tmp_dict2)
print(t5)

print(t2.astype(float))

t6 = pd.Series(np.arange(5), index=list(string.ascii_lowercase[:5]))
print(t6)

print(t4['age'])
print(t4[0])
print(t4[[0,2]])
print(t4[['age','school']])
print(t5[t5>5])


t1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(t1)

t2 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('wxyz'))
print(t2)

d1 = {'name':['xxx', 'yyy'], 'age':[18, 19], 'school':['SZSH', 'GDUT']}
t1 = pd.DataFrame(d1)
print(t1)

d2 = [ {'name':"xxx", 'age':18, 'school':'SZSH'}, {'name':"yyy", 'age':19, 'school':'GDUT'}, {'name':"zzz", 'age':20, 'school':'GDUT'}]
t2 = pd.DataFrame(d2)
print(t2)
d3 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
t3 = pd.DataFrame(d3)
print(t3)
print(t3['one'])

d4 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
t4 = pd.DataFrame(d4)
t4['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
t4.insert(0, column='zero', value=[5,4,3,2])
t4['four'] = t4['one'] + t4['three']
'''
del t4['three']
t4.pop('two')
print(t4)
'''
print(t4.loc['b'])
print(t4.iloc[2])

t1 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns = ['a','b'])
t1 = t1.drop(0)
print(t1)

d1 = { 'one':[1, 2, 3], 'two':[4, 5, 6], 'three':[7, 8, 9] }
t1 = pd.DataFrame(d1, index=['a', 'b', 'c'])
print(t1)
print(t1[0:2])


t1 = pd.DataFrame(['x', 'y', np.nan, [], None, 'z'], columns=['name'])
t1 = t1[['name']].fillna('xx')
print(t1)
t2 = pd.Series(['M', 'F', np.nan, 'F', 'M', None, 'M'])
t1['gender'] = t2
print(t1)
t1[['gender']].fillna(method='ffill')
print(t1)

t1 = pd.DataFrame([[1, 2, 3], [4, 5, None], [7, None, 9], [None, None, None]])
print(t1)
print(t1.dropna())
print(t1.dropna(how='all'))

t1 = pd.DataFrame({'one': ['A', 'A', 'A', 'B', 'A', 'B', 'B', 'B'], 'two': [1, 1, 2, 3, 3, 4, 4, 4]})
print(t1)
print(t1.duplicated())
print(t1.duplicated(keep='last'))
print(t1.drop_duplicates())
print(t1.drop_duplicates(keep='last'))

t1 = pd.DataFrame(np.random.randn(1000,4))
print(t1.describe())
print(t1[np.abs(t1[1])>3])
'''
print(t1[(np.abs(t1)>3).any(axis=1)])
t1[np.abs(t1)>3] = np.sign(t1)*3
print(t1)
print(t1[(np.abs(t1)>3).any(axis=1)])
'''
col = t1[1]
t1.drop(t1[np.abs(col)>3].index,inplace=True)
print(t1)