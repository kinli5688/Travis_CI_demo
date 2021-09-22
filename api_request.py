#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import requests
# r = requests.post('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '123456'})
# print(r.text)

resp = requests.get('http://127.0.0.1:5000/api/users')
print(resp.content)

# r = requests.put('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '654321'})
# print(r.text)