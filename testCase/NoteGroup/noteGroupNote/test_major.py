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
    groupId = envData['groupId']
    ar = ApiRe()

    def setUp(self) -> None:
        # 【前置】清空分组下便签数据
        step("清空用户分组下便签数据")
        DataOperator().clear_group_notes(self.userId, self.sid)

    def testcast08_major(self):
        """【获取分组下便签】主流程"""
        step('【INIT】新增一条分组下便签数据')
        note_datas = DataOperator().create_group_notes(1, self.userId, self.sid, self.groupId)
        step('【STEP】请求获取分组下便签的接口')
        url = f"{self.host}/v3/notesvr/web/getnotes/group"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': self.groupId,
            'startIndex': 0,
            'rows': 50
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': str,
                    'createTime': int,
                    'star': 0,
                    'remindTime': 0,
                    'remindType': 0,
                    'infoVersion': 67 ,
                    'infoUpdateTime': int,
                    'groupId': str,
                    'title': 'test',
                    'summary': 'test',
                    'thumbnail': None,
                    'contentVersion': 12,
                    'contentUpdateTime': int
                }
            ]
        }

        CheckTools().output_check(expect, res.json())