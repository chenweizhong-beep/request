# ***
# @autor CWZ
# ***
import allure
import pytest

from api.department import Department
from common.log import log

url = "https://work.weixin.qq.com/api/doc/90000/90135/90195"


@allure.testcase(url, "api地址")
@allure.feature("部门增删改查等接口测试")
class TestDepartment:
    # 实例化部门类
    d = Department()
    # 读取department.yaml文件中的测试数据
    datas = d.yaml_load("data\\department.yaml")
    add_data = datas['add']['data']
    add_ids = datas['add']['ids']

    get_data = datas['get']['data']
    get_ids = datas['get']['ids']

    update_data = datas['update']['data']
    update_ids = datas['update']['ids']

    delete_data = datas['delete']['data']
    delete_ids = datas['delete']['ids']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("增加部门接口")
    @pytest.mark.parametrize("parentid, name,errcode, errmsg, log_name", add_data, ids=add_ids)
    def test_add_department(self, token, parentid, name, errcode, errmsg, log_name):
        log.info(f"{30 * '<<'}开始测试增加部门{30 * '>>'}")
        res = self.d.add_department(token=token, name=name, parentid=parentid)
        log.info(f"{30 * '<<'}增加部门测试结束{30 * '>>'}")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获取部门接口")
    @pytest.mark.parametrize("id, errcode, errmsg", get_data, ids=get_ids)
    def test_get_department(self, token, id, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试查询部门{30 * '>>'}")
        res = self.d.get_department(token=token, id=id)
        log.info(f"{30 * '<<'}查询部门测试结束{30 * '>>'}")
        assert res['errcode'] == errcode
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("修改部门接口")
    @pytest.mark.parametrize("id,name,errcode,errmsg", update_data, ids=update_ids)
    def test_update_department(self, token, id, name, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试修改部门{30 * '>>'}")
        res = self.d.update_department(token=token, id=id, name=name)
        log.info(f"{30 * '<<'}修改部门测试结束{30 * '>>'}")
        assert res['errcode'] == errcode
        assert errmsg in res['errmsg']

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除部门接口")
    @pytest.mark.parametrize("id, errcode, errmsg", delete_data, ids=delete_ids)
    def test_delete_department(self, token, id, errcode, errmsg):
        log.info(f"{30 * '<<'}开始测试删除部门{30 * '>>'}")
        res = self.d.delete_department(token=token, id=id)
        log.info(f"{30 * '<<'}删除部门测试结束{30 * '>>'}")
        assert res['errcode'] == errcode
        assert errmsg in res['errmsg']

    # def test_add_depart(self, token, department_smoke):
    #     log.info("======开始冒烟增加部门测试======")
    #     res = self.d.add_department(token, 'smoke2', 1)
    #     log.info("======结束冒烟增加部门测试======")
    #     assert res["errcode"] == 0
    #     assert "created" in res["errmsg"]
