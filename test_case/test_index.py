"""
author : QY
"""
from apis.index import Index


class TestIndex:
    def setup(self):
        self.detail = {
            "course_detail_id": "12"
        }
        self.menu1 = {
            "vip_status": "true"
        }
        self.menu2 = {
            "vip_status": "false"
        }

    # 展示学员系统首页的banner数据
    def test_banner(self):
        r = Index().banner()
        print(r)
        assert r["data"][0]["index_subject"] == "pytest与接口自动化测试训练营"

    # 展示学员系统首页的课程列表数据
    def test_class_list(self):
        r = Index().class_list()
        print(r)
        assert r["data"][0]["index_subject"] == "软件测试 / 名企定向培养测试开发进阶班"

    def test_course_detail(self):
        r = Index().course_detail(self.detail)
        print(r)

    # 展示学员系统首页的目录数据
    def test_menu(self):
        r = Index().menu()
        print(r)
        assert r["data"][0]["menu_name"] == "测试开发进阶班"

    # true
    def test_study_menu1(self):
        r = Index().study_menu(self.menu1)
        print(r)
        assert r["data"][1]["son_menus"][0]["study_menu_url"] == "https://ceshiren.com/c/job/31"

    # false
    def test_study_menu2(self):
        r = Index().study_menu(self.menu2)
        print(r)
        assert r["data"][1]["son_menus"][0]["study_menu_tips"] == "vip学员专属"
