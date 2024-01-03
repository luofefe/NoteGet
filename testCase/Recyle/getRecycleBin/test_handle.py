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

    def testCase11_major(self):
        """【前置步骤新增一条回收站A用户便签数据】【前置步骤清空回收站】"""
        step('【INIT】删除回收站数据')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': [-1],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        step('【INIT】删除便签数据')
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
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        # """【前置步骤新增一条回收站B用户便签数据】"""
        """【前置步骤清空回收站】"""
        step('【INIT】删除回收站数据')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': [-1],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId2, self.sid2)
        step('【INIT】删除便签数据')
        url = f'{self.host}/v3/notesvr/delete'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        step('【INIT】B用户获取回收站便签B数据--数据隔离测试')
        url = f'{self.host}/v3/notesvr/user/{self.userId2}/invalid/startindex/0/rows/999/notes'
        res = self.ar.get(url, sid=self.sid2)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": 0,
            "webNotes": [
                {
                    'noteId': note_datas[0]['noteId'],
                    'createTime': int,
                    'star': 0,
                    'remindTime': int,
                    'remindType': 0,
                    'infoVersion': 2,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': '6MC5h1NpfG9+If6c2eE7UA==',
                    'summary': 'Kf7eO5uEBcJILXCBYt0skg==',
                    'thumbnail': None,
                    'contentVersion': 1,
                    'contentUpdateTime': int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase1101_major(self):
        # """【前置步骤新增一条回收站A用户便签数据】"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        step('【INIT】删除便签数据')
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
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        step('【INIT】删除回收站数据')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': [-1],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)

        step('【INIT】A用户获取回收站便签A数据--约束条件-状态限制')
        url = f'{self.host}/v3/notesvr/user/{self.userId}/invalid/startindex/0/rows/999/notes'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        res = self.ar.get(url, sid=self.sid, headers=headers)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": 0,
            "webNotes": []
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')