# ***
# @autor CWZ
# ***
import allure
import pytest

from api.meeting_room import MeetingRoom
from common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("会议室增删改查等接口")
class TestMeetingRoom:
    room = MeetingRoom()
    datas = room.yaml_load("data\\meeting_room.yaml")

    create_room_data = datas['create_room']['data']
    create_room_ids = datas['create_room']['ids']

    get_room_data = datas['get_room']['data']
    get_room_ids = datas['get_room']['ids']

    update_room_data = datas['update_room']['data']
    update_room_ids = datas['update_room']['ids']

    delete_room_data = datas['delete_room']['data']
    delete_room_ids = datas['delete_room']['ids']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("创建会议室接口")
    @pytest.mark.parametrize("name, capacity, city, building, floor, equipment, errcode, errmsg", create_room_data,
                             ids=create_room_ids)
    def test_create_meeting_room(self, token, name, capacity, city, building, floor, equipment, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试创建会议室{30 * '>>'}")
        res = self.room.create_meeting_room(token, name, capacity, city, building, floor, equipment)
        log.info(f"{30 * '<<'}创建会议室测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获取会议室接口")
    @pytest.mark.parametrize("city, building, floor, equipment, errcode, errmsg", get_room_data, ids=get_room_ids)
    def test_get_meeting_room(self, token, city, building, floor, equipment, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试获取会议室{30 * '>>'}")
        res = self.room.get_meeting_room(token, city, building, floor, equipment)
        log.info(f"{30 * '<<'}获取会议室测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改会议室接口")
    @pytest.mark.parametrize("meetingroom_id, name, capacity, city, building, floor, equipment, errcode,errmsg",
                             update_room_data, ids=update_room_ids)
    def test_update_meeting_room(self, token, meetingroom_id, name, capacity, city, building, floor, equipment, errcode,
                                 errmsg):
        log.info(f"{30 * '<<'}开始测试修改会议室{30 * '>>'}")
        res = self.room.update_meeting_room(token, meetingroom_id, name, capacity, city, building, floor, equipment)
        log.info(f"{30 * '<<'}修改会议室测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除会议室接口")
    @pytest.mark.parametrize("meetingroom_id,errcode,errmsg", delete_room_data, ids=delete_room_ids)
    def test_delete_meeting_room(self, token, meetingroom_id, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试删除会议室{30 * '>>'}")
        res = self.room.delete_meeting_room(token, meetingroom_id)
        log.info(f"{30 * '<<'}删除会议室测试结束{30 * '>>'}")
        assert errcode == res['errcode']
        assert errmsg in res['errmsg']
