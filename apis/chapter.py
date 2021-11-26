"""
author : QY
"""
from apis.base_api import BaseApi


class Chapter(BaseApi):
    # 根据 project_id(班级id)和stage_id 获取该班级的阶段章节信息,若未给定stage_id则展示全部数据
    def chapter(self,params):
        cha_url = "http://39.102.48.202:6089/api/chapter"
        r = self.get_info(cha_url, params)
        return r.json()