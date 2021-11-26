"""
author : QY
"""
from apis.record import Record


class TestRecord:
    def setup(self):
        # 就业2 作业情况查询
        self.params1 = {
            "union_id": "oo7xa073wzsidZsxWtUL-4Ydql0w",
            "project_id": "131"
        }
        # 用户union_id错误
        self.params2 = {
            "union_id": "1",
            "project_id": "131"
        }
        # 班级id错误
        self.params3 = {
            "union_id": "oo7xa073wzsidZsxWtUL-4Ydql0w",
            "project_id": "1"
        }

        self.json = {
            "form": "string",
            "form_name": "string",
            "entry": {}
        }

        # union_id正确，获取该学员整体进度情况
        self.total1 = {
            "union_id": "oo7xa073wzsidZsxWtUL-4Ydql0w",
            "project_id": "131"

        }
        # 用户union_id错误
        self.total2 = {
            "union_id": "1",
            "project_id": "131"
        }
        # 班级id错误
        self.total3 = {
            "union_id": "oo7xa073wzsidZsxWtUL-4Ydql0w",
            "project_id": "1"
        }

    # 作业完成情况写入
    def test_write_homework(self):
        req = {
            "method": "POST",
            "url": "http://39.102.48.202:6089/api/record/homework",
            "json": self.json
        }
        r = self.send_api(req)
        print(r.text)

    # 用户id正确 班级正确 作业完成情况查询
    def test_search_homework1(self):
        r = Record().record_homework(self.params1)
        print(r)
        assert r["data"][4]["form_name"] == "【简答题】测试理论基础"

    # 用户id错误 班级正确 返回错误信息
    def test_search_homework2(self):
        r = Record().record_homework(self.params2)
        print(r)
        assert r["errmsg"] == "用户数据未找到！！！"

    # 用户id正确 班级错误 返回错误信息
    def test_search_homework3(self):
        r = Record().record_homework(self.params3)
        print(r)
        assert r["errmsg"] == "班级数据未找到！！！"

    # 输入正确参数，获取该学员整体进度情况
    def test_record_total1(self):
        r = Record().record_total(self.total1)
        print(r)
        assert r["data"]["homework_total_rate"] == 40

    # 用户id错误 班级正确 返回错误信息
    def test_record_total2(self):
        r = Record().record_total(self.total2)
        print(r)
        assert r["errmsg"] == "用户数据未找到！！！"

    # 用户id正确 班级错误 返回错误信息
    def test_record_total3(self):
        r = Record().record_total(self.total3)
        print(r)
        assert r["errmsg"] == "班级数据未找到！！！"
