#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# List
s = 'Python-中文'
array = ["sd", 45, "arraydess", s.encode('utf-8'), "last item", 'Apple', 123, True]

print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[3])
print(array[-1])
print(array[-2])
print(array[-3])

array.append("appent item")
print(array[-1])

popitem = array.pop(2)
print(popitem)
print(array)

array.insert(2, "insert item")
print(array)

array[2] = "replace item"
print(array)

array = ["sd", 45, "arraydess", [s.encode('utf-8'), "last item", 'Apple', 123], True]
print(len(array))
print(array)

array = ['Apple', 123, True]
print(len(array))
print(array)

array = ["sd", 45, "arraydess", array, True]
print(len(array))
print(array)


l = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', "test", 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(l[0][0])
print(l[1][2])
print(l[-1][-1])

a = ["c","b","a"]
print(a)
a.sort()
print(a)

# 交集
# 方法一:
a = [2, 3, 4, 5]
b = [2, 5, 8]
tmp = [val for val in a if val in b]
print(tmp)
# [2, 5]

# 方法二
print(list(set(a).intersection(set(b))))

#并集
print (list(set(a).union(set(b))))

#差集
print (list(set(b).difference(set(a)))) # b中有而a中没有的