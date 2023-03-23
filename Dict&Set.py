#!/usr/bin/env python3
# -*- coding: utf-8 -*-

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
student |= {'Sheep'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if ('Rose' in student):
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素


d = {"Sheep": 55, "Lincheng": 77, "yangjing": 99}
print("%s" %{len(d)})
print(d["Sheep"])
print(d["Lincheng"])
print(d["yangjing"])

for n in d.items():
    print("%15s : %3d" % n)

for n, s in d.items():
    print("%15s : %3d" % (n, s))

d["sheep"] = 102
d["Sheep"] = 102
print(d["Sheep"])
print(d["sheep"])
print(d)

print("sheep is in dict or not %s" % ("sheep" in d))
print("chengjie is in dict or not %s" % ("chengjie" in d))

item = d.get("sheep")
print(item)
item = d.get("chengjie")
print(item)
item = d.get("chengjie", -1)
print(item)

# set
s = set([1, 2, 3])
print(s)

s = set([1, 1, 2, 2, 3, 3, 3])
print(s)

print(len(s))

s.add(4)
print(s)
print(len(s))

s.remove(1)
print(s)
print(len(s))

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print("s1 & s2: %s" % (s1 & s2))

print("s1 | s2: %s" % (s1 | s2))

a = ["c", "b", "a"]
print(a)
a.sort()
print(a)

a = "abc"
print(a.replace("a", "A"))
print(a)

print({x: x+2 for x in (2, 4, 6)})
