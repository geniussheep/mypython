#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# map
# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)
#
# from sys import argv, path  # 导入特定的成员
#
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
# print("\n")
# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))
# #<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
#
# class A:
#     pass
#
# class B(A):
#     pass
#
# isinstance(A(), A)  # returns True
# print(type(A()) == A)      # returns True
# isinstance(B(), A)    # returns True
# print(type(B()) == A)        # returns False
import json

import requests

monitor = "Benlai.Search.Service.ESB(681)有Topic消费延迟，具体见Lag数：<br>AppId: 681：<br>AppName: Benlai.Search.Service.ESB：<br><table border='1'><tr><td>Topic</td><td>Group</td><td>Lag</td></tr><tr><td>Benlai_Lhotse_Product_Update_SEO</td><td>Benlai_Lhotse_Product_Update_SEO_681</td><td>7573</td></tr></table>"

monitor.replace("<br>","\r\n").replace("<tr>","\r\n").replace("</tr>","\r\n").replace("<table>","").replace("</table>","").replace("<td>","\t").replace("</td>","\t")
print(monitor)

str = 'Runoob/'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[-1])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串
print('Ru\noob')
print(r'Ru\noob')

def get_mon_user():
    mon_receivers_api_url = 'http://10.234.151.196/api/v1/relation/receivers'
    r = requests.get(mon_receivers_api_url)
    if r.status_code == requests.codes.ok and r.json()['errcode'] != 0:
        receivers = r.json()['receivers']
    len(receivers)

get_mon_user()

