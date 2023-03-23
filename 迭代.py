#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3


print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next(iter):')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print('next(g()):')
it = g()
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 带下标循环
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)

for i, value in enumerate("ABC"):
    print(i, value)

# 多变量循环
for x, y in [(1, "a"), (2, "b"), (3, "c")]:
    print(x, y)

for x, y, z in [(1, "a", "1A"), (2, "b", "2B"), (3, "c", "3C")]:
    print(x, y, z)


def fab(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b


def fab3(max):
    a, b = 1, 1
    while a < max:
        yield a
        a = b
        b = a + b


result = "fab1:"
for i in fab(20):
    result += (str(i) + ",")
print(result)

result3 = "fab3:"
for i in fab3(20):
    result3 += (str(i) + ",")
print(result3)
