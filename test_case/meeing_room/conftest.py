# ***
# @autor CWZ
# ***
import pytest

from day04_reqursts.api.wework import WeWork
from day04_reqursts.common.config import cf


@pytest.fixture(scope="session")
def token():
    secret = cf.get_value('wwork', 'meeting_room_secret')
    access_token = WeWork().get_token(secret)
    return access_token
