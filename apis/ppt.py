"""
author : QY
"""
from apis.base_api import BaseApi


class PPt(BaseApi):
    # 根据 project_id、stage_id获取ppt信息,如果送了阶段,则只进行该阶段数据获取
    def get_ppt(self, params):
        url = "http://39.102.48.202:6089/api/ppt"
        r = self.get_info(url, params)
        return r.json()

    # 输入 班级名称, ppt名称, ppt_url 实现插入ppt的issue，并自动绑定到其同名的章节issue记录
    def ppt_add(self, json):
        ppt_url = "http://39.102.48.202:6089/api/ppt/quick_add"
        r = self.post_info(ppt_url, json)
        return r.json()
