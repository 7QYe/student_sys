"""
author : QY
"""
from apis.stage import Stage


class TestSatge:
    def setup(self):
        self.params1 = {
            # 131 就业2
            "project_id": "131"
        }
        self.params2 = {
            #
            "project_id": "12"
        }

    # 成功获取信息
    def test_stage1(self):
        r = Stage().stage(self.params1)
        print(r)
        # data 数据不为空
        assert r['data']['grade_name'] == '就业班2期'

    # 输入错误的id，data返回为空
    def test_stage2(self):
        r = Stage().stage(self.params2)
        print(r)
        # data 数据不为空
        assert r['data'] == {}

