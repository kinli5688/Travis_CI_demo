#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# import requests
# # r = requests.post('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '123456'})
# # print(r.text)
#
# resp = requests.get('http://127.0.0.1:5000/api/users')
# print(resp.content)
#
# # r = requests.put('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '654321'})
# # print(r.text)
import requests
import utils_demo


# 封装request请求公共方法
def run_single_testcase(testcase):
    req_kwargs = testcase['request']

    try:
        url = req_kwargs.pop('url')
        method = req_kwargs.pop('method')
    except KeyError as e:
        # raise Exception.ParamsError("Params Error")
        # print(e)
        # 抛出错误不会终止代码的运行
        raise Exception('******' + str(e) + '******')

    resp_obj = requests.request(url=url, method=method, **req_kwargs)
    diff_content = utils_demo.diff_response(resp_obj, testcase['response'])
    # print('diff_content:', diff_content)
    success = False if diff_content else True
    # print('success123:', success)
    return success, diff_content