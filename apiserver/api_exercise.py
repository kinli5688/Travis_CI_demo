# #!/usr/local/bin/python3
# # -*- coding:utf-8 -*-
#
#
import importlib
# import random

import requests
from utils import load_data

# testcase_file_path1 = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.json'
# data1 = load_data.load_json(testcase_file_path1)
# print('data:', load_data.load_json(testcase_file_path1)[0]['request'])

# testcase_file_path = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.yml'
# data = load_data.load_yaml(testcase_file_path)
# print('data:', data[0]['request'])
# print('data:', type(data[0]['request']))
# url = data['request'].get('url')
# method = data['request'].get('method')
# headers = data['request'].get('headers')
# json1 = data['request'].get('json')

#
# if __name__ == '__main__':
#     # r = requests.post('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '123456'})
#     r = requests.request(**data1[0]['request'])
#     # r = requests.request(**data[0]['request'], json=data[0]['data'])
#     # r = requests.request(**data[0]['request'], json=data[0]['data'])
#     # r = requests.request(**data[0]['request'], proxies={'http': '127.0.0.1:8888'})
#     print(r.text)
#     #
#     # # resp = requests.get('http://127.0.0.1:5000/api/users')
#     # # print(resp.content)
#     #
#     # # r = requests.put('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '654321'})
#     # # print(r.text)
#     # Authorization字段是一个签名值，签名方式为TOKEN+RequestBody+Random拼接字符串的MD5值
#     # TOKEN = 'abc123'
#     # RequestBody = data[0]['request'].get('json')
#     # Random = 'A2dEx'
#     # s = TOKEN + str(RequestBody) + Random
#     # print(s)
#     # print(utils.md5_generate(s))


# print(map(lambda x: x + 1, [1, 2, 3]))
# print(list(map(lambda x: x + 1, [1, 2, 3])))
# for i in map(lambda x: x + 1, [1, 2, 3]):
#     print(i)


# print(map(None, [1, 2, 3, 4], [5, 6, 7, 8]))

# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     print('it:', it)
#     if initializer is None:
#         try:
#             initializer = next(it)
#             print('initializer:', initializer)
#         except StopIteration:
#             # 传入为空列表时，可出现此报错
#             raise TypeError('reduce() of empty sequence with no initial value')
#     accum_value = initializer
#     for x in it:
#         # print('x:', x)
#         # print('accum_value:', accum_value)
#         accum_value = function(accum_value, x)
#     return accum_value
#
#
# plus = lambda x, y: x + y
# # reduce(plus, [])
# print(reduce(plus, [1, 2, 3, 4, 5]))
# print(reduce(plus, [1, 2, 3, 4, 5], 10))


# mode2 = lambda x: x % 2
# print(list(filter(mode2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# 函数式编程  替换条件控制语句
# pr = lambda s: s
# print_num = lambda x: (x == 1 and pr("one")) or (x == 2 and pr("two")) or (pr("other"))
# print(print_num(1))
# print(print_num(2))
# print(print_num(3))


# 替换循环控制语句 - 替换for循环
# # python3
# square = lambda x, y : x * y
# # for x, y in [(1, 5), (2,6), 3, 4, 5], [5, 6, 7, 8, 9]):
# # 使用for 循环实现
# print('以上使用for循环实现：')
# for x, y in [(1, 5), (2, 6)]:
#     print(square(x, y))
#
# # 使用map实现
# print('以上使用map循环实现：')
# print(list(map(square, [1, 2], [5, 6])))
# for i in map(square, [1, 2], [5, 6]):
#     print(i)

# 替换循环控制语句 - 替换while循环
# 递归学习 https://www.jianshu.com/p/6870e23b8ebe
# 例子1：实现一个递归函数：计算n!=1*2*3*4*------*n
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# print(fact(4))

# 例子2：实现一个递归函数：对传入的dict进行key去重操作，将结果放到传入的set对象中
# def dict_to_set(dict_ob, set_ob):
#     for key, value in dict_ob.items():
#         set_ob.add(key)
#         if isinstance(value, dict):
#             dict_to_set(value, set_ob)
#         elif isinstance(value, list):
#             for li in value:
#                 dict_to_set(li, set_ob)
#     return set_ob


# if __name__ == "__main__":
#     dict01 = {"name": "ting", "pass": "123", "family": [{"name": "tian", "age": 1}, {"name": "zhou", "age": 26}]}
#     # dict01 = {"name": "ting", "pass": "123", "test": {"name": 'haha', 'b': 2}}
#     my_set = set()
#     print(dict_to_set(dict01, my_set))  # 结果：{'name', 'pass', 'family', 'age'}


# 例子3：这是一个错误的递归，正确的方法参考例子2
# def dict_to_set(dict_ob,set_ob):
#     for key, value in dict_ob.items():
#         set_ob.add(key)
#         if isinstance(value, dict):
#             return dict_to_set(value, set_ob)
#         elif isinstance(value, list):
#             for li in value:
#                 return dict_to_set(li, set_ob)
#     return set_ob
#
#
# if __name__ == "__main__":
#     # 结果：异常
#     dict01 = {"name": "ting",
#               "pass": "123",
#               "family": [{"name": "tian", "age": 1}, {"name": "zhou", "age": 26}],
#               "friend": [{"name": "yaya", "age": 21}, {"name": "ayu", "age": 12}]
#               }
#     my_set = set()
#     print(dict_to_set(dict01, my_set))

# imperative version of "echo()"
# def echo_IMP():
#     while 1:
#         x = input("IMP -- ")
#         print(x)
#         if x == 'quit':
#             break
#
#
# echo_IMP()


# def monadic_print(x):
#     print(x)
#     return x
#
# # FP version of "echo()"
# echo_FP = lambda : monadic_print(input("FP -- "))=='quit' or echo_FP()
# echo_FP()



from functools import reduce

# def fun_filter(x):
#     return x+1

# def add(x, y):
#     return x+y

# print(reduce(add, [1, 2, 3, 4, 5]), 10)

# print(list(filter(fun_filter, [1,2,3,4,5,6])))

# print(list(map(add, [1, 2, 3], [6, 8])))


# 笛卡尔积
# bigmuls = lambda xs, ys: filter(lambda x, y:x*y > 25, combine(xs,ys))
# combine = lambda xs, ys: map(None, xs*len(ys), dupelms(ys, len(xs)))
# dupelms = lambda lst, n: reduce(lambda s, t: s+t, map(lambda l, n=n: [l]*n, lst))  # [1,2,3],n=2 -> [1,1,2,2,3,3]

# print(bigmuls([1, 2, 3, 4], [10, 15, 3, 22]))  # [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]
# print(list(bigmuls([1, 2, 3, 4], [10, 15, 3, 22]))) # [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]

# print(list(map(lambda l, n=3: [l] * n, [1, 2, 3])))
# for i in map(lambda l, n: [l] * n, [1, 2, 3], [4, 5, 6]):
#     print(i)

# print(reduce(lambda s, t: s + t, map(lambda l, n: [l] * n, [1, 2, 3], [4, 5, 6])))
# print(reduce(lambda s, t: s + t, [1,2,3]))
# dupelms = lambda lst, n: reduce(lambda s, t: s+t, map(lambda l, n=n: [l]*n, lst))   # [1,2,3],n=2 -> [1,1,2,2,3,3]
# # lst = [1, 2, 3]
# # print(dupelms(lst, 3))
# xs = [1, 2, 3]
# ys = [10, 15, 3, 22]
# print(list(map(lambda x: x, xs*len(ys))))  # 函数是None时，Python2中，直接原样输出后续结果   Python3中  结果是NoneType
# print(list(dupelms(ys, len(xs))))
# combine = lambda xs, ys: map(lambda x: x, xs*len(ys), dupelms(ys, len(xs)))
# combine = lambda xs, ys: map(lambda x, y: (x, y), xs*len(ys), dupelms(ys, len(xs)))
# combine = lambda xs, ys: map(None, xs*len(ys), dupelms(ys, len(xs)))

# print(list(combine(xs, ys)))
# for i in combine(xs, ys):
#     print(i)
# print(list(map(lambda x, y: (x, y), [1, 2, 3], [5, 6])))

# print(list(filter(lambda x, y: (x * y > 25), list(combine(xs, ys)))))
# print(list(filter(lambda x: (x[0] * x[1] > 25), [(6, 5), (2, 5), (3, 5), (6, 6), (2, 6), (3, 6)])))

# bigmuls = lambda xs, ys: filter(lambda x: x[0] * x[1] > 25, combine(xs, ys))
# print(list(bigmuls(xs, ys)))
# print(list(bigmuls([1, 2, 3, 4], [10, 15, 3, 22]))) # [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]


# python3
# 步骤1：dupelms，将 ys,len(xs) -> ys的每个元素扩充为len(xs)个元素 即 [10.15.3.22],len([1,2,3,4])=4 -> [10,10,10,10,15,15,15,15,3,3,3,3,22,22,22,22]
dupelms = lambda lst, n: reduce(lambda s, t: s+t, map(lambda l, n=n: [l]*n, lst))

# 步骤2：combine， 计算笛卡尔积 使用map函数，将两个列表组合为元组列表
# 即：[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]与[10,10,10,10,15,15,15,15,3,3,3,3,22,22,22,22] ->
# （1，10）（2，10）（3，10）（4，10）
# （1，15）（2，15）（3，15）（4，15）
# （1，3）（2，3）（3，3）（4，3）
# （1，22）（2，22）（3，22）（4，22）
# combine = lambda xs, ys: map(lambda x, y: (x, y), xs*len(ys), dupelms(ys, len(xs)))
combine = lambda xs, ys: zip(xs*len(ys), dupelms(ys, len(xs)))

# 步骤3：bigmuls,利用filter进行过滤，得到笛卡尔积大于25的结果 ->
# [(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]
bigmuls = lambda xs, ys: filter(lambda x: x[0] * x[1] > 25, combine(xs, ys))
print(list(bigmuls([1, 2, 3, 4], [10, 15, 3, 22])))





# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @file   : Cartesian.py
# @author : shlian
# @date   : 2018/5/29
# @version: 1.0
# @desc   : 用python实现求笛卡尔积
# import itertools
#
#
# class cartesian(object):
#     def __init__(self):
#         self._data_list = []
#
#     def add_data(self, data=[]):  # 添加生成笛卡尔积的数据列表
#         self._data_list.append(data)
#
#     def build(self):  # 计算笛卡尔积
#         for item in itertools.product(*self._data_list):
#             print(item)
#
#
# if __name__ == "__main__":
#     car = cartesian()
#     car.add_data([1, 2, 3, 4])
#     car.add_data([5, 6, 7, 8])
#     car.add_data([9, 10, 11, 12])
#     car.build()


#
# # eval
# import random
# module_name = 'random'
# importlib.import_module(module_name)
# print(random.choice('asdff'))
# import string
# gen_random_string = "lambda str_len: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))"
#
# func = eval(gen_random_string)
# func = eval("lambda str_len: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))")
#
# func # => <function <lambda> at 0x10e19a398>
# print(func(5))
