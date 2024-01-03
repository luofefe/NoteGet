import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from businessCommon.dataOperator import DataOperator
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class getCalendarNoteInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['getCalendarNote']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    @parameterized.expand([[{'key': 'remindStartTime', 'errorCode': -7}], [{'key': 'remindEndTime', 'errorCode': -7}],
                           [{'key': 'startIndex', 'errorCode': -7}], [{'key': 'rows', 'errorCode': -7}]])
    def testCase08_input_must_key(self, dic):
        """【获取用户日历下便签】必填字段缺失"""
        step('获取用户日历下便签接口')
        url = f"{self.host}{self.apiData['path']}"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        body = {
            'remindStartTime': 1703855825,
            'remindEndTime': 1704028625,
            'startIndex': 0,
            'rows': 100
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(res.json())
        self.assertEqual(500, res.status_code, msg='状态码校验失败')

    def testCase02_input(self):
        """【获取用户日历下便签】remindStartTime 结束的时间戳 > 当前时间"""
        step('请求获取用户日历下便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        body = {
            'remindStartTime': 1411111111111,
            'remindEndTime': 5633008085000,
            'startIndex': 0,
            'rows': 0
        }
        body['remindStartTime'] = 3221222212222
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_input(self):
        """【获取用户日历下便签】remindStartTime 为负数"""
        step('请求获取用户日历下便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        body = {
            'remindStartTime': 1411111111111,
            'remindEndTime': 5633008085000,
            'startIndex': 0,
            'rows': 0
        }
        body['remindStartTime'] = -3221222212222
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_input(self):
        """【获取用户日历下便签】remindStartTime 为极小数值"""
        step('请求获取用户日历下便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        body = {
            'remindStartTime': 1411111111111,
            'remindEndTime': 5633008085000,
            'startIndex': 0,
            'rows': 0
        }
        body['remindStartTime'] = 1000000000001
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_input(self):
        """【获取用户日历下便签】remindStartTime 为极大数值"""
        step('请求获取用户日历下便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        body = {
            'remindStartTime': 1411111111111,
            'remindEndTime': 5633008085000,
            'startIndex': 0,
            'rows': 0
        }
        body['remindStartTime'] = 9999999999999
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(412, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')
