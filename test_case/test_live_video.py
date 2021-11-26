"""
author : QY
"""

from apis.live_video import LiveVideo


class TestLiveVideo:
    def setup(self):
        # 正确的id
        self.params1 = {
            "project_id": "131"
        }
        # 错误的id
        self.params2 = {
            "project_id": "12"
        }

    # 成功获取直播信息
    def test_live_video1(self):
        r = LiveVideo().get_video(self.params1)
        print(r)
        assert r["data"][0]["video_type_name"] == "直播"

    # 信息输入错误，无法获取信息
    def test_live_video2(self):
        r = LiveVideo().get_video(self.params2)
        print(r)
        assert r["data"] == []
