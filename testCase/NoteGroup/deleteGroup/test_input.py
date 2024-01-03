import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class DeleteGroupInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['deleteGroup']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    @parameterized.expand([[{'key': 'groupId', 'errorCode': -1010}]])
    def testCase01_input_must_key(self, dic):
        """【删除分组】必填字段缺失"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': group_id
        }
        body.pop(dic['key'])
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(412, res.status_code, msg='状态码校验失败')
        expect = {
            'errorCode': -1010,
            'errorMsg': "GroupId Requested!"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase02_input(self):
        """【删除分组】groupId 英文的大小写"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # body = self.reBase
        body = {'groupId': group_id,
                'groupName': 'testGroup',
                'order': 0}
        body['groupId'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_input(self):
        """【删除分组】groupId 特殊字符"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # body = self.reBase
        body = {'groupId': group_id,
                'groupName': 'testGroup',
                'order': 0}
        body['groupId'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_input(self):
        """【删除分组】groupId 空字符"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # body = self.reBase
        body = {'groupId': group_id,
                'groupName': 'testGroup',
                'order': 0}
        body['groupId'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_input(self):
        """【删除分组】groupId 中文"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # body = self.reBase
        body = {'groupId': group_id,
                'groupName': 'testGroup',
                'order': 0}
        body['groupId'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_input(self):
        """【删除分组】groupId "or"1=1"""
        step('请求删除分组接口')
        url = f'{self.host}{self.apiData["path"]}'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # body = self.reBase
        body = {'groupId': group_id,
                'groupName': 'testGroup',
                'order': 0}
        body['groupId'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')