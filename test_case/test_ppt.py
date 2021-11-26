"""
author : QY
"""

from apis.ppt import PPt


class TestPPt:
    def setup(self):
        # 就业班2期 阶段1
        self.params1 = {
            "project_id": "131",
            "stage_id": "1"
        }
        # 错误id
        self.params2 = {
            "project_id": "12",
            "stage_id": "12"
        }
        # 班级错误
        self.data1 = {
            "class_name": "string",
            "ppt_subject": "string",
            "ppt_url": "string"
        }
        # 章节错误
        self.data2 = {
            "class_name": "就业班2期",
            "ppt_subject": "string",
            "ppt_url": "string"
        }
        # 正确参数
        self.data3 = {
            "class_name": "就业班2期",
            "ppt_subject": "毕业设计",
            "ppt_url": "string"
        }

    # 成功获取 某班级某阶段 ppt信息
    def test_ppt_get1(self):
        r = PPt().get_ppt(self.params1)
        assert r["data"][0]["stage"] == "阶段一"

    # 输入错误信息，不返回数据
    def test_ppt_get2(self):
        r = PPt().get_ppt(self.params2)
        print(r)
        assert r["data"] == []

    # 班级ID错误
    def test_ppt_quick_add1(self):
        r = PPt().ppt_add(self.data1)
        print(r)
        assert r["errmsg"] == "班级：string 的班级ID不存在！"

    # issue标题错误
    def test_ppt_quick_add2(self):
        r = PPt().ppt_add(self.data2)
        print(r)
        issue = self.data2["ppt_subject"]
        assert r["errmsg"] == f"找不到同名章节记录！issue标题：{issue}"

    # 成功
    def test_ppt_quick_add3(self):
        r = PPt().ppt_add(self.data3)
        print(r)
        # 获取 ppt issue编号 章节issue编号
        assert r["msg"] == "操作成功！PPT issue编号：36132, 章节issue编号：18638"
