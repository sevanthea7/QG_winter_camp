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
