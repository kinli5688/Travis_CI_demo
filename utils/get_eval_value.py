#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

"""
用到了递归的概念，当参数是变量（例如：${gen_md5($TOKEN, $data, $random)}），或者为列表、字典等嵌套类型时，也可以实现正常的解析
"""


from utils import gendata


class GetData:
    def __init__(self):
        self.testcase_variables_mapping = {
            "TOKEN": "debugtalk",
            "random": "${gen_random_string(5)}",
            "data": '{"name": "user", "password": "123456"}'
        }

    def get_eval_value(self, data):
       """ evaluate data recursively, each variable in data will be evaluated.
       """
       if isinstance(data, (list, tuple)):
           return [self.get_eval_value(item) for item in data]

       if isinstance(data, dict):
           evaluated_data = {}
           for key, value in data.items():
               evaluated_data[key] = self.get_eval_value(value)

           return evaluated_data

       if isinstance(data, (int, float)):
           return data

       # data is in string format here
       data = "" if data is None else data.strip()
       # print('data:', data)
       if gendata.is_variable(data):
       # ？？？这一段暂时看不懂，后续再看：主要是针对 $var的处理，提取出变量var再继续进行处理
           # variable marker: $var
           variable_name = gendata.parse_variable(data)
           # print('variable_name:', variable_name, type(variable_name))
           value = self.testcase_variables_mapping.get(variable_name)
           # print('value:', value)
           if value is None:
               # raise exception.ParamsError(
               #     "%s is not defined in bind variables!" % variable_name)
               raise ("%s is not defined in bind variables!" % variable_name)
           # return value
           return self.get_eval_value(value)
       # 如果 data是用例规定格式的正则表达式 ${func(1, 2, a=3, b=4)}
       elif gendata.is_functon(data):
           # print('gendata.is_functon(data):', gendata.is_functon(data))
           # function marker: ${func(1, 2, a=3, b=4)}
           fuction_meta = gendata.parse_function(data)
           # print('fuction_meta:', fuction_meta)
           func_name = fuction_meta['func_name']
           args = fuction_meta.get('args', [])
           kwargs = fuction_meta.get('kwargs', {})
           args = self.get_eval_value(args)
           kwargs = self.get_eval_value(kwargs)
           # return self.testcase_config["functions"][func_name](*args, **kwargs)
           print('args123******:', args)
           return gendata.custom_functions_dict[func_name](*args, **kwargs)
       else:
           # print('hahaha')
           return data


if __name__ == '__main__':
    get_data = GetData()
    # print(get_data.get_eval_value(""))
    # print(get_data.get_eval_value("${gen_random_string(5)}"))
    # - TOKEN: debugtalk
    # - random: ${gen_random_string(5)}
    # - data: '{"name": "user", "password": "123456"}'
    # - authorization: ${gen_md5($TOKE, $data, $random)}
    # a = '${gen_md5("debugtalk", "{"name": "user", "password": "123456"}", ${gen_random_string(5)})}'
    a = '${gen_md5($TOKEN, $data, $random)}'
    # a = '${gen_md5($random)}'
    print(get_data.get_eval_value(a))

