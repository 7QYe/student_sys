"""
author : QY
"""
from apis.base_api import BaseApi


class Stage(BaseApi):
    # 根据 project_id(班级id) 获取该班级阶段信息
    def stage(self, params):
        sta_url = "http://39.102.48.202:6089/api/stage"
        r = self.get_info(sta_url, params)
        return r.json()

