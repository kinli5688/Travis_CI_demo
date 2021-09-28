#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


import hashlib
import random
import string
import importlib


def gen_random_string(str_len):
    """
    生成指定长度的随机字符串(A-Fa-f0-9)
    :param str_len: 要生成的字符串长度
    :return: 长度为str_len的随机字符串
    """
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))

# gen_random_string = lambda str_len: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))
# gen_md5 = lambda *str_args: hashlib.md5(''.join(str_args).encode('utf-8')).hexdigest()


def gen_md5(*args):
    """
    获取可变参数的MD5值
    :param args:字符串格式
    :return:返回传入参数组合的MD5值
    """
    print('args:', args)
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


def import_requires(modules):
   """ import required modules dynamicly
   """
   for module_name in modules:
       globals()[module_name] = importlib.import_module(module_name)




if __name__ == '__main__':
    print(gen_random_string(5))  # => A2dEx

    TOKEN = "debugtalk"
    data = '{"name": "user", "password": "123456"}'
    random = "Xtisc"
    # gen_md5(TOKEN, data, random)  # => a83de0ff8d2e896dbd8efb81ba14e17d
    # gen_md5(TOKEN)  # => a83de0ff8d2e896dbd8efb81ba14e17d
    # print(gen_md5(TOKEN, data, random), gen_md5(TOKEN))
    print(gen_md5(TOKEN, data, random))
