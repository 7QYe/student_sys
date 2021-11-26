"""
author : QY
"""
from apis.base_api import BaseApi


class BindPhone(BaseApi):
    def bind_phone(self, data):
        '''
        根据学员填写的手机号进行匹配，匹配上手机号之后给学员加入到对应的组群
        :return:
        '''
        bin_url = "http://39.102.48.202:6089/api/bind_phone"
        r = self.post_info(bin_url, data)
        return r.json()
