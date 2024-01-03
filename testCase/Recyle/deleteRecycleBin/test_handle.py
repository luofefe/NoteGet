import unittest
import requests
from common.checkTools import CheckTools
import time
from copy import deepcopy
from businessCommon.dataOperator import DataOperator
from common.configRead import read_env_yaml
from common.caseLog import info, step, error, class_case_log
from businessCommon.apiRe import ApiRe


@class_case_log
class TestGetNotes(unittest.TestCase):
    envData = read_env_yaml()
    userId = envData['userId']
    sid = envData['sid']
    userId2 = envData['userId2']
    sid2 = envData['sid2']
    host = envData['host']
    ar = ApiRe()

    def testCase13_major(self):
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条A用户便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        step('【INIT】删除A用户便签A数据')
        url = f'{self.host}/v3/notesvr/delete'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        step('【INIT】B用户删除A用户回收站A便签数据--越权测试')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            "errorCode": -7,
            "errorMsg": ""
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')


    def testCase1301_major(self):
        # """【前置步骤新建一条回收站便签数据】"""
        step('【INIT】新增一条A用户便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        step('【INIT】删除A用户便签A数据')
        url = f'{self.host}/v3/notesvr/delete'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        step('【INIT】多次删除用户A下回收站便签A数据--约束条件-状态限制')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        body = {
            'noteIds': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)

        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        body = {
            'noteIds': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        # expect = {
        #     "responseTime": int
        # }
        # CheckTools().output_check(expect, res.json())
        # step('请求获取分组信息接口，校验数据源的正确性')


