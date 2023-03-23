#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tuple tuple和list非常类似，但是tuple一旦初始化就不能修改 所以Tuple一般用于常来数组

tuple = ("sheep", "yangyang", "double")
print(tuple)
print(len(tuple))
for n in tuple:
    print("name:%s" % n)

tuple_one = (1)  # tuple_one不是一个tuple 而是 数字 1
# print(len(tuple_one))
print(tuple_one)

tuple_oneitem_int = (1,)
print(len(tuple_oneitem_int))
print(tuple_oneitem_int)

# 可变tuple 技巧
t = ("a", "b", ["A", "B"])
print(len(t))
print(t)

t[2].append("C")
print(len(t))
print(t)

t[2][0] = "X"
t[2][1] = "Y"
t[2][2] = "Z"
print(len(t))
print(t)
