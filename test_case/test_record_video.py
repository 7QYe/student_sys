"""
author : QY
"""


from apis.record_video import RecordVideo


class TestRecordVideo:
    def setup(self):
        # 输入正确的信息
        self.params1 = {
            "project_id": "131",
            "stage_id": "5"
        }
        # 输入错误的信息
        self.params2 = {
            "project_id": "1",
            "stage_id": "5"
        }
        # 输入错误的信息
        self.params3 = {
            "project_id": "1"
        }

    def test_record_video1(self):
        r = RecordVideo().get_record_video(self.params1)
        print(r)
        assert r["data"][0]["video_type_name"] == "录播"

    # 输入错误的班级id和阶段
    def test_record_video2(self):
        r = RecordVideo().get_record_video(self.params2)
        print(r)
        assert r["data"] == []

    # 错误的班级id 无阶段
    def test_record_video3(self):
        r = RecordVideo().get_record_video(self.params3)
        print(r)
        assert r["data"] == []
