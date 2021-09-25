#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import json
import yaml
import hashlib


def load_json(json_file_path):
    """
    读取文件中的json数据
    :param json_file_path: json文件路径
    :return: 返回dict格式的数据
    """
    with open(json_file_path, encoding="utf-8") as f:
        data = json.load(f)  # 结果为dict格式
        return data


def load_yaml(yaml_file_path):
    """
    读取文件中的yaml数据
    :param yaml_file_path: yaml文件路径
    :return: 返回读取的数据 list或dict
    """
    with open(yaml_file_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data


def md5_generate(str_data):
    return hashlib.md5(str_data.encode()).hexdigest()


def sorted_dict_key(dict_data):
    """
    对字典的key由小到大的排序方式（虽然字典是无序存储的，但是计算MD5的时候，需要按照某种方式排序，目的是为了保持一致性）
    :param dict_data:待排序字典
    :return:返回排序后的字典
    """
    return dict(sorted(dict_data.items()))


if __name__ == '__main__':
    # file_path = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.json'
    # print(type(load_testcases(file_path)))
    # s = 'abc'
    # print(len(md5_generate(s)))
    # print(len('47f135c33e858f2e3f55156ae9f78ee1'))
    # s = {'b': 1, 'a': 2}
    # print(sorted_dict_key(s))
    file_path = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.yml'
    print(load_yaml(file_path))
    print(type(load_yaml(file_path)))

