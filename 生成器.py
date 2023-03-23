#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [x * x for x in range(10)]
print(l)

g = (x * x for x in range(10))
for x in range(10):
    print(next(g))

g = (x * x for x in range(10))
for x in g:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


fib(10)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b, n = b, a + b, n + 1
    return 'done'


for x in fib(10):
    print(x)

f = fib(10)
while True:
    try:
        x = next(f)
        print("fib:%s" % x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()

print(next(o))
print(next(o))
print(next(o))
