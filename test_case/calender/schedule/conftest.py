# ***
# @autor CWZ
# ***
import pytest

from day04_reqursts.api.schedule import Schedule

schedule = Schedule()


@pytest.fixture(scope="session")
def update_1(token):
    smoke_list = [token, "cwz", "2021-10-29 00:00:00", "2021-10-30 00:00:00", "wufang", "创建我的日程一", "测试创建日程", "湘江五十"]
    schedule.create_schedule(*smoke_list)
