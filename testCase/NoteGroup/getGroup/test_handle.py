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

    def testCase01_major(self):
        # 【前置】清空用户分组
        step("清空用户分组")
        DataOperator().clear_groups(self.userId, self.sid)
        # """【前置步骤新建一条分组数据】"""
        step('【INIT】新增一条A用户分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        print(note_datas)
        # 【前置】清空用户分组
        step("清空用户分组")
        DataOperator().clear_groups(self.userId2, self.sid2)
        step('【INIT】新增一条B用户分组数据')
        note_datasB = DataOperator().create_groups(1, self.userId2, self.sid2)
        print(note_datasB)
        step('【INIT】B用户获取分组B数据--数据隔离测试')
        url = f'{self.host}/v3/notesvr/get/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        body = {"excludeInValid": "true"}
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'requestTime': int,
            'noteGroups': [
                {
                    "userId": self.userId2,
                    "groupId": note_datasB[0]['groupId'],
                    "groupName": str,
                    "order": 0,
                    "valid": 1,
                    "updateTime": int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())

    def testCase0101_major(self):
        # 【前置】清空用户分组
        step("清空用户分组")
        DataOperator().clear_groups(self.userId, self.sid)
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条A用户分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        print(note_datas)
        step('【INIT】删除分组数据')
        url = f'{self.host}/v3/notesvr/delete/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": note_datas[0]['groupId']
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        step('【INIT】A用户获取分组A数据--约束条件-状态限制')
        url = f'{self.host}/v3/notesvr/get/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        body = {"excludeInValid": "true"}
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'requestTime': int,
            'noteGroups': [
                {
                    "userId": self.userId,
                    "groupId": note_datas[0]['groupId'],
                    "groupName": str,
                    "order": 0,
                    "valid": 1,
                    "updateTime": int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())

    def testCase0102_major(self):
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条A用户分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        print(note_datas)
        step('【INIT】B用户获取A用户首页分组A数据--约束条件-权限控制')
        url = f'{self.host}/v3/notesvr/get/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {"excludeInValid": "true"}
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'requestTime': int,
            'noteGroups': [
                {
                    "userId": self.userId2,
                    "groupId": note_datas[0]['groupId'],
                    "groupName": str,
                    "order": 0,
                    "valid": 1,
                    "updateTime": int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())