#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成列表
l = list(range(1, 11))
print("list(range(1,11)) %s" % l)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
l = []
for x in range(1, 11):
    l.append(x * x)

print("for(range(1,11)) %s" % l)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + "=" + v for k, v in d.items()])


panda_list={'1号':'100','2号':'86','3号':'130','4号':'140','5号':'52','6号':'99'}
overweight = [k for k, v in panda_list.items() if int(v) > 110 ]
print(overweight)