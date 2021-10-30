# ***
# @autor CWZ
# ***
import pytest

from api.wework import WeWork
from common.config import cf


@pytest.fixture(scope="session")
def token():
    secret = cf.get_value("wwork", "schedule_secret")
    access_token = WeWork().get_token(secret=secret)
    return access_token
