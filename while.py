#!/usr/bin/env python3
# -*- coding: utf-8 -*-

array = ["sheep", 1, True, "中午"]
for item in array:
    print(item)

result = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    result += x
    # print(result)
print("for %s " % result)

# range(100)   =  0-99
array = list(range(100))
print("list(range(100)) %s" % array[-1])

array = list(range(101))
print("list(range(101)) %s" % array[-1])


result = 0
for x in range(101):
    result += x
print("for %s " % result)

# while
result = 0
n = 99
while n > 0:
    result += n
    n -= 2
print("while %s " % result)
