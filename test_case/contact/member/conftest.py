# ***
# @autor CWZ
# ***
import pytest

from day04_reqursts.api.member import Member

member = Member()


@pytest.fixture(scope="session")
def create(token):
    member.delete_membera(token, "tong")
    member.delete_membera(token, "tong5")


@pytest.fixture(scope="session")
def update(token):
    member.creat_member(token, "name", "edit", "15172222165")


@pytest.fixture(scope="session")
def delete(token):
    member.creat_member(token, "delete", "delete", "15894143301")


@pytest.fixture(scope="session")
def batch_delete(token):
    member.creat_member(token, "delete1", "delete1", "15310232145")
    member.creat_member(token, "delete2", "delete2", "15310232146")
    member.creat_member(token, "delete3", "delete3", "15310232147")


