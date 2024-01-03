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
    host = envData['host']
    ar = ApiRe()


    def testCase04_major(self):
        """【删除回收站】主流程"""
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
        # """【查看回收站下便签列表】主流程"""
        step('【STEP】请求查看回收站下便签列表的接口')
        url = f'{self.host}/v3/notesvr/user/{self.userId}/invalid/startindex/0/rows/999/notes'
        res = self.ar.get(url, sid=self.sid)
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