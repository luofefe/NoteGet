import time
import unittest

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class updateNoteContentInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['updateNoteContent']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    # noteId字符串校验点
    def testCase02_noteId_input(self):
        """【更新便签内容】noteId 英文的大小写"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['noteId'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_noteId_input(self):
        """【更新便签内容】noteId 特殊字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['noteId'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_noteId_input(self):
        """【更新便签内容】noteId 空字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['noteId'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_noteId_input(self):
        """【更新便签内容】noteId 中文"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['noteId'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_noteId_input(self):
        """【更新便签内容】noteId "or"1=1"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['noteId'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    # title字符串校验点
    def testCase02_title_input(self):
        """【更新便签内容】title 英文的大小写"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['title'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_title_input(self):
        """【更新便签内容】title 特殊字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['title'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_title_input(self):
        """【更新便签内容】title 空字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['title'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_title_input(self):
        """【更新便签内容】title 中文"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['title'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_title_input(self):
        """【更新便签内容】title "or"1=1"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['title'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    # summary字符串校验点
    def testCase02_summary_input(self):
        """【更新便签内容】summary 英文的大小写"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['summary'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_summary_input(self):
        """【更新便签内容】summary 特殊字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['summary'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_summary_input(self):
        """【更新便签内容】summary 空字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['summary'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_summary_input(self):
        """【更新便签内容】summary 中文"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['summary'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_summary_input(self):
        """【更新便签内容】summary "or"1=1"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['summary'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    # body字符串校验点
    def testCase02_body_input(self):
        """【更新便签内容】body 英文的大小写"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['body'] = 'OHKjhbvmn'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_body_input(self):
        """【更新便签内容】body 特殊字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['body'] = '@#￥%……&*（；'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase04_body_input(self):
        """【更新便签内容】body 空字符"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['body'] = ''
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(412, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase05_body_input(self):
        """【更新便签内容】body 中文"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['body'] = '接电话反馈'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase06_body_input(self):
        """【更新便签内容】body "or"1=1"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body['body'] = '"or"1=1'
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        step('请求获取分组信息接口，校验数据源的正确性')