# ***
# @autor CWZ
# ***
import requests

if __name__ == '__main__':
    URl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    # 参数（corpid，corpsecret ）
    params = {
        "corpid": "wwe053b4cf05614835",
        "corpsecret": "dqi0vitUUuer-71ZVr6J765tn_KM0ehHfylwSanN-Qg",

    }
    # 发起方法请求，获取
    r = requests.request(method="get", url=URl, params=params)
    access_tocken = (r.json()['access_token'])
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_tocken}",
    data = {
        "userid": "tong",
        "name": "bbb"
    }

    res = requests.request(method='post', url=url, json=data)
    print(res)
