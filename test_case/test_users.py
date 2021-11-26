"""
author : QY
"""
from apis.users import Users


class TestUsers:
    def setup(self):
        self.json = {
            "data": {},
            "class_name": "string"
        }

    def test_users(self):
        r = Users().users_info(self.json)
        print(r)

    def test_users_golden(self):
        r = Users().users_golden()
        print(r)
