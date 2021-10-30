# ***
# @autor CWZ
# ***
import datetime
import json


# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime("%Y-%m-%d")
#         else:
#             return json.JSONEncoder.default(self, obj)
#
#
# dic = {'name': 'jack', 'create_time': "2021-10-14"}
# print(json.dumps(dic))
# print(json.dumps(dic, cls=DateEncoder))
