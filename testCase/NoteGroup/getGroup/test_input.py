import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class getGroupInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['getGroup']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    @parameterized.expand([[{'key': 'excludeInValid', 'errorCode': -7}]])
    def testCase01_input_must_key(self, dic):
        """【获取分组】选填字段缺失"""
        step('请求获取分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "excludeInValid": "true"
        }
        body.pop(dic['key'])
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'requestTime': int,
            'noteGroups': [
                {
                    "userId": self.userId,
                    "groupId": int,
                    "groupName": str,
                    "order": 0,
                    "valid": 1,
                    "updateTime": int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    # def testCase02_input(self):
    #     """【获取分组】excludeInValid 值为true"""
    #     step('请求获取分组接口')
    #     url = f'{self.host}{self.apiData["path"]}'
    #     group_id = str(int(time.time() * 1000)) + '_groupId'
    #     # body = self.reBase
    #     body = {'excludeInValid': 'true'}
    #     body['excludeInValid'] = 'true'
    #     res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
    #     self.assertEqual(200, res.status_code, msg='状态码校验失败')
    #     step('请求获取分组信息接口，校验数据源的正确性')
    #
    # def testCase03_input(self):
    #     """【获取分组】excludeInValid 值为false"""
    #     step('请求获取分组接口')
    #     url = f'{self.host}{self.apiData["path"]}'
    #     group_id = str(int(time.time() * 1000)) + '_groupId'
    #     # body = self.reBase
    #     body = {'excludeInValid': 'true'}
    #     body['excludeInValid'] = 'false'
    #     res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
    #     self.assertEqual(200, res.status_code, msg='状态码校验失败')
    #     step('请求获取分组信息接口，校验数据源的正确性')
    #
    # def testCase04_input(self):
    #     """【获取分组】excludeInValid 值为null"""
    #     step('请求获取分组接口')
    #     url = f'{self.host}{self.apiData["path"]}'
    #     group_id = str(int(time.time() * 1000)) + '_groupId'
    #     # body = self.reBase
    #     body = {'excludeInValid': 'true'}
    #     body['excludeInValid'] = 'null'
    #     res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
    #     self.assertEqual(200, res.status_code, msg='状态码校验失败')
    #     step('请求获取分组信息接口，校验数据源的正确性')