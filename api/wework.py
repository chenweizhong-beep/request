# ***
# @autor CWZ
# ***
from day04_reqursts.api.base_api import BaseApi
from day04_reqursts.common.config import cf


class WeWork(BaseApi):
    """
    获取token类
    """
    corpid = cf.get_value('wwork', 'corp_id')
    # print(corpid)
    corpsecret = cf.get_value('wwork', 'contact_secret')

    # print(corpsecret)
    def get_token(self, secret):
        """
        获取token方法
        :param secret: 凭证密钥
        :return: 返回token
        """
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={secret}",
            # "params": f"corpid = {self.corpid}&corpsecret = {self.corpsecret}"

        }
        res = self.send_api(data)
        token = res["access_token"]
        return token


if __name__ == '__main__':
    w = WeWork()
    print(w.get_token(secret=cf.get_value('wwork', 'contact_secret')))
