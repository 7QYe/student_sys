"""
author : QY
"""
from apis.base_api import BaseApi


class Project(BaseApi):
    # 根据 open_id 获取该学员的项目信息
    def get_pro_info(self, params):
        pro_url = "http://39.102.48.202:6089/api/project"
        r = self.get_info(pro_url, params)
        return r.json()

    # 通过yaml文件进行项目的创建操作
    def pro_create(self):
        pro_url = "http://39.102.48.202:6089/api/project"
        r = self.other_info(pro_url)
        return r.json()