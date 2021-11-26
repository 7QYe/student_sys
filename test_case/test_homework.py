"""
author : QY
"""

from apis.homework import HomeWork


class TestHomeWork:
    def setup(self):
        # 就业2 阶段17 作业信息
        self.params1 = {
            "project_id": "131",
            "stage_id": "17"
        }
        # 就业2 全部 作业信息
        self.params2 = {
            "project_id": "131"
        }
        self.params3 = {
            "project_id":"2"
        }

    # 获取 就业2 阶段17 作业信息
    def test_homework1(self):
        r = HomeWork().homework(self.params1)
        print(r)
        assert r["data"][0]["stage_name"] == "Python 编程语言"

    # 获取 就业2 所有作业信息
    def test_homework2(self):
        r = HomeWork().homework(self.params2)
        # 5个 阶段的作业信息
        assert len(r["data"]) == 5

    # 参数输入错误 无法获取信息 返回数据为空
    def test_homework3(self):
        r = HomeWork().homework(self.params3)
        # data 值为空
        assert r["data"] == []

