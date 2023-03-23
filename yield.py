# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from contextlib import contextmanager

@contextmanager
def make_context():
    print('enter')
    try:
        yield 1
        print('I"m between two yield')
    except Exception:
        print("here is excepted")


with make_context() as value:
    print(value)
    raise Exception

#虽然make_context()是一个函数，但是由于它被contextmanager装饰了，所以现在with后面其实是一个上下文的类，而这个类的__enter__()函数的主体是make_context.next()，__exit__()的主要代码
#是make_context.next()。所以，当执行的时候，首先执行make_context.next()，输出“enter” 。然后执行到yield，这时这个函数就中断了，回过来执行with里body里的代码，由于我们接收了yield返回的值，
#所以输出“ 1  ”。然后我们抛出异常，with的body就执行完了。接着我们进入__exit__()函数，也就是再执行一次make_context.next()函数。这里就是最神奇的地方了，虽然这两段代码没有在一个函数体里，3
#但是__exit__()函数可以捕捉到with的body里的异常，所以我们进入了make_context函数的except里，并打印出“  here is excepted ”。

#with和yield配合在一起，确实省了不少事，这样，如果想处理同一类异常的时候，我们不用在每个函数里都加入多个try...catch块，而只需要在代码块前加一个with表达式即可。
# ---------------------
# 作者：Emma1985
# 来源：CSDN
# 原文：https://blog.csdn.net/u013213434/article/details/42554161
# 版权声明：本文为博主原创文章，转载请附上博文链接！



# yield返回值, 生成器

def gen():
    for x in ["a", "b", "c"]:
        yield x

for i in gen():
    print(i)



# yield接收值, 协程
def gen():
    while True:
        x = yield
        print("x = %s"% x)

g = gen()
next(g)  # 执行到yield， 激活协程 send(None) ”预激(prime)“协程
g.send(10)
g.send(20)
g.send(30)
g.close()


# 调用生成器

def gen():
    yield from ["x", "y", "z"]

for i in gen():
    print(i)

#yield实现异步


def consumer():
    r = ''
    while True:
        n = yield r
        print("[Consumer] n = %d" % n)
        if not n:
            return
        print("[Consumer] consuming %s..." % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    h = 0
    while h < 5:
        h = h + 1
        print("[Producer] producing %d..." % h)
        s = c.send(h)
        print("[Producer] consumer return: %s" % s)
    c.close()


c = consumer()  # 创建一个生成器
produce(c)  # 在该函数中，调用生成器的send()方法

#结合程序运行过程，可分析出：

#第一步：在produce(c)函数中，调用了c.send(None)启动了生成器，遇到yield暂停；接着执行produce()中接下来的代码，从运行结果看，
# 确实打印出了[Produce] producing 1 … 当程序运行至c.send(h)时，调用生成器并且通过yield传递了参数(h = 1)进入consumer()函数执行。

#第二步，yield传递参数（h=1）给consumer()函数中的n,并接着上一次暂停处往下继续执行，打印出[Consumer] n = 1，[Consumer] consuming 1… ；
# 在consumer()函数中此时 r 被赋值为’200 OK’,接着循环遇到yield， consumer()函数又暂停并且返回变量 r 的值，此时程序又进入produce(c)函数中接着执行。

#第三步，produce(c)函数接着第一步中c.send(h)处，继续往下执行打印出[Producer] consumer return: 200 OK，并进行循环，
# 打印[Producer] producing 2… 后，又调用c.send(h) 。。。如此循环回到第一步！