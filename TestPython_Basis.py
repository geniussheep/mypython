#!/usr/bin/env python3
# 使py Linux直接运行
# print(lambda m,n:m*n,range(1,10));
#
#
# # imperative version of "echo()"
# def echo_IMP():
#     while 1:
#         x = input("IMP -- ")
#         if x == 'quit':
#             break
#         else:
#             print(x)
#
#
# echo_IMP()
#
#
# # utility function for "identity with side-effect"
# def monadic_print(x):
#     print(x)
#     return x
#
#
# # FP version of "echo()"
# echo_FP = lambda: monadic_print(input("FP -- ")) == 'quit' or echo_FP()
# echo_FP()
#

bigmuls = lambda xs, ys: filter(lambda x, y: x * y > 25, combine(xs, ys))
combine = lambda xs, ys: map(None, xs * len(ys), dupelms(ys, len(xs)))
dupelms = lambda lst, n: reduce(lambda s, t: s + t, map(lambda l, n=n: [l] * n, lst))
print(bigmuls((1, 2, 3, 4), (10, 15, 3, 22)))
# -*- coding: utf-8 -*-
# 指定保存为UTF-8编码



print("你好，世界")
print("hello word")

name = input("请输入字符串：")
print("我输入的字符串", name)

a = -10e9
if a > 0:
    print(a)
elif a == 0:
    print(0)
else:
    print(-a)
print('i am ok')
print("i'm \"ok\"")
print(r"i'm \"ok\"")
print('''line1"
      line2

      line3''')

print(True and False)

print(True or False)

print(5 > 1 and 1 == 0)

print(5 > 1 or 1 == 2)

print(not True)

print(not 5 > 1 and 1 == 0)
print(not (5 > 1 and 1 == 0))

a = "abc"
b = a
a = "xyz"
print(b)
print(a)

a = 10 / 3
print("10/3=", a)
a = 9 / 3
print("9/3=", a)
a = 10 // 3
print("10//3=", a)
a = 11 / 3
print("11/3=", a)
a = 11 // 3
print("11//3=", a)

a = 11 % 3
print("11 % 3 =", a)
a = 'hello,world'
print(a)
a = 'hello,\'Adam\''
print(a)
a = r'hello,\"bart"'
print(a)
a = r'''hello,
lisa!'''
print(a)
a = ord("A")
print(a)
a = ord("中")
print(a)
a = chr(65)
print(a)
a = chr(25991)
print(a)

a = '\u4e2d\u6587'
print(a)

# bytes
a = b'abc'
print(a)
a = "abc".encode('ascii')
print(a)
a = "中午".encode("utf-8")
print(a)
a = b'\xe4\xb8\xad\xe5\x8d\x88'.decode("utf-8")
print(a)
a = b'aBc'.decode('utf-8')
print(a)
a = b'aBc'.decode('ascii')
print(a)

a = len("abc")
print(a)
a = len("中午")
print(a)

a = len(b'Abc')
print(a)

a = len(b"\xe4\xb8\xad\xe5\x8d\x88")
print(a)

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

a = 'hello ,%s ' % "world"
print(a)

a = "hi, %s, you have $%d" % ('sheep', 5000)
print(a)

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

a = "%2d-%#3d" % (3, 1)
print(a)
a = "%2d-%03d" % (3, 1)
print(a)
a = "%2d-%.4d" % (3, 1)
print(a)

a = "%.2f-%.3f" % (3.14159999444, 1.214578963)
print(a)
a = "%.2f-%f" % (3.14159999444, 1.214578963)
print(a)
a = "%.2f-%04f" % (3.14159999444, 1.214578963)
print(a)

a = "age :%s, Gender: %s" % (25, True)
print(a)

a = "growth rate :%d%%" % 25
print(a)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
