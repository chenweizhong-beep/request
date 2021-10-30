# ***
# @autor CWZ
# ***
import pytest

from day04_reqursts.api.member import Member
from day04_reqursts.api.tag import Tag
from day04_reqursts.common.log import log

tag = Tag()
member = Member()


def qian_zhi(token):
    res = tag.get_all_tag(token)
    '''
    获取所有标签的id,存在标签id，就删除该标签
    '''
    for i in res['taglist']:
        tagid = i['tagid']
        if tagid is not None:
            tag.delete_tag(token, tagid)


@pytest.fixture(scope="session")
# @pytest.fixture(scope='class')
def create_tag(token):
    log.info("************************开始创建成员的前置条件*****************************************")
    qian_zhi(token)
    tag.creat_tag(token, 6, 'create1')


@pytest.fixture(scope="session")
# @pytest.fixture(scope='class')
def update_tag(token):
    log.info("************************开始修改成员的前置条件*****************************************")
    qian_zhi(token)
    tag.creat_tag(token, 1, "uuu1")
    tag.creat_tag(token, 2, "uuu2")
    tag.creat_tag(token, 3, "uuu3")


@pytest.fixture(scope="session")
# @pytest.fixture()
def delete_tag(token):
    log.info("************************开始删除成员的前置条件*****************************************")
    qian_zhi(token)
    tag.creat_tag(token, 1, "add1")


@pytest.fixture(scope="session")
# @pytest.fixture()
def get_all_tag(token):
    log.info("************************开始获取成员的前置条件*****************************************")
    tag.creat_tag(token, 1, "add1")
    tag.creat_tag(token, 2, "add2")
    tag.creat_tag(token, 3, "add3")
    yield
    log.info("************************开始获取成员的后置条件*****************************************")
    qian_zhi(token)
    log.info("************************开始获取成员的后置条件结束*****************************************")


@pytest.fixture(scope="session")
def create_tag_member(token):
    log.info("************************开始增加标签成员的前置条件*****************************************")
    member.creat_member(token, "sign1", 'sign1', '15894143201')
    member.creat_member(token, "sign2", 'sign2', '15894143202')
    member.creat_member(token, "sign3", 'sign3', '15894143203')
    member.creat_member(token, "sign4", 'sign4', '15894143204')
    tag.creat_tag(token, 1, "add1")


@pytest.fixture(scope="session")
def delete_tag_member(token):
    log.info("************************开始删除标签成员的前置条件*****************************************")
    tag.create_tag_member(token, 1, ['sign1', 'sign2', 'sign3', 'sign4'], [])


@pytest.fixture(scope="session")
def get_tag_member(token):
    log.info("************************开始获取标签成员的前置条件*****************************************")
    tag.creat_tag(token, 2, "partydepart1")
    tag.create_tag_member(token, 1, ['sign1', 'sign2', 'sign3', 'sign4'], [])
    tag.create_tag_member(token, 2, [], [4])
    yield
    qian_zhi(token)
