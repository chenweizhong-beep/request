# ***
# @autor CWZ
# ***
import allure
import pytest

from day04_reqursts.api.member import Member
from day04_reqursts.common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("通讯录人员的增删改查等接口测试")
class TestMember:
    member = Member()
    datas = member.yaml_load("data\\member.yaml")
    add_datas = datas['add']['data']
    add_ids = datas['add']['ids']

    update_datas = datas['update']['data']
    update_ids = datas['update']['ids']

    get_datas = datas['get']['data']
    get_ids = datas['get']['ids']

    delete_datas = datas['delete']['data']
    delete_ids = datas['delete']['ids']

    batch_delete_datas = datas['batch_delete']['data']
    batch_delete_ids = datas['batch_delete']['ids']

    depart_simple_datas = datas['depart_simple']['data']
    depart_simple_ids = datas['depart_simple']['ids']

    depart_explicit_datas = datas['depart_explicit']['data']
    depart_explicit_ids = datas['depart_explicit']['ids']

    active_status_datas = datas['active']['data']
    print(active_status_datas)
    active_status_ids = datas['active']['ids']

    invite_datas = datas['qr']['data']
    invite_ids = datas['qr']['ids']

    @allure.severity(allure.severity_level.CRITICAL)  # 等级严重
    @allure.story("增加联系人接口")
    @pytest.mark.parametrize("userid, name, mobile,errcode, errmsg, logname", add_datas, ids=add_ids)
    def test_creat_member(self, token, userid, name, mobile, errcode, errmsg, logname, create):
        log.info(f"{30 * '<<'}开始测试创建成员{30 * '>>'}")
        res = self.member.creat_member(token, userid, name, mobile)
        log.info(f"{30 * '<<'}创建成员测试结束{30 * '>>'}")
        assert res['errcode'] == errcode
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改联系人接口")
    @pytest.mark.parametrize("userid, name, mobile,errcode,errmsg,logname ", update_datas, ids=update_ids)
    def test_update_member(self, token, userid, name, mobile, errcode, errmsg, logname, update):
        log.info(f"{30 * '<<'}开始测试修改成员{30 * '>>'}")
        res = self.member.update_member(token, name, userid, mobile)
        log.info(f"{30 * '<<'}修改成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.NORMAL)  # 等级普通
    @allure.story("查询联系人接口")
    @pytest.mark.parametrize("userid, errcode, errmsg, logname", get_datas, ids=get_ids)
    def test_get_member(self, token, userid, errcode, errmsg, logname):
        log.info(f"{30 * '<<'}开始测试获取成员{30 * '>>'}")
        res = self.member.get_menmber(token, userid)
        log.info(f"{30 * '<<'}获取成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除联系人接口")
    @pytest.mark.parametrize("userid, errcode, errmsg, logname", delete_datas, ids=delete_ids)
    def test_delete_member(self, token, userid, errcode, errmsg, logname, delete):
        log.info(f"{30 * '<<'}开始测试删除成员{30 * '>>'}")
        res = self.member.delete_membera(token, userid)
        log.info(f"{30 * '<<'}删除成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("批量山删除联系人接口")
    @pytest.mark.parametrize("useridlist, errcode, errmsg", batch_delete_datas, ids=batch_delete_ids)
    def test_batch_delete_member(self, token, useridlist, errcode, errmsg, batch_delete):
        log.info(f"{30 * '<<'}开始测试批量删除成员{30 * '>>'}")
        res = self.member.batch_delete_member(token, useridlist)
        log.info(f"{30 * '<<'}批量删除成员测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("获取联系人简单信息接口")
    @pytest.mark.parametrize("department_id, fetch_child, errcode, errmsg,logname", depart_simple_datas,
                             ids=depart_simple_ids)
    def test_depart_simple(self, token, department_id, fetch_child, errcode, errmsg, logname):
        log.info(f"{30 * '<<'}开始测试获取联系人简单信息{30 * '>>'}")
        res = self.member.get_depart_simple(token, department_id, fetch_child)
        log.info(f"{30 * '<<'}获取联系人简单信息测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("获取联系人详细信息接口")
    @pytest.mark.parametrize("department_id, fetch_child, errcode, errmsg, logname", depart_explicit_datas,
                             ids=depart_explicit_ids)
    def test_depart_explicit(self, token, department_id, fetch_child, errcode, errmsg, logname):
        log.info(f"{30 * '<<'}开始测试获取联系人详细信息{30 * '>>'}")
        res = self.member.get_depart_simple(token, department_id, fetch_child)
        log.info(f"{30 * '<<'}获取联系人详细信息测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("查看企业微信活跃度")
    @pytest.mark.parametrize("data, errcode, errmsg, logname", active_status_datas, ids=active_status_ids)
    def test_active_status(self, token, data, errcode, errmsg, logname):
        log.info(f"{30 * '<<'}开始测试企业微信活跃度{30 * '>>'}")
        log.info(f"==================================================={self.active_status_datas}")
        res = self.member.get_active_status(token, data)
        log.info(f"{30 * '<<'}企业微信活跃度测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("获取加入成员二维码")
    @pytest.mark.parametrize("size_type, errcode, errmsg, logname", invite_datas, ids=invite_ids)
    def test_get_invite(self, token, size_type, errcode, errmsg, logname):
        log.info(f"{30 * '<<'}开始测试获取加入成员二维码{30 * '>>'}")
        res = self.member.get_invite_qr(token, size_type)
        log.info(f"{30 * '<<'}获取加入成员二维码测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']


