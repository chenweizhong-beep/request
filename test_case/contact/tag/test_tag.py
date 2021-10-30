# ***
# @autor CWZ
# ***

import allure
import pytest

from api.tag import Tag
from common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("标签增删改查等接口测试")
class TestTag:
    tag = Tag()
    datas = tag.yaml_load("data\\tag.yaml")
    create_data = datas['add']['data']
    create_ids = datas['add']['ids']

    update_data = datas['update']['data']
    update_ids = datas['update']['ids']

    delete_data = datas['delete']['data']
    delete_ids = datas['delete']['ids']

    get_all_data = datas['get_all']['data']
    get_all_ids = datas['get_all']['ids']

    create_tag_member_data = datas['create_tag_member']['data']
    create_tag_member_ids = datas['create_tag_member']['ids']

    delete_tag_member_data = datas['delete_tag_member']['data']
    delete_tag_member_ids = datas['delete_tag_member']['ids']

    get_tag_member_data = datas['get_tag_member']['data']
    get_tag_member_ids = datas['get_tag_member']['ids']

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("增加标签接口")
    @pytest.mark.parametrize("tagid, tagname,  errcode, errmsg,logname", create_data, ids=create_ids)
    def test_creat_tag(self, token, tagid, tagname, errcode, errmsg, logname, create_tag):
        log.info(f"{30 * '<<'}开始测试创建标签{30 * '>>'}")
        res = self.tag.creat_tag(token, tagid, tagname)
        log.info(f"{30 * '<<'}创建标签结束测试{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改标签接口")
    @pytest.mark.parametrize("tagid, tagname, errcode, errmsg, logname", update_data, ids=update_ids)
    def test_update_tag(self, token, tagid, tagname, logname, errcode, errmsg, update_tag):
        log.info(f"{30 * '<<'}开始测试修改标签{30 * '>>'}")
        res = self.tag.update_tag(token, tagid, tagname)
        log.info(f"{30 * '<<'}修改标签结束测试{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除标签接口")
    @pytest.mark.parametrize("tagid,errcode,errmsg", delete_data, ids=delete_ids)
    def test_delete_tag(self, token, tagid, errcode, errmsg, delete_tag):
        log.info(f"{30 * '<<'}开始测试删除标签{30 * '>>'}")
        res = self.tag.delete_tag(token, tagid)
        log.info(f"{30 * '<<'}删除标签结束测试{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    # @pytest.mark.skip
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("获取所有标签接口")
    @pytest.mark.parametrize("errcode, errmsg", get_all_data, ids=get_all_ids)
    def test_get_tag(self, token, errcode, errmsg, get_all_tag):
        log.info(f"{30 * '<<'}开始测试获取所有标签{30 * '>>'}")
        res = self.tag.get_all_tag(token)
        log.info(f"{30 * '<<'}获取所有标签结束测试{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("增加标签成员接口")
    @pytest.mark.parametrize("tagid, userlist, partylist, errcode, errmsg", create_tag_member_data,
                             ids=create_tag_member_ids)
    def test_create_tag_member(self, token, tagid, userlist, partylist, errcode, errmsg, create_tag_member):
        log.info(f"{30 * '<<'}开始测试增加标签成员{30 * '>>'}")
        res = self.tag.create_tag_member(token, tagid, userlist, partylist)
        log.info(f"{30 * '<<'}增加标签成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除标签成员接口")
    @pytest.mark.parametrize("tagid, userlist,partylist,errcode,errmsg", delete_tag_member_data,
                             ids=delete_tag_member_ids)
    def test_delete_tag_member(self, token, tagid, userlist, partylist, errcode, errmsg, delete_tag_member):
        log.info(f"{30 * '<<'}开始测试删除标签成员{30 * '>>'}")
        res = self.tag.delete_tag_member(token, tagid, userlist, partylist)
        log.info(f"{30 * '<<'}删除标签成员测试结束{30 * '>>'}")
        assert errcode == res["errcode"]
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("获取标签成员接口")
    @pytest.mark.parametrize("tagid,errcode,errmsg", get_tag_member_data, ids=get_tag_member_ids)
    def test_get_tag_member(self, token, tagid, errcode, errmsg, get_tag_member):
        log.info(f"{30 * '<<'}开始测试获取标签成员{30 * '>>'}")
        res = self.tag.get_tag_member(token, tagid)
        log.info(f"{30 * '<<'}获取标签成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']
