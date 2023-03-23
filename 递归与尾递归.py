# # 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
#
# print(fact(100))
#
# # 栈会溢出
# print(fact(1000))


# 使用尾递归的方式保障栈不会溢出

def fact_iter(n, result):
    if n == 1:
        return result
    return fact_iter(n - 1, n * result)


def fact(n):
    return fact_iter(n, 1)

print(fact(5))

print(fact(100))

# 栈会溢出
print(fact(1000))