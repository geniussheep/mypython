# encoding: UTF-8
import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())

### 输出 ###
# hello

m = re.match(r'(\w+) (\w+)(?P<sheep>.*)', 'hello world!')

print("m.string:", m.string)
print("m.re:", m.re)
print("m.pos:", m.pos)
print("m.endpos:", m.endpos)
print("m.lastindex:", m.lastindex)
print("m.lastgroup:", m.lastgroup)

print("m.group(1,2):", m.group(1, 2))
print("m.groups():", m.groups())
print("m.groupdict():", m.groupdict())
print("m.start(2):", m.start(2))
print("m.end(2):", m.end(2))
print("m.span(2):", m.span(2))
print(r"m.expand(r'\2 \1 + \3'):", m.expand(r'\2 \1 + \3'))

### output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!


"""
re.compile(strPattern[, flag]):

这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。 
第二个参数flag是匹配模式，取值可以使用按位或运算符’|’表示同时生效，
比如re.I | re.M。另外，你也可以在regex字符串中指定模式，比如re.compile(‘pattern’, re.I | re.M)与re.compile(‘(?im)pattern’)是等价的。
可选值有：

re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变’^’和’$’的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变’.’的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的：
"""

split_reg = re.compile('^GO$', re.I | re.M)

sql = '''
SELECT GETDATE()

GO

SELECT GETDATE()

GO

SELECT * FROM Address_GeoInfo 

GO

ALTER TABLE Address_GeoInfo add test_go INTEGER

GO

SELECT GETDATE()
'''
sql =sql.replace("\n", "\r\n")
split_sql_result = re.split(split_reg, sql, 0)



p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print("p.pattern:", p.pattern)
print("p.flags:", p.flags)
print("p.groups:", p.groups)
print("p.groupindex:", p.groupindex)

### output ###
# p.pattern: (\w+) (\w+)(?P<sign>.*)
# p.flags: 16
# p.groups: 3
# p.groupindex: {'sign': 3}


p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))

### output ###
# ['one', 'two', 'three', 'four', '']

print(p.findall('one1two2three3four4'))

### output ###
# ['1', '2', '3', '4']

p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print(m.group(),)

### output ###
# 1 2 3 4

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print(p.subn(r'\2 \1', s))


def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(p.subn(func, s))

### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)