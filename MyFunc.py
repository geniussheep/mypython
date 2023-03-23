def my_max(x, y):
    if x > y:
        return x
    else:
        return y


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


print(my_max(1, 2))

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = x - step * math.sin(angle)
    return nx, ny


x, y = move(10, 100, 60, math.pi / 60)
print(x, y)


def nop():
    pass  # 占位符


print(nop())


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print(power(7))
print(power(5, 4))


def enroll(name, gender, age=8, city="bj"):
    print("name:%s" % name)
    print("name:%s" % gender)
    print("name:%s" % age)
    print("name:%s" % city)
    print("\n")


enroll("sheep", "A")
enroll("sheep", "A", city="SH")
enroll("sheep", "A", city="ui", age=78)
enroll("sheep", "A", 19, "SZ")


# 默认值 坑

def add_end(l=[]):
    l.append('end')
    return l


# 结果没问题
print(add_end([1, 2, 3]))
print(add_end(["x", "y", "z"]))

# 空掉一次 结果ok
print(add_end())

# 空掉第二次以上  坑了
print(add_end())
print(add_end())


# 修复
def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(add_end())
print(add_end())


# 可变参数 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(numbers):
    if not isinstance(numbers, (list, tuple)):
        numbers = []
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc([]))
print(calc([4, 5]))
print(calc([1, 3, 4, 5]))


# *号作为可变参数前缀
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc())
print(calc(4, 5))
print(calc(1, 3, 4, 5))

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))


# 关键参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("Sheep", 30)
person("Sheep", 30, city="sh", job="engineer")

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
# 参数名不受限
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 参数限定住
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


# person('Jack', 24, "Beijing",'Engineer')

person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print('name:', name, 'age:', age, 'args:', args, "city:", city, "job:", job)


person('Jack', 24, 456, "string", 7777, "a arg", city="SH", job="egn")


def person(name, age, *args, city="BJ", job):
    print('name:', name, 'age:', age, 'args:', args, "city:", city, "job:", job)


person('Jack', 24, 456, "string", 7777, "a arg", job="egn")


# 参数组合
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)

f1(1, 2, 3)

f1(1, 2, c=3)

f1(1, 2, 3, 4, 5, 6)

f1(1, 2, 3, 4, 5, 6, ext="7", ext2=8)

f1(1, 2, ext="7")

# f2(1,2)
f2(1, 2, d=3)

f2(1, 2, d=3, ext="4", ext2="78")

# 神奇的事情

args = ("a", "b", "c", 4, 6, 89, "ks")  # tuple
kw = {"d": 78, "for": 1245, "x": '=='}

f1(*args, **kw)

args = ("a", "b", "c")  # tuple
f2(*args, **kw)


def hello(greeting, *args):
    if len(args) == 0:
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))


hello('Hi')  # => greeting='Hi', args=()
hello('Hi', 'Sarah')  # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')  # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names)  # => greeting='Hello', args=('Bart', 'Lisa')


def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():  # 方便的循环dict
        print('%15s  %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)





