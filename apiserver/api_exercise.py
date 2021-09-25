# #!/usr/local/bin/python3
# # -*- coding:utf-8 -*-
#
#
import requests
from utils import load_data

testcase_file_path1 = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.json'
data1 = load_data.load_json(testcase_file_path1)
print('data:', load_data.load_json(testcase_file_path1)[0]['request'])

# testcase_file_path = '/Users/kingli/PycharmProjects/Travis_CI_demo/data/demo.yml'
# data = load_data.load_yaml(testcase_file_path)
# print('data:', data[0]['request'])
# print('data:', type(data[0]['request']))
# url = data['request'].get('url')
# method = data['request'].get('method')
# headers = data['request'].get('headers')
# json1 = data['request'].get('json')


if __name__ == '__main__':
    # r = requests.post('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '123456'})
    r = requests.request(**data1[0]['request'])
    # r = requests.request(**data[0]['request'], json=data[0]['data'])
    # r = requests.request(**data[0]['request'], json=data[0]['data'])
    # r = requests.request(**data[0]['request'], proxies={'http': '127.0.0.1:8888'})
    print(r.text)
    #
    # # resp = requests.get('http://127.0.0.1:5000/api/users')
    # # print(resp.content)
    #
    # # r = requests.put('http://127.0.0.1:5000/api/users/1000', json={'name': 'user1', 'password': '654321'})
    # # print(r.text)
    # Authorization字段是一个签名值，签名方式为TOKEN+RequestBody+Random拼接字符串的MD5值
    # TOKEN = 'abc123'
    # RequestBody = data[0]['request'].get('json')
    # Random = 'A2dEx'
    # s = TOKEN + str(RequestBody) + Random
    # print(s)
    # print(utils.md5_generate(s))
