# ***
# @autor CWZ
# ***
from api.base_api import BaseApi
from common.log import log
from common.mysql import mysql


class Calender(BaseApi):
    path = "data\\calender_api.yaml"

    def get_cal_id_list(self):
        query = "SELECT cal_id FROM calender;"
        # 从数据库获得的数据是元组类型
        data_touple = mysql.select(query)
        # 将元组转化为列表
        data_list = [i[0] for i in data_touple]
        return data_list

    def create_calender(self, token, organizer, readonly, set_as_default, summary, color, description, userid, userid1):
        d_data = {"token": token, "organizer": organizer, "readonly": readonly, "set_as_default": set_as_default,
                  "summary": summary, "color": color, "description": description, "userid": userid, "userid1": userid1}
        res = self.send_api_data(self.path, d_data, "create")

        cal_id = res['cal_id']
        qurey = f"INSERT INTO calender (user_id,readonly,set_as_deafult,summary,color,description,cal_id) VALUES {(organizer, readonly, set_as_default, summary, color, description, cal_id)} ;"
        mysql.insert(qurey)
        return res

    def get_calender(self, token, index=None):
        cal_id_list = []
        try:
            log.info(f"index的值是：{index}")
            '''
            通过index判断是查询所有日历信息，还是查询单个日历信息
            '''
            if index is None:
                cal_id_list = self.get_cal_id_list()
            else:
                cal_id_list.append(self.get_cal_id_list()[index])
        except Exception as e:
            log.error(f"报错信息是：{e}")
        d_data = {"token": token, "cal_id_list": cal_id_list}
        res = self.send_api_data(self.path, d_data, 'get')
        return res

    def update_calender(self, token, readonly, summary, color, description, userid, index=None):
        cal_id_list = self.get_cal_id_list()
        try:
            cal_id = cal_id_list[index]
        except Exception as e:
            log.info(f"报错信息是：{e}")
            cal_id = cal_id_list
        d_data = {"token": token, "readonly": readonly, "summary": summary, "color": color, "description": description,
                  "userid": userid, "cal_id": cal_id}
        res = self.send_api_data(self.path, d_data, "update")
        qurey = f"UPDATE calender SET readonly = {readonly}, summary = '{summary}', color = '{color}', description = '{description}' WHERE cal_id = '{cal_id}';"
        mysql.insert(qurey)
        return res

    def delete_calender(self, token, index=None):
        cal_id_list = self.get_cal_id_list()
        try:
            cal_id = cal_id_list[index]
        except Exception as e:
            log.info(f"报错信息是：{e}")
            cal_id = cal_id_list
        d_data = {"token": token, "cal_id": cal_id, "index": index}
        res = self.send_api_data(self.path, d_data, "delete")
        query = f"delete from calender where cal_id = '{cal_id}'"
        mysql.delete(query)
        return res
