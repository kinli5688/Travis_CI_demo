#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# pytest 实现部分用例的前后置

import multiprocessing
import time
import unittest
import pytest
from apiserver import api_server

# sets up an HTTP server which can be used within the tests


@pytest.fixture(scope='class', autouse=True)
def api_server1():
    # 多进程启动api_server服务
    api_server_process = multiprocessing.Process(
        target=api_server.app.run
    )
    api_server_process.start()
    time.sleep(0.1)
    print('api_server服务已开启')
    yield
    api_server_process.terminate()
    print('api_server服务已关闭')