# ***
# @autor CWZ
# ***
import pytest

from day04_reqursts.api.department import Department

depart = Department()


# ð�̲��Ե�ǰ����������������
# @pytest.fixture(scope="session")
# def department_smoke(token):
#     depart.delete_department(token, 2)
#     depart.delete_department(token, 3)
#     depart.delete_department(token, 7)
#     yield
#     depart.delete_department(token, 5)
#     depart.delete_department(token, 6)


# �������Ų��Ե�ǰ����������������
# @pytest.fixture(scope="session")
# def department_add(token):
#     depart.delete_department(token, 5)
#     depart.delete_department(token, 6)
#     depart.delete_department(token, 7)
#     yield
#     depart.delete_department(token, 5)


# �޸Ĳ��Ų��Ե�ǰ����������������
@pytest.fixture(scope="session")
def department_update(token):
    depart.add_department(token, "smoke2", 1)
    yield
    depart.delete_department(token, 5)


# ɾ�����Ų��Ե�ǰ����������������
@pytest.fixture(scope="session")
def department_delete(token):
    depart.add_department(token, "deleted", 1)
