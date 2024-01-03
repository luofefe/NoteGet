import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class deleteNoteInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['deleteNote']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    @parameterized.expand([[{'key': 'noteId', 'errorCode': -7}]])
    def testCase05_input_must_key(self, dic):
        """【删除便签】必填字段缺失"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
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
        """【删除便签】noteId 英文的大小写"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        # body = self.reBase
        body = {
            'noteId': note_id
        }
        body['noteId'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_input(self):
        """【删除便签】noteId 特殊字符"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        body['noteId'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_input(self):
        """【删除便签】noteId 空字符"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        body['noteId'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_input(self):
        """【删除便签】noteId 中文"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        body['noteId'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_input(self):
        """【删除便签】noteId "or"1=1"""
        step('请求删除便签接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        body['noteId'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')