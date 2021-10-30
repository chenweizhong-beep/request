# ***
# @autor CWZ
# ***
import allure
import pytest

from api.calendar import Calender
from common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("日历增删改查等接口测试")
class TestCalender:
    calender = Calender()
    datas = calender.yaml_load("data\\calender.yaml")

    create_calender_data = datas['create_calender']['data']
    create_calender_ids = datas['create_calender']['ids']

    get_calender_data = datas['get_calender']['data']
    get_calender_ids = datas['get_calender']['ids']

    update_calender_data = datas['update_calender']['data']
    update_calender_ids = datas['update_calender']['ids']

    delete_calender_data = datas['delete_calender']['data']
    delete_calender_ids = datas['delete_calender']['ids']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("创建日历接口")
    @pytest.mark.parametrize(
        " organizer, readonly, set_as_default, summary, color, description,userid,userid1, errcode,errmsg",
        create_calender_data, ids=create_calender_ids)
    def test_create_calender(self, token, organizer, readonly, set_as_default, summary, color, description, userid,
                             userid1, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试创建日历{30 * '>>'}")
        res = self.calender.create_calender(token, organizer, readonly, set_as_default, summary, color, description,
                                            userid, userid1)
        log.info(f"{30 * '<<'}创建日历测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("查询日历接口")
    @pytest.mark.parametrize("errcode, errmsg,index", get_calender_data, ids=get_calender_ids)
    def test_get_calender(self, token, errcode, errmsg, index):
        log.info(f"{30 * '<<'}开始测试获取日历{30 * '>>'}")
        res = self.calender.get_calender(token, index)
        log.info(f"{30 * '<<'}获取日历测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改日历接口")
    @pytest.mark.parametrize("readonly,summary,color,description,userid,index,errcode,errmsg",
                             update_calender_data, ids=update_calender_ids)
    def test_update_calender(self, token, readonly, summary, color, description, userid, index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试修改日历{30 * '>>'}")
        res = self.calender.update_calender(token, readonly, summary, color, description, userid, index)
        log.info(f"{30 * '<<'}修改日历测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除日历接口")
    @pytest.mark.parametrize("index,errcode,errmsg", delete_calender_data, ids=delete_calender_ids)
    def test_delete_calender(self, token, index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试删除日历{30 * '>>'}")
        res = self.calender.delete_calender(token, index)
        log.info(f"{30 * '<<'}删除日历测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']
