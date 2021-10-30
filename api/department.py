# ***
# @autor CWZ
# ***

from api.base_api import BaseApi


class Department(BaseApi):
    def add_department(self, token, name, parentid):
        d_data = {"token": token, "name": name, "parentid": parentid}
        res = self.send_api_data("data\\department_api.yaml", d_data, "add")
        return res

    def get_department(self, token, id):
        d_data = {"token": token, "id": id}
        res = self.send_api_data("data\\department_api.yaml", d_data, "get")
        return res

    def update_department(self, token, id, name):
        d_data = {"token": token, "id": id, "name": name}
        res = self.send_api_data("data\\department_api.yaml", d_data, "update")
        return res

    def delete_department(self, token, id):
        d_data = {"token": token, "id": id}
        res = self.send_api_data("data\\department_api.yaml", d_data, "delete")
        return res


if __name__ == '__main__':
    d = Department()
    datas = d.yaml_load("data/department.yaml")
    # print(json.dumps(datas, ensure_ascii=False, indent=2))
    add_data = datas['add']['data']
    print(add_data)
    add_ids = datas['add']['ids']
    print(add_ids)
