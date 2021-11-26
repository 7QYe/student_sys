"""
author : QY
"""
from apis.base_api import BaseApi


class Users(BaseApi):
    # 根据金数据发送来的学员信息，在redmine中创建对应的学员数据
    def users_info(self, ui_json):
        ui_url = "http://39.102.48.202:6089/api/users"
        r = self.post_info(ui_url, ui_json)
        return r.json()

    # 根据金数据发送来的学员信息，在redmine中创建对应的学员数据
    def users_golden(self):
        ug_url = "http://39.102.48.202:6089/api/users/from_golden"
        r = self.golden_info(ug_url)
        return r.json()
