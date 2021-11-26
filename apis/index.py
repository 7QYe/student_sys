"""
author : QY
"""
from apis.base_api import BaseApi


class Index(BaseApi):
    def banner(self):
        '''
        展示学员系统首页的banner数据
        :return:
        '''
        ban_url = "http://39.102.48.202:6089/api/index/banner"
        r = self.show_info(ban_url)
        return r.json()

    def class_list(self):
        '''
        展示学员系统首页的课程列表数据
        :param params:
        :return:
        '''
        cls_list_url = "http://39.102.48.202:6089/api/index/class_list"
        r = self.show_info(cls_list_url)
        return r.json()

    def course_detail(self, params):
        '''
        根据课程的详情id，展示课程的详情信息
        :param params:
        :return:
        '''
        corde_url = "http://39.102.48.202:6089/api/index/course_detail"
        r = self.get_info(corde_url, params)
        return r.json()

    def menu(self):
        '''
        展示学员系统首页的目录数据
        :return:
        '''
        menu_url = "http://39.102.48.202:6089/api/index/menu"
        r = self.show_info(menu_url)
        return r.json()

    def study_menu(self, params):
        '''
        展示学员系统学习页的目录数据
        :return:
        '''
        stme_url = "http://39.102.48.202:6089/api/index/study_menu"
        r = self.get_info(stme_url, params)
        return r.json()
