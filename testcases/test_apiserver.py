#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import pytest
import requests
# from .base import ApiServerUnittest


class TestApiServer():
    def setup(self):
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        # self.clear_users()

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


if __name__ == '__main__':
    pytest.main(['test_apiserver.py', '-vs'])