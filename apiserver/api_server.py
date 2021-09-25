#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
# api mock server

import json
from flask import Flask
from flask import request, make_response
import utils_demo

app = Flask(__name__)
users_dict = {}
# users_dict = {2000: {'name': 'user1', 'password': '123456'}}


# 约定token为：'abc123'
@app.route('/api/users/<int:uid>', methods=['POST'])
# 创建用户
def create_user(uid):
    header = request.headers
    user = request.get_json()  # 接收的数据是json格式
    # print('接收的headers数据是：', header.get('Random'), header.get('Authorization'))
    # print('接收的请求JSON数据是：', user)
    # print('接收的uid数据是：', uid)
    # Authorization字段是一个签名值，签名方式为TOKEN+RequestBody+Random拼接字符串的MD5值
    # 签名校验
    # TOKEN = 'abc123'
    token = 'abc123'
    authorization = utils_demo.md5_generate(token + str(user) + header.get('random'))
    print('authorization:', authorization)
    if authorization == header.get('authorization'):
        print('校验通过')
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
    else:
        print('校验不通过')
        result = {
            'success': False,
            'msg': "Authentication failed."
        }
        status_code = 201

    response = make_response(json.dumps(result), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/api/users/<int:uid>', methods=['PUT'])
# 更新用户
def update_user(uid):
    user = users_dict.get(uid, {})
    print('修改的用户user为：', user)
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


if __name__ == '__main__':
    import os
    os.system()
