# ***
# @autor CWZ
# ***
import datetime
import json
import os
import time
from string import Template

import requests
import yaml
from jsonpath import jsonpath

from day04_reqursts.common.config import cf
from day04_reqursts.common.log import log


class BaseApi:
    ip = cf.get_value('env', 'formal_ip')
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def send_api(self, req: dict):
        """
        封装requests请求
        :param req: 请求包体
        :return: 返回报文
        """
        """
        requests请求包体：
        "method" : "post",
        "url":"www.baidu.com",
        "param":"f'corpid={self.corpid}&corpsecret={secret}'"
        """
        return requests.request(**req).json()

    def get_time(self, date):
        """
        时间戳方法
        :param date:传入的时间
        :return:
        """
        # 将传入的格式化时间转化为时间元组
        time_strip1 = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        # 将时间元组转化为时间戳
        time_stamp1 = int(time.mktime(time_strip1))
        return time_stamp1

    def json_path(self, json, expr):
        """
        提取josn中的内容 方便断言
        :param json: 传入json格式的内容
        :param expr: 提取字符串的jsonpath表达式
        :return: 返回提取出来的字符串
        """
        return jsonpath(json, expr)

    def yaml_load(self, path, sub=None):
        """
        读取yaml文件中存储的数据方法
        :param path: yaml文件的相对路径的
        :param sub: 读取yml文件的二级数据目录，默认为None
        :return: 返回yaml中的内容
        """
        path = os.path.join(self.BASE_PATH, path)
        # print(path)
        '''
        读取yaml数据
        '''
        with open(path, encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    def template_1(self, path, data, sub=None):
        """
        模板技术，替换文件中的变量
        :param path: 输入yaml文件的相对路径
        :param data: 需要更改的数据
        :param sub:  yaml是否有二级目录
        :return:
        """
        with open(path, encoding="utf-8") as f:
            if sub is None:
                # a = f.read(f)
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                '''
                由于Template需要替换全部的变量，有漏的就会报错，先写Template(f.read()).substitute(data)
                就会报错，data只对sub下一层的数据改，并没有改其他层的数据，肯定会报错
                需要先yaml.safe_load(f)[sub]提取到下一层的数据，但由于是dict
                要通过yaml.dump转化成yml格式，经的字符串过Template来改变变量，最后在yaml.safe_load转化成dict
                '''
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))

    def json_dumps(self, res):
        """
        格式化json格式内容
        :param res: json格式内容
        :return:
        """
        return json.dumps(res, ensure_ascii=False, indent=2)
        # return json.dumps(res, cls=DateEncoder)

    def send_api_data(self, path, p_data, sub, js_on=None, da_te=None):
        """
        进一步封装请求，解决请求中非必输的字段输入为空
        :param path: yaml文件的相对路径
        :param p_data: 需要替换的数据
        :param sub: 针对yaml第二个层级进行替换数据
        :return: 返回相应的报文
        """
        path = os.path.join(self.BASE_PATH, path)
        data: dict = self.template_1(path, p_data, sub)
        try:
            '''
            循环文件中[json]中的键值，如果键值的类型为datetime.date就转换为str类型
            '''
            for i in data[js_on].values():
                if type(i) == datetime.date:
                    # 将日期的类型从datetime.date转化为str类型
                    data[js_on][da_te] = i.isoformat()
        except:
            pass
        # log.info(f"**********api变化的模板参数是:\n{self.json_dumps(p_data)}")
        try:
            '''
            循环文件[json]中的键值，如果键值为空，就默认为空
            '''
            for i in data["json"].keys():
                if data["json"][i] == 'None':
                    data["json"][i] = None
        except:
            pass
        log.info(
            f"{60 * '='}请求修改后的数据{60 * '='}：\n{self.json_dumps(data)}")
        res = self.send_api(data)
        log.info(
            f"{60 * '='}返回的数据为{60 * '='}：\n{self.json_dumps(res)}")
        return res


if __name__ == '__main__':
    # b = BaseApi()
    # print(b.BASE_PATH)
    # path = os.path.join(b.BASE_PATH, "data\\department_api.yaml")
    # data = {"token": "555", "name": "cwz", "parentid": 1}
    # c = b.template_1(path, data, "add")
    # print(json.dumps(c, ensure_ascii=False, indent=2))

    # print(b.yaml_load("data\contact.yaml")["sub"])
    time_strip = time.strptime('2020-10-01 00:00:00', "%Y-%m-%d %H:%M:%S")
    # print(type(time_strip))
    # print(time_strip)
    time_stamp = (time.mktime(time_strip))
    print(time_stamp)
    print(type(time_stamp))
    #  获取当前时间
    now = datetime.datetime.now()
    # 通过strftime方法格式化获取的当前时间
    now_1 = now.strftime('%Y-%m-%d')
    print(now_1)
    print(type(now_1))
    t = datetime.datetime.strptime(str(now_1), "%Y-%m-%d")
    print(t)
    print(type(t))
