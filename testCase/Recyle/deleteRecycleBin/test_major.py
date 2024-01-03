# import unittest
# import requests
# from common.checkTools import CheckTools
# import time
# from copy import deepcopy
# from businessCommon.dataOperator import DataOperator
# from common.configRead import read_env_yaml
# from common.caseLog import info, step, error, class_case_log
# from businessCommon.apiRe import ApiRe
#
#
# @class_case_log
# class TestGetNotes(unittest.TestCase):
#     envData = read_env_yaml()
#     userId = envData['userId']
#     sid = envData['sid']
#     host = envData['host']
#     ar = ApiRe()
#
#     def testCase13_major(self):
#         """【前置步骤新增一条回收站A用户便签数据】【前置步骤清空回收站】"""
#         step('【INIT】新增一条便签数据')
#         note_datas = DataOperator().create_notes(1, self.userId, self.sid)
#         step('【INIT】删除便签数据')
#         url = f'{self.host}/v3/notesvr/delete'
#         headers = {
#             'Content-Type': 'application/json',
#             'X-user-key': self.userId,
#             'Cookie': f"wps_sid={self.sid}"
#         }
#         note_id = str(int(time.time() * 1000)) + '_noteId'
#         body = {
#             'noteId': note_datas[0]['noteId'],
#         }
#         res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
#         # """【删除回收站】主流程"""
#         step('【INIT】删除回收站数据')
#         url = f'{self.host}/v3/notesvr/cleanrecyclebin'
#         headers = {
#             'Content-Type': 'application/json',
#             'X-user-key': self.userId,
#             'Cookie': f"wps_sid={self.sid}"
#         }
#         note_id = str(int(time.time() * 1000)) + '_noteId'
#         body = {
#             'noteIds': note_datas[0]['noteId'],
#         }
#         res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
#         print(body)
#         print(res)
#         self.assertEqual(200, res.status_code, msg='状态码校验失败')
#         expect = {
#             "responseTime": int
#         }
#         CheckTools().output_check(expect, res.json())
#         step('请求获取分组信息接口，校验数据源的正确性')
#

import unittest
import requests
from common.checkTools import CheckTools
import time
from businessCommon.dataOperator import DataOperator
from common.configRead import read_env_yaml
from common.caseLog import info, step, error, class_case_log
from businessCommon.apiRe import ApiRe
from copy import deepcopy


@class_case_log
class TestGetNotes(unittest.TestCase):
    envData = read_env_yaml()
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    def testCase13_major(self):
        """【前置步骤新增一条回收站A用户便签数据】【前置步骤清空回收站】"""
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
        """【删除回收站便签】主流程"""
        step('【INIT】删除回收站便签数据')
        url = f'{self.host}/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': note_datas[0]['noteId'],
        }
        print(headers)
        print(body)
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(res)
        print(self.ar)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        print(res.status_code)
        expect = {
            "responseTime": int
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

# url = 'http://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
# user_id = '301701083'
# headers = {
#     'Content-Type': 'application/json',
#     'X-user-key': user_id,
#     'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
# }
# note_id = str(int(time.time() * 1000)) + '_noteIds'
# body = {
#     "noteIds": ['21235gsgs']
# }
# res = requests.post(url=url, headers=headers, json=body)
# print(res.text)