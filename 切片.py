#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 获取一个list或者tuple的部分元素

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = l[:4]
print(result)

result = l[1:4]
print(result)

result = l[-4:]
print(result)

result = l[-4:-1]
print(result)

result = l[-1:-4]
print(result)

l = range(100)

result = l[:4]
print(result)

result = l[1:4]
print(result)

result = l[-4:]
print(result)

result = l[-4:-1]
print(result)

result = l[-1:-4]
print(result)

l = list(range(100))

result = l[:4]
print(result)

result = l[10:20]
print(result)

result = l[:]
print(result)

# 所有数，每5个取一个
result = l[::5]
print(result)

# 前10个数，每两个取一个
result = l[:10:2]
print(result)

result = l[-4:-1]
print(result)

result = l[-1:-4]
print(result)

# tuple
result = (0, 1, 2, 4, 5)[:3]
print(result)

#String
result = "ABCDEFGH"[:3]
print(result)

result = "ABCDEFGH"[::3]
print(result)
