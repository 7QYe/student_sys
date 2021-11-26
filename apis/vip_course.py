"""
author : QY
"""
from apis.base_api import BaseApi


class VipCourse(BaseApi):
    def get_vip_course(self, params):
        '''
        根据 open_id 获取用户赠送课的信息
        :return:
        '''
        vip1_url = "http://39.102.48.202:6089/api/vip_course"
        r = self.get_info(vip1_url, params)
        return r.json()

    def post_vip_course(self, data):
        '''
        根据 open_id 和课程的受众申请该课程的兑换码
        :param data:
        :return:
        '''
        vip2_url = "http://39.102.48.202:6089/api/vip_course"
        r = self.post_info(vip2_url,data)
        return r.json()
