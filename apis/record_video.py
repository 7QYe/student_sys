"""
author : QY
"""
from apis.base_api import BaseApi


class RecordVideo(BaseApi):

    # 根据 project_id(班级id) 获取该班级的录播信息,如果送了阶段,则只进行该阶段数据获取
    def get_record_video(self, params):
        re_url = "http://39.102.48.202:6089/api/record_video"
        r = self.get_info(re_url, params)
        return r.json()
