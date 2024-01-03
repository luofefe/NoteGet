import unittest
import requests
from common.checkTools import CheckTools
import time
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
    remindStartTime = envData['remindStartTime']
    remindEndTime = envData['remindEndTime']

    def setUp(self) -> None:
        # 【前置】清空用户日历下便签
        step("清空用户便签数据")
        DataOperator().clear_remind_notes(self.userId, self.sid)

    def testcast01_major(self):
        # """【前置步骤新建日历便签】"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_remind_notes(1, self.userId, self.sid)
        # case:【获取日历下便签】
        step('【STEP】请求获取日历下便签的接口')
        url = f'{self.host}/v3/notesvr/web/getnotes/remind'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'remindStartTime': 1111111111111,
            'remindEndTime': 5633008085000,
            'startIndex':  0,
            'rows': 0
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.json())

        expect = {
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': note_datas[0]['noteId'],
                    'createTime': int,
                    'star': 0,
                    'remindTime': 0,
                    'remindType': 0,
                    'infoVersion': 1,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': 'test',
                    'summary': 'test',
                    'thumbnail': None,
                    'contentVersion': 1,
                    'contentUpdateTime': int
                }
            ]
        }
        CheckTools().output_check(expect, res.json())

    def test02(self):
        print('test02')
        act_body = {'responseTime': 0, 'webNotes': [
            {'noteId': '1702108365485_noteId', 'createTime': 1702108365873, 'star': 0, 'remindTime': 0,
             'remindType': 0, 'infoVersion': 1, 'infoUpdateTime': 1702108365873, 'groupId': None,
             'title': 'test', 'summary': 'test', 'thumbnail': None, 'contentVersion': 1,
             'contentUpdateTime': 1702108365873}]}

        expect_body = {
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': '1702108365485_noteId',
                    'createTime': int,
                    'star': 0,
                    'remindTime': 0,
                    'remindType': 0,
                    'infoVersion': 1,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': 'test',
                    'summary': 'test',
                    'thumbnail': None,
                    'contentVersion': 1,
                    'contentUpdateTime': int
                }
            ]
        }

        CheckTools().output_check(expect_body, act_body)
