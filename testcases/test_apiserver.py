#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import pytest
import requests
# from .base import ApiServerUnittest
import utils_demo
import api_request
import os


# 1- 没有使用数据驱动
class TestApiServer:
    def setup(self):
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        self.clear_users()

    def clear_users(self):
        pass


# 创建一个用户，该用户之前不存在
    def test_create_user_not_existed(self):
        # self.clear_users()

        url = "%s/api/users/%d" % (self.host, 1000)
        data = {
            "name": "user1",
            "password": "123456"
        }
        resp = self.api_client.post(url, json=data)
        print('resp:', resp.text)
        assert resp.status_code == 201
        assert resp.json()["success"] == True


# 2- 使用数据驱动 目前是单条数据
    def test_run_single_testcase_success(self):
       testcase_file_path = os.path.join(os.getcwd(), 'data/demo.json')
       testcases = utils_demo.load_json(testcase_file_path)  #  json数组
       # success, _ = self.test_runner.run_single_testcase(testcases[0])
       success, _ = api_request.run_single_testcase(testcases[0])
       # self.assertTrue(success)
       utils_demo.assertTrue(success)
       # assert success
