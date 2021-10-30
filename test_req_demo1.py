# ***
# @autor CWZ
# ***
import datetime
import json
from string import Template

import pytest
import requests
import yaml


def tem_1(path, data, sub=None):
    with open(path, encoding="utf-8") as f:
        if sub is None:
            return yaml.safe_load(Template(f.read()).substitute(data))
        else:
            return yaml.safe_load(Template(yaml.safe_dump(yaml.safe_load(f)[sub])).substitute(data))


def send_api_data(path, p_data, sub):
    data: dict = tem_1(path, p_data, sub)
    print(data)
    for i in data['json'].values():
        if type(i) == datetime.date:
            # a = i.strftime('%Y-%m-%d') 将datetime.time类型转化为str类型
            data['json']['date'] = i.isoformat()
    print(data)
    print(type(data))
    res = requests.request(**data)
    return res.json()


with open("F:\\pythonProject2\\day04_reqursts\\time_1.yaml", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    active_datas = datas['active']['data']
    active_ids = datas['active']['ids']
    print(active_datas)
    print(type(active_datas))


class TestWeiXin:

    def setup(self):
        """
        前置条件，获取access_tocken
        """
        # 获取地址
        URl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 参数（corpid，corpsecret ）
        params = {
            "corpid": "wwe053b4cf05614835",
            "corpsecret": "dqi0vitUUuer-71ZVr6J765tn_KM0ehHfylwSanN-Qg",

        }
        # 发起方法请求，获取
        r = requests.request(method="get", url=URl, params=params)
        self.access_tocken = (r.json()['access_token'])

    def test_creat_department(self):
        '''
        创建部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_tocken}"
        # 创建部门信息
        data = {
            "name": "上海研究中心",
            "parentid": "1",
            # "order": ""，
        }
        r = requests.request(method='post', url=url, json=data, )
        print(r.json())
        assert r.json()['errmsg'] == 'created'

    def test_update_dapartment(self):
        '''
        修改部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_tocken}"
        # 修改部门信息
        data = {
            "id": "2",
            "name": "陈氏测试中心2",
            "name_en": "ceshi2",
        }
        r = requests.request(method='post', url=url, json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'updated'

    def test_select_department(self):
        '''
        查询部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_tocken}"
        r = requests.request(method="get", url=url)
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))

    def test_deleted_department(self):
        '''
        删除部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_tocken}&id=2"
        r = requests.request(method='get', url=url)
        print(r.json())
        assert r.json()["errmsg"] == 'deleted'

    def test_update_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_tocken}"
        data = {
            "userid": "tong",
            "name": None,
            # "department": [1, 3]
            # "mobile": "15172222165",
        }
        r = requests.request(method='post', url=url, json=data)
        print(r.json())

    @pytest.mark.parametrize("data, errcode, errmsg, logname", active_datas, ids=active_ids)
    def test_active_status(self, data, errcode, errmsg, logname):
        p_data = {"token": self.access_tocken, "data": data}
        res = send_api_data("F:\\pythonProject2\\day04_reqursts\\time_1_api.yaml", p_data, "active")
        print(res)
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    def test_a(self):
        data = {'json': 2021-10-17,
                'method': 'post',
                'params': 'access_token=FTsumt3j6txqKydN103S6fHcMRa4JADvDUohu_kLMIzcLDopz407TMV-D1f9Vj8GPd1NSgneHDGFv_tbyxxKusx6qmYWXogj2iseIpbpq7ukAMNCqnUjFhROLqMnRmDQBUwCzlam62jzXrWnMQG-I_aWRFCOy79g_Smh1ZTgTlXpV7HGYMvP2SzDoHepdMTb1pygm58991iWJdFT007M3w',
                'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat'

                }
        r = requests.request(**data)
        print(r.json())

