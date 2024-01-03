import time
import unittest
import requests
from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from businessCommon.dataOperator import DataOperator
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class get_Home_Page_Input(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['getHomePage']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    # @parameterized.expand
    def testCase01_input_must_key(self):
        """【获取首页便签】userId字段缺失"""
        step('请求获取首页便签接口')
        url = f'{self.host}{self.apiData["path1"]}'
        res = self.ar.get(url, sid=self.sid)
        self.assertEqual(404, res.status_code, msg='状态码校验失败')
        expect = {
            "timestamp": str,
            "status": 404,
            "error": "Not Found",
            "message": "No message available",
            "path": "/v3/notesvr/user/home/startindex/0/rows/9999/notes"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取首页便签信息接口，校验数据源的正确性')

    def testCase02_input_must_key(self):
        """【获取首页便签】startindex字段缺失"""
        step('请求获取首页便签接口')
        url = f'{self.host}{self.apiData["path2"]}'
        res = self.ar.get(url, sid=self.sid)
        self.assertEqual(404, res.status_code, msg='状态码校验失败')
        expect = {
            "timestamp": str,
            "status": 404,
            "error": "Not Found",
            "message": "No message available",
            "path": "/v3/notesvr/user/301701083/home/startindex/0/rows/notes"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取首页便签信息接口，校验数据源的正确性')

    def testCase03_input_must_key(self):
        """【获取首页便签】rows字段缺失"""
        step('请求获取首页便签接口')
        url = f'{self.host}{self.apiData["path3"]}'
        res = self.ar.get(url, sid=self.sid)
        self.assertEqual(404, res.status_code, msg='状态码校验失败')
        expect = {
            "timestamp": str,
            "status": 404,
            "error": "Not Found",
            "message": "No message available",
            "path": "/v3/notesvr/user/301701083/home/startindex/rows/9999/notes"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取首页便签接口，校验数据源的正确性')

    # def testCase02_input(self):
    #     """【新增分组】groupId 英文的大小写"""
    #     step('请求新增分组接口')
    #     url = f'{self.host}{self.apiData["path"]}'
    #     group_id = str(int(time.time() * 1000)) + '_groupId'
    #     # body = self.reBase
    #     body = {'groupId': group_id,
    #             'groupName': 'testGroup',
    #             'order': 0}
    #     body['groupId'] = 'OHKjhbvmn'
    #     res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
    #     self.assertEqual(200, res.status_code, msg='状态码校验失败')
    #     step('请求获取分组信息接口，校验数据源的正确性')
