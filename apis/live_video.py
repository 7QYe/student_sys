"""
author : QY
"""
from apis.base_api import BaseApi


class LiveVideo(BaseApi):
    # 根据 project_id(班级id) 获取该班级的直播信息
    def get_video(self,params):
        vi_url = "http://39.102.48.202:6089/api/live_video"
        r = self.get_info(vi_url, params)
        return r.json()
