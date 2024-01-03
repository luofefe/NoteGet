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
class GetNotePageMajor(unittest.TestCase):   # 大驼峰命名
    envData = read_env_yaml()    # 小驼峰  工具类对象的实例化、环境变量、【base】
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    def setUp(self):
        # 【前置】清空用户便签数据
        step("清空用户便签数据")
        DataOperator().clear_notes(self.userId, self.sid)

    def testCase01_major(self):
        # """【获取首页便签】主流程"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
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