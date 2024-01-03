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

    def setUp(self):
        # 【前置】清空用户便签数据
        step("清空用户便签数据")
        DataOperator().clear_notes(self.userId, self.sid)

    def testCase04_major(self):
        """【获取便签内容】主流程"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        print(note_datas)
        step('【STEP】请求获取便签内容的接口')
        url = f'{self.host}/v3/notesvr/get/notebody'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        note_ids = str(int(time.time() * 1000)) + '_noteIds'
        body = {
            # "noteIds": note_datas[0]["noteId"]
            "noteIds": ["1703265154611_noteId"]
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(res.json())
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