"""
author : QY
"""
from apis.base_api import BaseApi


class Record(BaseApi):
    # 查询作业完成情况,提交状态：0：未提交，1：已提交
    def record_homework(self, params):
        reh_url = "http://39.102.48.202:6089/api/record/homework"
        r = self.get_info(reh_url, params)
        return r.json()

    # 查询整体进度情况
    def record_total(self,params):
        tol_url = "http://39.102.48.202:6089/api/record/total"
        r = self.get_info(tol_url,params)
        return r.json()

