#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# api mock server

import json
from flask import Flask
from flask import request, make_response

app = Flask(__name__)
# users_dict = {}
users_dict = {2000: {'name': 'user1', 'password': '123456'}}


@app.route('/api/users/<int:uid>', methods=['POST'])
# 创建用户
def create_user(uid):
    user = request.get_json()  # 接收的数据是json格式
    # print('接收的请求JSON数据是：', user)
    # print('接收的uid数据是：', uid)
    if uid not in users_dict:
        result = {
            'success': True,
            'msg': "user created successfully."
        }
        status_code = 201
        users_dict[uid] = user
        # print('创建数据，非持久存储：', users_dict)
    else:
        result = {
            'success': False,
            'msg': "user already existed."
        }
        status_code = 500

    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/users/<int:uid>', methods=['PUT'])
# 更新用户
def update_user(uid):
    user = users_dict.get(uid, {})
    # print('修改的用户user为：', user)
    if user:
        user = request.get_json()
        # print('修改后的用户user为：', user)
        # 修改用户
        # users_dict[uid] = request.get_json()
        success = True
        status_code = 200
        # print('非持久数据：', users_dict)
    else:
        success = False
        status_code = 404

    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/users', methods=['GET'])
# 查询用户
def get_user():
    result = {
        'success': True,
        'data': users_dict
    }
    status_code = 200


    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response
