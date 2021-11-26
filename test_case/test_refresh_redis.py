"""
author : QY
"""

from apis.refresh_redis import RefreshRedis


class TestRefreshRedis:
    def setup(self):
        # 错误的参数
        self.params1 = {
            "class_name": "1"
        }

    def setup(self):
        # 正确的参数
        self.params2 = {
            "class_name":"就业班2期"
        }

    # 错误的参数
    def test_refresh_redis1(self):
        r = RefreshRedis().refresh_redis(self.params1)
        assert r["data"]["status"] == "Error"

    # 正确的参数
    def test_refresh_redis2(self):
        r = RefreshRedis().refresh_redis(self.params2)
        print(r.json())
