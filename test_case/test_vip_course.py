"""
author : QY
"""
from apis.vip_course import VipCourse


class TestVipCourse:
    def setup(self):
        # 正确的openid
        self.params1 = {
            "open_id": "oo7xa073wzsidZsxWtUL-4Ydql0w"
        }
        # 错误的openid
        self.params2 = {
            "open_id":"12"
        }
        self.json = {
            "open_id": "string",
            "course_name": "string"
        }

    def test_vip_course1(self):
        '''
        正确的openid
        :return:
        '''
        r = VipCourse().get_vip_course(self.params1)
        print(r)
        assert len(r["data"]) == 5

    def test_vip_course2(self):
        '''
        错误的openid
        :return:
        '''
        r = VipCourse().get_vip_course(self.params2)
        print(r)
        assert len(r["data"]) == 5

    def test_vip_course_(self):
        r = VipCourse().post_vip_course(self.json)
        print(r)
