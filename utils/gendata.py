#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import hashlib
import random
import string
import importlib
import types
import re
import ast


function_regexp = re.compile(r"^\$\{(\w+)\(([\$\w =,]*)\)\}$")  # 正则表达式，匹配用例中的函数名及参数 ${func(a=1, b=2)}$ -> (func,(a=1,b=2))


def is_functon(content):
    """
    是否能够正则匹配
    :param content:"${gen_random_string(5)}"
    :return: 如果能测试匹配，返回TRUE 否则 FALSE
    """
    matched = function_regexp.match(content)
    return True if matched else False


def parse_string_value(str_value):
    """ parse string to number if possible
    e.g. "123" => 123
         "12.2" => 12.3
         "abc" => "abc"
         "$var" => "$var"
    """
    try:
        return ast.literal_eval(str_value)
    except ValueError:
        return str_value
    except SyntaxError:
        # e.g. $var, ${func}
        return str_value


# print(parse_string_value("qwee"), type(parse_string_value("qwee")))
# print(parse_string_value("12.31"), type(parse_string_value("12.31")))

# 处理参数
def parse_function(content):
    """
    将一个函数调用的字符串转换为函数的结构体
    :param content:  "${func(1, 2, a=3)}"
    :return: {'args': [1, 2], 'kwargs': {'a': 3}, 'func_name': 'func'}
    """
    function_meta = {
        "args": [],
        "kwargs": {}
    }
    matched = function_regexp.match(content)
    function_meta["func_name"] = matched.group(1)
    # print('function_meta:', function_meta)

    args_str = matched.group(2).replace(" ", "")
    # args_str = matched.group(2)
    # print('args_str:', args_str)
    if args_str == "":
        return function_meta
    #
    args_list = args_str.split(',')
    # print('args_list:', args_list)
    for arg in args_list:
        if '=' in arg:
            key, value = arg.split('=')
            function_meta["kwargs"][key] = parse_string_value(value)
        else:
            function_meta["args"].append(parse_string_value(arg))
    return function_meta

#
# # fun_1 = "${func(a=1, b=2)}"
# fun_1 = "${func(1, 2, a=3)}"
# # fun_1 = "${func()}"
#
# print(parse_function(fun_1))


def is_variable(var):
    """ Takes $var, returns True if it is a $var.
    先临时这样写
    """
    # name, item = tup
    # "$TOKEN".startswith()
    if var.startswith("$") and '{' not in var:
        return True
    # pass


def parse_variable(var):
    """
    取$var的值
    :param var:'$var'
    :return: 'var'
    """
    return var[1:]


def is_function(tup):
    """ Takes (name, object) tuple, returns True if it is a function.
    """
    name, item = tup
    return isinstance(item, types.FunctionType)
#
# module_name = 'custom_functions'
# imported = importlib.import_module(module_name)
# print(vars(imported))
# imported_functions_dict = dict(filter(is_function, vars(imported).items()))
# print('imported_functions_dict:', imported_functions_dict)

# ?？？ 目前只支持一个module   __update_context_config  这个方法目前还没看懂  后续需要继续看下
def import_module_functions(modules, level="testcase"):
    """ import modules and bind all functions within the context
    """
    for module_name in modules:
        imported = importlib.import_module(module_name)
        # print('*******:', vars(imported).items())
        imported_functions_dict = dict(filter(is_function, vars(imported).items()))
        # self.__update_context_config(level, "functions", imported_functions_dict)
    return imported_functions_dict


# print(import_module_functions(['custom_functions', 'load_data']))
# custom_functions_dict = import_module_functions(['custom_functions', 'load_data'])
custom_functions_dict = import_module_functions(['custom_functions'])
# print('custom_functions_dict:', custom_functions_dict)
# fun_1 = "${gen_random_string(5)}"
fun_1 = "${gen_md5($TOKEN, $data, $random)}"
function_meta = parse_function(fun_1)
# print("function_meta:", function_meta)
func_name = function_meta['func_name']
kwargs = function_meta['kwargs']
# print('func_name:', func_name)
args = function_meta['args']
# print('args:', args)

# print(custom_functions_dict[func_name](*args, **kwargs))


    # def gen_random_string(str_len):
    #     """
    #     生成指定长度的随机字符串(A-Fa-f0-9)
    #     :param str_len: 要生成的字符串长度
    #     :return: 长度为str_len的随机字符串
    #     """
    #     return ''.join(
    #         random.choice(string.ascii_letters + string.digits) for _ in range(str_len))

    # gen_random_string = lambda str_len: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))
    # gen_md5 = lambda *str_args: hashlib.md5(''.join(str_args).encode('utf-8')).hexdigest()


    # def gen_md5(*args):
    #     """
    #     获取可变参数的MD5值
    #     :param args:字符串格式
    #     :return:返回传入参数组合的MD5值
    #     """
    #     return hashlib.md5("".join(args).encode('utf-8')).hexdigest()

    # def import_requires(modules):
    #    """ import required modules dynamicly
    #    """
    #    for module_name in modules:
    #        globals()[module_name] = importlib.import_module(module_name)

class GenData:
    def import_module_functions(self, modules, level="testcase"):
       """ import modules and bind all functions within the context
       """
       for module_name in modules:
           imported = importlib.import_module(module_name)
           imported_functions_dict = dict(filter(is_function, vars(imported).items()))
           self.__update_context_config(level, "functions", imported_functions_dict)


# if __name__ == '__main__':
#     print(gen_random_string(5))  # => A2dEx
#
#     TOKEN = "debugtalk"
#     data = '{"name": "user", "password": "123456"}'
#     random = "A2dEx"
#     gen_md5(TOKEN, data, random)  # => a83de0ff8d2e896dbd8efb81ba14e17d
#     gen_md5(TOKEN)  # => a83de0ff8d2e896dbd8efb81ba14e17d
#     print(gen_md5(TOKEN, data, random), gen_md5(TOKEN))