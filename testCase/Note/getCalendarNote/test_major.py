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

    # def setUp(self) -> None:
        # 【前置】清空日历下便签数据
        # step("清空用户日历下便签数据")
        # DataOperator().clear_remind_notes(self.userId, self.sid)

    def testcast08_major(self):
        """【获取分组下便签】主流程"""
        step('【INIT】新增一条日历下便签数据')
        note_datas = DataOperator().create_remind_notes(1, self.userId, self.sid)
        print(note_datas)
        step('【STEP】请求获取日历下便签数据的接口')
        url = f"{self.host}/v3/notesvr/web/getnotes/remind"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        body = {
            'remindStartTime': 1703855825,
            'remindEndTime': 1704028625,
            'startIndex': 0,
            'rows': 100
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(res.json())
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': note_datas[0]['noteId'],
                    'createTime': int,
                    'star': 0,
                    'remindTime': 1703942225,
                    'remindType': 0,
                    'infoVersion': 3 ,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': 'test',
                    'summary': 'test',
                    'thumbnail': None,
                    'contentVersion': 2,
                    'contentUpdateTime': int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())