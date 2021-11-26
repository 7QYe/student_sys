"""
author : QY
"""
from apis.base_api import BaseApi


class HomeWork(BaseApi):
    # 根据 project_id、stage_id、获取作业信息,如果送了阶段,则只进行该阶段数据获取
    def homework(self,params):
        hom_url = "http://39.102.48.202:6089/api/homework"
        r = self.get_info(hom_url, params)
        return r.json()
