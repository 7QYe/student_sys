"""
author : QY
"""
from apis.base_api import BaseApi


class RefreshRedis(BaseApi):
    # 刷新redis缓存的课程数据。课程名称必填，支持输入单个课程名称， 或者输入 all 表示所有课程名称
    def refresh_redis(self,params):
        ref_url = "http://39.102.48.202:6089/api/refresh_redis"
        r = self.get_info(ref_url, params)
        return r.json()