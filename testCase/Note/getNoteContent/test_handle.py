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

    def testCase05_major(self):
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条a用户便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        step('【INIT】b用户获取a用户便签内容数据--越权测试')
        url = f'{self.host}/v3/notesvr/get/notebody'
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


    def testCase0501_major(self):  #--数据隔离测试
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条A用户便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        print(note_datas)
        step('【INIT】新增一条B用户便签数据')
        note_datasB = DataOperator().create_notesB(1, self.userId2, self.sid2)
        print(note_datasB)
        step('【INIT】B用户获取B用户便签内容数据')
        url = f'{self.host}/v3/notesvr/get/notebody'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': ['1703746231872_noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": str,
                    "noteId": str,
                    "infoNoteId": str,
                    "bodyType": int,
                    "body": str,
                    "contentVersion": int,
                    "contentUpdateTime": int,
                    "title": str,
                    "valid": int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')




    def testCase0502_major(self):
        # 【前置】清空用户便签数据
        step("清空用户便签数据")
        DataOperator().clear_notes(self.userId, self.sid)
        step('【INIT】获取a用户便签内容数据--不同的处理数量用户a获取0条便签')
        url = f'{self.host}/v3/notesvr/get/notebody'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': note_id,
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            "errorCode": -7,
            "errorMsg": ""
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase0503_major(self):
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条a用户便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        print(note_datas)
        # """【前置步骤删除一条便签数据】"""
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
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        print(body)
        print(res)

        step('【INIT】约束条件--状态限制--a用户获取已经删除的便签内容')
        url = f'{self.host}/v3/notesvr/get/notebody'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': note_datas[0]['noteId'],
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(body)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            "errorCode": -7,
            "errorMsg": ""
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')