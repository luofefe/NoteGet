import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class deleteRecycleBinInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['deleteRecycleBin']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    @parameterized.expand([[{'key': 'noteIds', 'errorCode': -7}]])
    def testCase01_input_must_key(self, dic):
        """【删除清空回收站】必填字段缺失"""
        step('请求删除清空回收站接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': [note_id],
        }
        body.pop(dic['key'])
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            "errorCode": -7,
            "errorMsg": "参数不合法！"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase02_input(self):
        """【删除清空回收站】noteIds 为[]"""
        step('请求删除清空回收站接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        # body = self.reBase
        body = {
            'noteIds': [note_id]
        }
        body['noteIds'] = []
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_input(self):
        """【删除清空回收站】noteIds 存在子对象 [234, [123, 123]]"""
        step('请求删除清空回收站接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        # body = self.reBase
        body = {
            'noteIds': [note_id]
        }
        body['noteIds'] = [234, [123, 123]]
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_input(self):
        """【删除清空回收站】noteIds 为null"""
        step('请求删除清空回收站接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        # body = self.reBase
        body = {
            'noteIds': [note_id]
        }
        body['noteIds'] = 'null'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')
