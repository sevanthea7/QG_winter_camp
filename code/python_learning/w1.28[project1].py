import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

train = pd.read_csv("D:/【Worksheet6】QG/QG_winter_camp/data/train.csv")
# print(train)
# print(train.describe())
# print(train.info())
# print(train.isna().sum())
# age_mean = train['Age'].mean()
# print(age_mean)
train['Age'] = train['Age'].fillna(method='ffill')
# print(train['Embarked'].value_counts())
train['Embarked'] = train['Embarked'].fillna('S')
# print(train['Cabin'].value_counts())
del train['Cabin']
# print(train.isnull().sum())


# 总体生还率
survived_total = train['Survived'].value_counts()
fig = plt.figure(figsize=(5,5), dpi=80)
# print(survived_total)
plt.pie(survived_total, textprops=dict(size=12), explode=[0, 0.1], autopct='%.2f%%', labels=['丧生','幸存'], pctdistance=0.5, labeldistance=0.7, colors=['#6495ED', '#FFDEAD'])
plt.title('总体生还率')
plt.savefig("D:/pycharm/pics/titanic-pics/总体生还率.png")
plt.show()

# 幸存男女比例
survived_sex = train.groupby(by='Sex')['Survived'].value_counts()
survived_sex_num = train.groupby(by='Sex')['Survived'].sum()
sex = train['Sex'].value_counts()
sex_num = train['Sex'].sum()
# print(sex)
# print(survived_sex_num)
plt.figure(figsize=(15,5), dpi=80)
pie1 = plt.subplot(1, 3, 2)
pie2 = plt.subplot(1, 3, 3)
pie3 = plt.subplot(1, 3, 1)
pie1.pie(survived_sex.loc['female'], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#FFC1C1', '#FFF0F5'], startangle=45)
pie2.pie(survived_sex.loc['male'][::-1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#BFEFFF', '#E0FFFF'], startangle=150)
pie3.pie(sex, textprops=dict(size=12), explode=[0, 0.05], autopct='%.2f%%', labels=['男性', '女性'], pctdistance=0.5, labeldistance=0.7, colors=['#BFEFFF', '#FFC1C1'], startangle=60)
pie1.set_title('女性生还率')
pie2.set_title('男性生还率')
pie3.set_title('男女性别比')
plt.savefig("D:/pycharm/pics/titanic-pics/幸存男女比例饼图.png")
# plt.show()

plt.figure(figsize=(8,8), dpi=80)
bar_width = 0.4
bar_positions = range(2)
plt.bar(bar_positions, sex, width=bar_width, color=['#E0FFFF', '#FFF0F5'], label=['总人数 - 男性', '总人数 - 女性'])
plt.bar(bar_positions, survived_sex_num[::-1], width=bar_width, color=['#BFEFFF', '#FFC1C1'], label=['生还人数 - 男性', '生还人数 - 女性'])
plt.yticks(range(0,600,30))
plt.legend()
plt.xticks(bar_positions, labels=['男性', '女性'])
plt.savefig("D:/pycharm/pics/titanic-pics/幸存男女比例条形图.png")
# plt.show()

# 幸存年龄比例
plt.figure(figsize=(10,5), dpi=80)
age = train['Age']
age_num = np.histogram(age, range=[0,80], bins=16)

survived_age_num = []
for n_age in range(5,81,5):
    num = train.loc[ (age >= n_age-5)&(age <= n_age) ]['Survived'].sum()
    survived_age_num.append(num)

# print(age_num)
# print(survived_age_num)
plt.bar(np.arange(2,78,5)+0.5,age_num[0], width=5,label='总人数',alpha=0.8, color='#6495ED')
plt.bar(np.arange(2,78,5)+0.5,survived_age_num,width=5,label='生还人数', color='#FFDEAD')
plt.xticks(range(0,81,5))
plt.yticks(range(0,141,10))
plt.xlabel('年龄', fontsize=15)
plt.ylabel('人数', fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(alpha=0.4)
plt.legend()
plt.savefig("D:/pycharm/pics/titanic-pics/幸存年龄比例.png")
# plt.show()


# 不同港口幸存比例
plt.figure(figsize=(20,5), dpi=80)
survived_embarked = train.groupby(by='Embarked')['Survived'].value_counts()
embarked = train['Embarked'].value_counts()
# print(survived_embarked)
pie1 = plt.subplot(1, 4, 1)
pie2 = plt.subplot(1, 4, 2)
pie3 = plt.subplot(1, 4, 3)
pie4 = plt.subplot(1, 4, 4)
pie2.pie(survived_embarked.loc['C'], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#A5682A', '#E0B979'], startangle=80)
pie3.pie(survived_embarked.loc['Q'][::-1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#8C6488', '#D8BFD8'], startangle=110)
pie4.pie(survived_embarked.loc['S'][::-1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#997A41', '#E6D59F'], startangle=120)
pie1.pie(embarked, textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['法国瑟堡市乘客', '爱尔兰昆士敦乘客', '英国南安普顿乘客'], pctdistance=0.5, labeldistance=0.7, colors=['#A5682A', '#8C6488', '#997A41'], startangle=45)
pie1.set_title('各港口登船比例')
pie2.set_title('法国瑟堡市乘客登船生还率')
pie3.set_title('爱尔兰昆士敦乘客登船生还率')
pie4.set_title('英国南安普顿乘客登船生还率')
plt.savefig("D:/pycharm/pics/titanic-pics/不同港口幸存比例.png")
# plt.show()


# 不同船舱生还比例
plt.figure(figsize=(20,5), dpi=80)
survived_pclass = train.groupby(by='Pclass')['Survived'].value_counts()
pclass = train['Pclass'].value_counts()
# print(survived_pclass)
pie1 = plt.subplot(1, 4, 1)
pie2 = plt.subplot(1, 4, 2)
pie3 = plt.subplot(1, 4, 3)
pie4 = plt.subplot(1, 4, 4)
pie2.pie(survived_pclass.loc[1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#4C6E8C', '#B0C4DE'], startangle=65)
pie3.pie(survived_pclass.loc[2][::-1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#8A5288', '#D8BFD8'], startangle=95)
pie4.pie(survived_pclass.loc[3][::-1], textprops=dict(size=12), explode=[0, 0.12], autopct='%.2f%%', labels=['幸存', '丧生'], pctdistance=0.5, labeldistance=0.7, colors=['#607C59', '#B0C985'], startangle=135)
pie1.pie(pclass, textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['一等舱乘客', '二等舱乘客', '三等舱乘客'], pctdistance=0.5, labeldistance=0.7, colors=['#4C6E8C', '#8A5288', '#607C59'], startangle=75)
pie1.set_title('不同船舱等级比例')
pie2.set_title('一等舱生还率')
pie3.set_title('二等舱生还率')
pie4.set_title('三等舱生还率')
plt.savefig("D:/pycharm/pics/titanic-pics/不同船舱生还比例.png")
# plt.show()

# 不同地区登船船舱比例
plt.figure(figsize=(20,5), dpi=80)
embarked_pclass = train.groupby(by='Embarked')['Pclass'].value_counts()
# print(embarked_pclass)
pie1 = plt.subplot(1, 4, 1)
pie2 = plt.subplot(1, 4, 2)
pie3 = plt.subplot(1, 4, 3)
pie4 = plt.subplot(1, 4, 4)
pie2.pie(embarked_pclass.loc['C'], textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['一等舱', '二等舱', '三等舱'], pctdistance=0.5, labeldistance=0.7, colors=['#A5682A', '#D4B999', '#EFD8C6'], startangle=90)
pie3.pie(embarked_pclass.loc['Q'][::-1], textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['一等舱', '二等舱', '三等舱'], pctdistance=0.5, labeldistance=0.7, colors=['#8C6488', '#C6B2CC', '#E8D4E6'], startangle=350)
pie4.pie(embarked_pclass.loc['S'][::-1], textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['一等舱', '二等舱', '三等舱'], pctdistance=0.5, labeldistance=0.7, colors=['#997A41', '#D8C88A', '#EFE5C1'], startangle=100)
pie1.pie(embarked, textprops=dict(size=12), explode=[0.05, 0.05, 0.05], autopct='%.2f%%', labels=['法国瑟堡市乘客', '爱尔兰昆士敦乘客', '英国南安普顿乘客'], pctdistance=0.5, labeldistance=0.7, colors=['#A5682A', '#8C6488', '#997A41'], startangle=45)
pie1.set_title('各港口登船比例')
pie2.set_title('法国瑟堡市乘客登船生还率')
pie3.set_title('爱尔兰昆士敦乘客登船生还率')
pie4.set_title('英国南安普顿乘客登船生还率')
plt.savefig("D:/pycharm/pics/titanic-pics/不同地区登船船舱比例.png")
# plt.show()


# 不同票价幸存率分布
fare_count = train.groupby(by='Fare')['Survived'].value_counts()
fare_count = pd.DataFrame(fare_count)
fare_count.rename(columns={'Survived':'count'},inplace=True)
fare_count.reset_index(inplace=True)
# print(fare_count)
fare_num = fare_count.groupby(by='Fare')['count'].sum()
fare_num = pd.DataFrame(fare_num)
fare_num.rename(columns={'count':'Total'},inplace=True)
# print(fare_num)
fare_survived = fare_count.loc[fare_count['Survived']==1]
fare_survived = fare_survived.merge(fare_num,left_on='Fare',right_index=True,how='inner')
fare_death = fare_count.loc[fare_count['Survived']==0]
fare_death = fare_death.merge(fare_num,left_on='Fare',right_index=True,how='inner')

survived_rate = fare_survived['count'].div(fare_survived['Total'])
survived_rate.index = fare_survived['Fare']
death_rate = fare_death['count'].div(fare_death['Total'])
death_rate.index = fare_death['Fare']

plt.figure(figsize=(20,5), dpi=80)
sct1 = plt.subplot(1, 2, 1)
sct2 = plt.subplot(1, 2, 2)
sct1.scatter(survived_rate.index,survived_rate,marker='o',color='r')
x_list = [i for i in range(0, 520, 20)]
y_list = [i/10 for i in range(11)]

sct1.set_xticks(x_list)
sct1.set_yticks(y_list)
sct1.set_xlabel('票价', fontsize=15)
sct1.set_ylabel('生还率', fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
sct1.set_title('乘客生还率和票价关系散点图')

sct2.scatter(death_rate.index,death_rate,marker='^',color='b')
sct2.set_title('乘客死亡率和票价关系散点图')
sct2.set_xticks(x_list)
sct2.set_yticks(y_list)
sct2.set_xlabel('票价', fontsize=15)
sct2.set_ylabel('死亡率', fontsize=15)
plt.savefig("D:/pycharm/pics/titanic-pics/不同票价幸存率分布.png")
plt.show()