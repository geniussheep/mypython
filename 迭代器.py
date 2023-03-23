#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abd', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
print()
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abd', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(range(10), Iterator))
print()
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('abd'), Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(iter(range(10)), Iterator))
