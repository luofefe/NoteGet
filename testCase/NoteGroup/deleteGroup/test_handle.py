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
        step('【INIT】新增一条A用户分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        step('【INIT】B用户删除A用户分组A数据--越权测试')
        url = f'{self.host}/v3/notesvr/delete/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": group_id
        }
        res = self.ar.post(url=url, body=body, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": int
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')


    def testCase0501_major(self):
        # """【前置步骤新建一条分组数据】"""
        step('【INIT】新增一条A用户分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        step('【INIT】用户A多次删除分组A数据--约束条件-状态限制')
        url = f'{self.host}/v3/notesvr/delete/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": group_id
        }
        res = self.ar.post(url=url, body=body, sid=self.sid2, user_id=self.userId2)

        url = f'{self.host}/v3/notesvr/delete/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId2,
            'Cookie': f"wps_sid={self.sid2}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": group_id
        }
        res = self.ar.post(url=url, body=body, sid=self.sid2, user_id=self.userId2)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": int
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')


    def testCase0502_major(self):
        # 【前置】清空用户分组数据
        step("清空用户分组数据")
        DataOperator().clear_groups(self.userId, self.sid)
        step('【INIT】用户A删除不存在分组数据--不同的处理数量')
        url = f'{self.host}/v3/notesvr/delete/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": group_id
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": int
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')