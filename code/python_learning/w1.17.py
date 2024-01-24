# 行
"""
段
"""
# basic
print("hello")
a = [1, 2, 3, 4, 5,
     6, 7, 8,
     9, 10]
b = 20.1
print(a)
print(b)
del a
c = 3
print(b/c)
d = 'qwert'
print(c)
print(id(c))
print(type(c))
print(d)
print(id(d))
print(type(d))

e = g = 1
f = 2
print('g = ', g)
print('before: ', e, f)
e, f = f, e   # exchange amount
print('after: ', e, f)

i, j, k = 1, 2, 3
print(i, j, k)

# calculation
print('1+2=', i+j)
print('1*2=', i*j)
print('3-2=', k-j)
print("3/2=", k/j)
k = round(k/j)  # 四舍五入
print(k)
print('3//2=', k//j)
print('3%2=', k % j)
print("3^2=", k**j)

j = 0.4
print(i**j)
i **= j
print(i)
i //= j
print(i)
i %= j
print(i)
i += j
print(i)
i *= j
print(i)
i -= j
print(i)
i *= j
print(i)

# string
h = 'abc'
print(h)
print(len(h))
n = 'a "b" c'
print(n)
print(len(n))
print(h+n)
print('\n')
m = '''
a
     b
          c
'''
print(m)
print(len(m))
print(h+n+m)
z = 1.4
w = 1.5
print(round(z))
print(round(w))
print(str(i)+h)

h = 'abcdefghijk'
h = h.replace('a', 'x')
print(h)
print(h[:])
print(h[1:3])
print(h[0:len(h):2])
print(h[::-1])


# input & output
'''
name = input('please input your name: ')
print('hi! ', name+'!')
salary = input('please input your monthly salary: ')
# input 读入的是字符串，需要做计算的时候需要转换成整型变量
print('your annual salary is: ' + str(int(salary)*12))
print('your annual salary is: ', int(salary)*12)
'''

x = 'aabbcc'
y = 'dd'
print(y in x)
print(y not in x)
x = '12345abcdefg一二三四五五五六七12345'
print(len(x))


p = (x*2 for x in range(4))
p = tuple(p)
print(p)
