# ***
# @autor CWZ
# ***
from api.base_api import BaseApi


class MeetingRoom(BaseApi):
    path = "data\\meeting_room_api.yaml"

    def create_meeting_room(self, token, name, capacity, city, building, floor, equipment):
        d_data = {"token": token, "name": name, "capacity": capacity, "city": city, "building": building,
                  "floor": floor, "equipment": equipment}
        res = self.send_api_data(self.path, d_data, "create_meeting")
        return res

    def get_meeting_room(self, token, city, building, floor, equipment):
        d_data = {"token": token, "city": city, "building": building, "floor": floor, "equipment": equipment}
        res = self.send_api_data(self.path, d_data, "get_meeting")
        return res

    def update_meeting_room(self, token, meetingroom_id, name, capacity, city, building, floor, equipment):
        d_data = {"token": token, "meetingroom_id": meetingroom_id, "name": name, "capacity": capacity, "city": city,
                  "building": building, "floor": floor, "equipment": equipment}
        res = self.send_api_data(self.path, d_data, "update_meeting")
        return res

    def delete_meeting_room(self, token, meetingroom_id):
        d_data = {"token": token, "meetingroom_id": meetingroom_id}
        res = self.send_api_data(self.path, d_data, "delete_meeting")
        return res
