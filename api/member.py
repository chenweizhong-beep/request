# ***
# @autor CWZ
# ***

from api.base_api import BaseApi


class Member(BaseApi):
    path = "data\\member_api.yaml"

    def creat_member(self, token, name, userid, mobile):
        d_data = {"token": token, "name": name, "userid": userid, "mobile": mobile}
        res = self.send_api_data(self.path, d_data, "add")
        return res

    def update_member(self, token, name, userid, mobile):
        d_data = {"token": token, "name": name, "userid": userid, "mobile": mobile}
        res = self.send_api_data(self.path, d_data, "update")
        return res

    def get_menmber(self, token, userid):
        d_data = {"token": token, "userid": userid}
        res = self.send_api_data(self.path, d_data, "get")
        return res

    def delete_membera(self, token, userid):
        d_data = {"token": token, "userid": userid}
        res = self.send_api_data(self.path, d_data, "delete")
        return res

    def batch_delete_member(self, token, useridlist):
        d_data = {"token": token, "useridlist": useridlist}
        res = self.send_api_data(self.path, d_data, "batch_delete")
        return res

    def get_depart_simple(self, token, department_id, fetch_child):
        d_data = {"token": token, "department_id": department_id, "fetch_child": fetch_child}
        res = self.send_api_data(self.path, d_data, "depart_simple")
        return res

    def get_depart_explicit(self, token, department_id, fetch_child):
        d_data = {"token": token, "department_id": department_id, "fetch_child": fetch_child}
        res = self.send_api_data(self.path, d_data, "depart_explicit")
        return res

    def get_active_status(self, token, data):
        d_data = {"token": token, "data": data}
        res = self.send_api_data(self.path, d_data, "active", "json", "date")
        return res

    def get_invite_qr(self, token, size_type):
        d_data = {"token": token, "size_type": size_type}
        res = self.send_api_data(self.path, d_data, "invite")
        return res

