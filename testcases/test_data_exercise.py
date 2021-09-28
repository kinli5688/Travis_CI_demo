#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import pytest
import requests
# from .base import ApiServerUnittest
import utils
from utils import load_data
from utils import gendata
import api_request
import os

# 读取yaml测试数据
# 1-1 拼接测试数据路径
testcase_file_path = os.path.join(os.getcwd(), 'data/demo.yml')
# 1-2 读取测试原始数据
testcases = load_data.load_yaml(testcase_file_path)
print('testcases_requirements:', testcases[0]['test']["requires"])
# 1-3 导入当前测试用例所需要的库
# import string
gendata.import_requires(testcases[0]['test']["requires"])
# print(string.digits)
# print(globals())
print('testcases_request:', testcases[0]['test']["request"])


#
# def test_run_single_testcase_success(self):
#     api_request.run_single_testcase()
#     # success, _ = self.test_runner.run_single_testcase(testcases[0])
#     success, _ = api_request.run_single_testcase(testcases[0])
#     # self.assertTrue(success)
#     utils_demo.assertTrue(success)
#     # assert success