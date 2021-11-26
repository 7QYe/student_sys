"""
author : QY
"""
from apis.project import Project


class TestProject:
    def setup(self):
        # 正确id 就业2 咕噜噜
        self.params1 = {
            "open_id": "oo7xa073wzsidZsxWtUL-4Ydql0w"
        }
        # 错误id
        self.params2 = {
            "open_id": "1w"
        }

    # 正确id
    def test_get_project1(self):
        r = Project().get_pro_info(self.params1)
        print(r)
        assert r["data"]["open_id"] == self.params1["open_id"]
        assert r["data"]["vip_status"] == True

    # 输入错误id
    def test_get_project2(self):
        r = Project().get_pro_info(self.params2)
        print(r)
        assert r["data"]["vip_status"] == False

    def test_post_project(self):
        r = Project().pro_create()
        print(r)
