num = input("please enter a number:")
if int(num) < 10:
    print("the number you entered (" + str(num) + ") is under 10")

num = input("please enter a number which is under 10:")
if int(num) < 10:
    print(num)
else:
    print("Error")

score = int(input("enter your score: "))
grade = ''
if score < 60:
    grade = 'unqualified'
elif score < 80:
    grade = 'qualified'
elif score < 90:
    grade = 'good'
elif score <= 100:
    grade = 'excellent'
print("your score is {0}，your grade is {1}".format(score, grade))


score = int(input("please enter your score:"))
grade = ''
if score > 100 or score < 0:
    print("error")
elif score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
    print("your score is {0}, your grade is {1}".format(score, grade))


score = int(input("please enter your score:"))
ygrade = 'ABCDE'
num = 0
if score > 100 or score < 0:
    print("error")
else:
    num = score//10
    if num < 6:
        num = 5
    print("your score is {0}, your grade is {1}".format(score, ygrade[9-num]))

a = 0
while a < 10:
    print(a+1)
    a += 1

num = 1
sum_total = 0
sum_even = 0
sum_odd = 0

while num <= 10:
    sum_total += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    num += 1

print("total sum is: " + str(sum_total))
print("even sum is: " + str(sum_even))
print("odd sum is: " + str(sum_odd))

for x in (20, 30, 40):
    print(x*2, end=' ')
print()
for x in 'abcde':
    print(x, end=' ')

info = {'name': 'xxx', 'age': 18, 'gender': 'M'}
for x in info:
    print(x)
for x in info.keys():
    print(x)

for x in info.values():
    print(x)
for x in info.items():
    print(x)

for i in range(10):
    print(i, end=' ')
print()
for i in range(3, 10):
    print(i, end=' ')
print()
for i in range(3, 10, 2):
    print(i, end=' ')

sum_total = 0
sum_even = 0
sum_odd = 0

for k in range(1, 11):
    sum_total += k
    if k % 2 == 0:
        sum_even += k
    else:
        sum_odd += k

print("total sum is: " + str(sum_total))
print("even sum is: " + str(sum_even))
print("odd sum is: " + str(sum_odd))

for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

for i in range(1, 10):
    for j in range(1, i+1):
        print("{0} * {1} = {2}".format(j, i, (i*j)), end='\t')
    print()

r1 = dict(name='xxx', age=18, gender='M')
r2 = dict(name='yyy', age=21, gender='F')
r3 = dict(name='zzz', age=22, gender='M')
tb = [r1, r2, r3]

for x in tb:
    if x.get('age') >= 19:
        print(x)
    print()

while True:
    a = input("enter 'x'or 'X to exit the programme: ")
    if a.upper() == 'X':
        print("ending")
        break
    else:
        print("continuing")

eenum = 0
slrysum = 0
slry = []
while True:
    s = input("enter the salary for the employee( enter 'x' or 'X' to end ): ")
    if s.upper() == 'X':
        print("ending")
        break
    elif float(s) < 0:
        print("error, please reenter positive number")
        continue
    print("enter success")
    eenum += 1
    slry.append(float(s))
    slrysum += float(s)

print("there are " + str(eenum) + " employees")
print("the salary entered are", slry)
print('the total amount of salary is: ' + str(slrysum))
print('the average salary is: '+str(slrysum/float(eenum)))

cells = [(row, col) for row, col in zip(range(1, 3), range(101, 103))]
for cell in cells:
    print(cell, end=' ')

values = ['a', 'b', 'c', 'd']
order = {odr: value for odr, value in zip(range(1, 5), values)}
print(order)

text = 'im on a hellevator'
char_count = {c: text.count(c) for c in text}
print(char_count)

print({x * 2 for x in range(1, 100) if x % 9 == 0})

n = (x for x in range(1, 20) if x % 9 == 0)
for x in n:
    print(x, end=' ')
for x in n:
    print(x, end=' ')
