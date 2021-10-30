# ***
# @autor CWZ
# ***
from day04_reqursts.api.base_api import BaseApi


class Tag(BaseApi):
    path = "data\\tag_api.yaml"

    def creat_tag(self, token, tagid, tagname):
        d_data = {"token": token, "tagid": tagid, "tagname": tagname}
        res = self.send_api_data(self.path, d_data, "creat")
        return res

    def update_tag(self, token, tagid, tagname):
        d_data = {"token": token, "tagid": tagid, "tagname": tagname}
        res = self.send_api_data(self.path, d_data, "update")
        return res

    def delete_tag(self, token, tagid):
        d_data = {"token": token, "tagid": tagid}
        res = self.send_api_data(self.path, d_data, "delete")
        return res

    def get_all_tag(self, token):
        d_data = {"token": token}
        res = self.send_api_data(self.path, d_data, "get_all")
        return res

    def create_tag_member(self, token, tagid, userlist, partylist):
        d_data = {"token": token, "tagid": tagid, "userlist": userlist, "partylist": partylist}
        res = self.send_api_data(self.path, d_data, "create_tag_member")
        return res

    def delete_tag_member(self, token, tagid, userlist, partylist):
        d_data = {"token": token, "tagid": tagid, "userlist": userlist, "partylist": partylist}
        res = self.send_api_data(self.path, d_data, "delete_tag_member")
        return res

    def get_tag_member(self, token, tagid):
        d_data = {"token": token, "tagid": tagid}
        res = self.send_api_data(self.path, d_data, "get_tag_member")
        return res
