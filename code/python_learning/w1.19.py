def add(a, b, c):
    total = a + b + c
    print("*"*total)
    return total


k = 10


def f():
    b = 3
    global k
    k = 5
    print(locals())  # 打印全部局部变量
    print(globals())  # 打印全部全局变量


add(1, 2, 3)
x = add
y = x
x(1, 1, 1)
y(2, 2, 2)
f()
print(k)


f = lambda a, b, c: a+b+c


class Student:
    school = 'GDUT'
    cnt = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.cnt += 1

    def say_score(self):
        print('my school is ' + Student.school)
        print('{0} "Student" content is created.'.format(Student.cnt))
        print('{0}\'s score is {1}'.format(self.name, self.score))


class School:
    school = 'GDUT'

    def __init__(self, name):
        self.name = name

    @classmethod
    def print_school_name(cls):
        print('my school is ' + cls.school)

    @staticmethod
    def add(a, b):
        print('{0} + {1} = {2}'.format(a, b, a + b))
        return a+b


class TestPri:
    __school = 'GDUT'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_info(self):
        print('my age is', self.__age)
        print('my school is', self.__school)

    def __primeth(self):
        print('assess PriMeth')


print(TestPri._TestPri__school)
m = TestPri('xxx', 18)
m._TestPri__primeth()
m.say_info()

print(f(1, 2, 3))
g = [lambda a: a+2, lambda b: b*3, lambda c: c*4]
print(g[0](1), g[1](2), g[2](3))

s1 = Student('aaa', 11)
s2 = Student('bbb', 12)
s1.say_score()


class Person:
    def __init__(self, name, age):
        print('create person info')
        self.name = name
        self.age = age

    def say_age(self):
        print('{0} age is {1}'.format(self.name, self.age))


class NewPerson(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        print('create new person info')
        self.score = score

    def say_score(self):
        print('{0} score is {1}'.format(self.name, self.score))

    def say_age(self):
        print('my age is', self.age)


s1 = NewPerson('xxx', 18, 90)
s1.say_age()
s1.say_score()

class A: pass
class B(A): pass
class C(B): pass

print(C.mro())

class WhoEats:
    def eat(self):
        print('I am eating')


class BY(WhoEats):
    def eat(self):
        print('BY EATS MUTTON')

class Quokka(WhoEats):
    def eat(self):
        print('QUOKKA EATS amkn')


def hungry(h):
    h.eat()


hungry(BY())
hungry(Quokka())


class CPU:
    def calculation(self):
        print('CPU calculating')


class Screen:
    def display(self):
        print('Screen displaying')


class Phone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


c = CPU()
s = Screen()
p = Phone(c, s)
p.cpu.calculation()
p.screen.display()
