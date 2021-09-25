#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import json
import hashlib


def load_json(testcase_file_path):
    with open(testcase_file_path, encoding="utf-8") as f:
        data = json.load(f)  # 结果为dict格式
        return data


# 将http请求返回结果resp_obj解析为与expected_resp_json相同的数据结构
def parse_response_object(resp_obj):
    try:
        resp_body = resp_obj.json()   # 获取json数据(dict格式) 返回结果是明文且是json格式的才可以
    except ValueError:
        resp_body = resp_obj.text

    return {
        'status_code': resp_obj.status_code,
        'headers': {'Content-Type': resp_obj.headers.get('Content-Type')},    # 由于header有时间戳，所以取一部分的数据
        'body': resp_body
    }


# 比较json函数
def diff_json(current_json, expected_json):
    json_diff = {}

    for key, expected_value in expected_json.items():
        value = current_json.get(key, None)
        if str(value) != str(expected_value):
            json_diff[key] = {
                'value': value,
                'expected': expected_value
            }

    return json_diff


def diff_response(resp_obj, expected_resp_json):
    # diff_content = {}
    resp_info = parse_response_object(resp_obj)
    diff_content = diff_json(resp_info, expected_resp_json)
    # 对比 status_code，将差异存入 diff_content
    # 对比 Headers，将差异存入 diff_content
    # 对比 Body，将差异存入 diff_content

    return diff_content


def diff_response1(resp_obj, expected_resp_json):
    if resp_obj.status_code == expected_resp_json.pop('status_code'):
        # print('status_code相同')
        if expected_resp_json.pop('headers')['Content-Type'] == resp_obj.headers['Content-Type']:
            # print('headers 相同')
            if resp_obj.json() == expected_resp_json.pop('body'):
                return
            else:
                return 'error3-body不相同'
        else:
            return 'error2-headers不相同'
    else:
        return 'error1-status_code不相同'


def assertTrue(assert_data):
    if assert_data:
        return True
    else:
        return False


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
    s = {'b': 1, 'a': 2}
    print(sorted_dict_key(s))

