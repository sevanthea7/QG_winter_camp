from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


x = range(2, 26, 2)
y = [i**2 for i in x]
fig = plt.figure(figsize=(20,8), dpi=80)
plt.plot(x, y)
plt.yticks(range(min(y), max(y)+1)[::20])
plt.xticks(range(min(x), max(x)+1))
plt.savefig('D:\pycharm\pics/w.1.27_pic7.png')
plt.show()

'''
import random
x = range(0, 120)
y = [random.randint(20,35) for i in range(120)]
fig = plt.figure(figsize=(20,8), dpi=80)
_x = list(x)
_xtick_labels = ['10:{}'.format(i) for i in range(60)] + ['11:{}'.format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45)
plt.yticks(range(min(y), max(y)+1))
plt.plot(x, y)
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('10点到12点每分钟的气温变化情况')
plt.savefig('D:/pycharm/pics/w.1.27_pic4.png')
plt.show()
'''
'''
fig = plt.figure(figsize=(20,8), dpi=80)
y_1 = [1, 0, 1, 1, 2, 4, 3, 4, 4, 5, 6, 5, 4, 3, 1, 1, 1, 2, 3, 2]
# y_2 = [1, 1, 1, 3, 2, 3, 1, 0, 3, 3, 4, 4, 6, 2, 0, 1, 0, 1, 2, 3]
x = range(11, 31)
plt.scatter(x, y_1, label='A')
# plt.plot(x, y_2, label='B')
plt.xticks(x)
plt.yticks(range(min(y_1), max(y_1)+1))
plt.xlabel('年龄')
plt.ylabel('个数')
plt.title('11到30岁每年交往人数')
# plt.grid(alpha=0.4)
# plt.legend()
# plt.savefig('D:/pycharm/pics/w.1.27_pic4.png')
plt.show()
'''
'''
import string
import random
fig = plt.figure(figsize=(20,8), dpi=80)
x = [string.ascii_uppercase[i] for i in range(10)]
y = [random.randint(0,200) for i in range(10)]
plt.bar(range(len(x)),y, width=0.3, color='orange')
plt.xticks(range(len(x)), x)
plt.yticks(range(min(y), max(y)+1)[::20])
plt.savefig('D:/pycharm/pics/w.1.27_pic5.png')
plt.show()
'''
'''
a = ['abcd', 'efgh', 'ijkl']
b_1 = [1232,325,32]
b_2 = [1364,1243,234]
b_3 = [1423,452,23]
bar_width = 0.2
x_1 = list(range(len(a)))
x_2 = [i+bar_width for i in x_1]
x_3 = [i+bar_width*2 for i in x_1]

plt.figure(figsize=(20,8), dpi=80)

plt.bar(x_1, b_1, width=bar_width, label='1.27')
plt.bar(x_2, b_2, width=bar_width, label='1.28')
plt.bar(x_3, b_3, width=bar_width, label='1.29')

plt.xticks([i + bar_width for i in range(len(a))], a)
plt.legend()
plt.savefig('D:/pycharm/pics/w.1.27_pic6.png')
plt.show()
'''