import unittest
import requests
import time
from businessCommon.dataOperator import DataOperator
from common.checkTools import CheckTools
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
     #
    # def tearDown(self) -> None:
    #     print('tearDown')

    def testCase01_major(self):
        """【获取首页便签】主流程"""
        # print('testcast01_major')
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        # print(note_datas)
        # case:
        step('【STEP】请求获取首页便签的接口')
        url = f'{self.host}/v3/notesvr/user/{self.userId}/home/startindex/0/rows/50/notes'
        res = self.ar.get(url, sid=self.sid)

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
                    'title': note_datas[0]['title'],
                    'summary': note_datas[0]['summary'],
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
