#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = "sheep"
age = input("请输入Age:")
age = int(age)
if age >= 18:
    print('your name is %s  age is %s your are adult' % (name, age))
    print("if age>=18 is true")
elif age >= 6:
    print('your name is %s  age is %s your are teenager' % (name, age))
    print("if age>=6 is true")
else:
    print('your name is %s  age is %s your are kid' % (name, age))
    print("if is false")
print("not if content")

# 永远不会到 age >= 18
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
a = 0
if a:
    print("%s %s" % (a, True))
a = ""
if "":
    print("%s %s" % (a, True))
a = []
if []:
    print("%s %s" % (a, True))

a = -1
if a:
    print("%s %s" % (a, True))
a = " "
if a:
    print("%s %s" % (a, True))
a = [1]
if a:
    print("%s %s" % (a, True))
