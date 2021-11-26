"""
author : QY
"""
from apis.chapter import Chapter


class TestChapter:
    def setup(self):
        # 就业2 所有 章节信息
        self.params1 = {
            "project_id": "131"
        }
        # 就业2 第一阶段 信息
        self.params2 = {
            "project_id":"131",
            "stage_id" :"1"
        }
        # 错误的班级id 和阶段信息
        self.params3 = {
            "project_id":"1",
            "stage_id":"1"
        }

    # 成功获取章节信息
    def test_chapter1(self):
        r = Chapter().chapter(self.params1)
        # print(r.json())
        assert r["data"][0]["chapters"][0]["chapter"]["chapter_id"] == 17858

    # 获取 就业2 阶段1 的所有 章节 信息
    def test_chapter2(self):
        r = Chapter().chapter(self.params2)
        print(r["data"][0]["chapters"])
        assert len(r["data"][0]["chapters"]) == 8

    # 信息输入错误，获取为空
    def test_chapter3(self):
        r = Chapter().chapter(self.params1)
        assert r["data"] == []

