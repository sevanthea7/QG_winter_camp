import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array( range(6) )
c = np.arange(6)

print(a, type(a))
print(b, type(b))
print(c, type(c))

t1 = np.arange(6)
t2 = np.arange(24).reshape((4,6))
t3 = np.arange(4).reshape((4,1))
print(t1*t2)
print(t2*t3)

t1 = np.arange(12).reshape(3,4)
print(t1)
print(t1.transpose())
print()
print(t1.T)
print()
print(t1.swapaxes(0,1))

t1 = np.arange(24).reshape(4,6)
m1 = np.matrix(t1)
print(t1[1])
print(m1[1])
print(t1[2:])
print(m1[2:])
print(t1[[0,1,3]])
print(m1[[0,1,3]])
print('xxxxxxxxxxxxxxx')
print(t1[:,3])
print(m1[:,3])
print(t1[:,3:])
print(m1[:,3:])
print(t1[:,[0,3]])
print(m1[:,[0,3]])
print(t1[0:3, 1:4])
print(m1[0:3, 1:4])

c = t1[[0,2], [0,1]]
d = m1[[0,2], [0,1]]
print(t1)
print(c)
print(d)


m = np.matrix(t1)
print(m)

t1 = np.arange(9).reshape(3,3)
t2 = np.arange(10,19).reshape(3,3)
m1 = np.matrix(t1)
m2 = np.matrix(t2)
print(m1)
print(m2)
print(m1*m2)
print(np.multiply(m1,m2))

t1 = np.arange(12).reshape(3,4)
m = np.matrix(t1)
print(t1)
print(m.I)
print(m.T)
print(m.transpose())
print(m.swapaxes(0,1))
