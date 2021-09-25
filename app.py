#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import pytest


if __name__ == '__main__':
    # pytest.main(['testcases/test_apiserver.py::TestApiServer::test_run_single_testcase_success', '-vs'])
    pytest.main(['testcases/test_apiserver.py', '-vs'])