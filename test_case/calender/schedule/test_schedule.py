# ***
# @autor CWZ
# ***
import allure
import pytest

from api.schedule import Schedule
from common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("日程增删改查等接口测试")
class TestSchedule:
    schedule = Schedule()
    datas = schedule.yaml_load("data\\schedule.yaml")

    create_schedule_data = datas['create_schedule']['data']
    create_schedule_ids = datas['create_schedule']['ids']

    get_all_schedule_data = datas['get_all_schedule']['data']
    get_all_schedule_ids = datas['get_all_schedule']['ids']

    update_schedule_data = datas['update_schedule']['data']
    update_schedule_ids = datas['update_schedule']['ids']

    delete_schedule_data = datas['delete_schedule']['data']
    delete_schedule_ids = datas['delete_schedule']['ids']

    get_schedule_data = datas['get_schedule']['data']
    get_schedule_ids = datas['get_schedule']['ids']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("创建日程接口")
    @pytest.mark.parametrize(
        "organizer, start_time, end_time, userid, summary, description, location, errcode, errmsg",
        create_schedule_data, ids=create_schedule_ids)
    def test_create_schedule(self, token, organizer, start_time, end_time, userid, summary, description, location, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试创建日程{30 * '>>'}")
        res = self.schedule.create_schedule(token, organizer, start_time, end_time, userid, summary, description,
                                            location)
        log.info(f"{30 * '<<'}创建日程测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获取日历下的日程列表接口")
    @pytest.mark.parametrize("index,offset,limit,errcode,errmsg", get_all_schedule_data, ids=get_all_schedule_ids)
    def test_get_all_schedule(self, token, index, offset, limit, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试获取日历下的日程列表{30 * '>>'}")
        res = self.schedule.get_all_schedule(token, index, offset, limit)
        log.info(f"{30 * '<<'}获取日历下的日程列表测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改日程接口")
    @pytest.mark.parametrize(
        "organizer,start_time, end_time, userid, summary, description, location,index, errcode, errmsg",
        update_schedule_data, ids=update_schedule_ids)
    def test_update_schedule(self, token, organizer, start_time, end_time, userid, summary, description, location,
                             index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试修改日程{30 * '>>'}")
        res = self.schedule.update_schedule(token, organizer, start_time, end_time, userid, summary, description,
                                            location, index)
        log.info(f"{30 * '<<'}修改日程测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除日程接口")
    @pytest.mark.parametrize("index,errcode,errmsg", delete_schedule_data, ids=delete_schedule_ids)
    def test_delete_schedule(self, token, index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试取消日程{30 * '>>'}")
        res = self.schedule.delete_schedule(token, index)
        log.info(f"{30 * '<<'}取消日程测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获取日程详细信息接口")
    @pytest.mark.parametrize("index,errcode,errmsg", get_schedule_data, ids=get_schedule_ids)
    def test_get_schedule(self, token, index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试获取日程详细信息{30 * '>>'}")
        res = self.schedule.get_schedule(token, index)
        log.info(f"{30 * '<<'}获取日程详细信息测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除日程接口")
    @pytest.mark.parametrize("index,errcode,errmsg", delete_schedule_data, ids=delete_schedule_ids)
    def test_delete_schedule(self, token, index, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试取消日程{30 * '>>'}")
        res = self.schedule.delete_schedule(token, index)
        log.info(f"{30 * '<<'}取消日程测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']
