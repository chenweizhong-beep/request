# ***
# @autor CWZ
# ***

from day04_reqursts.api.base_api import BaseApi
from day04_reqursts.common.log import log
from day04_reqursts.common.mysql import mysql


class Schedule(BaseApi):
    path = "data\\schedule_api.yaml"

    def get_cal_id_list_1(self):
        query = "SELECT cal_id FROM calender;"
        # 从数据库获得的数据是元组类型
        data_touple = mysql.select(query)
        # 将元组转化为列表
        data_list = [i[0] for i in data_touple]
        return data_list

    def get_sch_id_list(self):
        qurey = "SELECT schedule_id FROM schedule_1 where status_a = 0;"
        data_touple = mysql.select(qurey)
        data_list = [i[0] for i in data_touple]
        return data_list

    def create_schedule(self, token, organizer, start_time, end_time, userid, summary, description, location):
        start_time = self.get_time(start_time)
        end_time = self.get_time(end_time)
        cal_id_list = self.get_cal_id_list_1()
        try:
            cal_id = cal_id_list[len(cal_id_list) - 1]
        except Exception as e:
            log.info(f"报错信息是:{e}")
            cal_id = cal_id_list
        d_data = {"token": token, "organizer": organizer, "start_time": start_time, "end_time": end_time,
                  "userid": userid, "summary": summary, "description": description, "location": location,
                  "cal_id": cal_id}
        res = self.send_api_data(self.path, d_data, "create")
        schedule_id = res['schedule_id']
        query = f"INSERT INTO schedule_1 (user_id,start_time,end_time,summary,description,location,cal_id," \
                f"schedule_id,status_a) " \
                f"VALUES {(organizer, start_time, end_time, summary, description, location, cal_id, schedule_id, 0)} ;"
        mysql.insert(query)
        return res

    def get_all_schedule(self, token, index, offset=None, limit=None):
        cal_id_list = self.get_cal_id_list_1()
        try:
            cal_id = cal_id_list[index]
        except Exception as e:
            log.info(f"报错信息是:{e}")
            cal_id = cal_id_list
        d_data = {"token": token, "index": index, "cal_id": cal_id, "offset": offset, "limit": limit}
        res = self.send_api_data(self.path, d_data, "get_all")
        return res

    def update_schedule(self, token, organizer, start_time, end_time, userid, summary, description, location, index):
        start_time = self.get_time(start_time)
        end_time = self.get_time(end_time)
        sch_id_list = self.get_sch_id_list()
        try:
            schedule_id = sch_id_list[index]
        except Exception as e:
            log.info(f"报错信息是:{e}")
            schedule_id = sch_id_list
        d_data = {"token": token, "organizer": organizer, "start_time": start_time, "end_time": end_time,
                  "userid": userid, "summary": summary, "description": description, "location": location,
                  "index": index, "schedule_id": schedule_id}
        res = self.send_api_data(self.path, d_data, "update")
        qurey = f"UPDATE schedule_1 SET start_time = '{start_time}', end_time = '{end_time}', summary = '{summary}', description = '{description}',location = '{location}' WHERE schedule_id = '{schedule_id}';"
        mysql.update(qurey)
        return res

    def delete_schedule(self, token, index):
        sch_id_list = self.get_sch_id_list()
        try:
            schedule_id = sch_id_list[index]
        except Exception as e:
            log.info(f"报错信息是:{e}")
            schedule_id = sch_id_list
        d_data = {"token": token, "index": index, "schedule_id": schedule_id}
        res = self.send_api_data(self.path, d_data, "delete")
        # query = f"delete from schedule_1 where schedule_id = '{schedule_id}';"
        query = f"update schedule_1 set status_a = 1 where schedule_id = '{schedule_id}';"
        mysql.delete(query)
        return res

    def get_schedule(self, token, index=None):
        if index is None:
            schedule_id_list = self.get_sch_id_list()
        else:
            schedule_id_list = [self.get_sch_id_list()[index]]
        d_data = {"token": token, "schedule_id_list": schedule_id_list}
        res = self.send_api_data(self.path, d_data, "get")
        return res
