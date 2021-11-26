"""
author : QY
"""
import logging
import requests


class BaseApi:
    # 设置logging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志等级
    logging.getLogger().setLevel(0)
    # 设置日志内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    # 设置日志生效
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        '''
        日志的方法
        :param msg:
        :return:
        '''
        return logging.info(msg)

    def send_api(self, req):
        self.log_info("--------request data--------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("--------response data--------")
        self.log_info(r.json())
        return r

    def get_info(self, url, params):
        # 获取信息
        req = {
            "method": "GET",
            "url": url,
            "params": params
        }
        r = self.send_api(req)
        return r

    def show_info(self, url):
        # 展示信息
        req = {
            "method": "GET",
            "url": url
        }
        r = self.send_api(req)
        return r

    def post_info(self, url, json):
        # 新增内容
        req = {
            "method": "POST",
            "url": url,
            "json": json
        }
        r = self.send_api(req)
        return r

    def golden_info(self,url):
        # 通过金数据 新增内容
        req = {
            "method":"POST",
            "url":url
        }
        r = self.send_api(req)
        return r

    def yaml_info(self, url):
        # 通过yaml文件新建内容
        req = {
            "method": "POST",
            "url": url
        }
        r = self.send_api(req)
        return r
