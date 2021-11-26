"""
author : QY
"""
from apis.bind_phone import BindPhone


class TestPhone:
    def setup(self):
        self.json = {
            "union_id": "string",
            "phone": 0
        }

    def test_bind_phone(self):
        r = BindPhone().bind_phone(self.json)
        print(r)
