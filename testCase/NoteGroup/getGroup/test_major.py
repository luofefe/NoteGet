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

    def setUp(self) -> None:
        # 【前置】清空用户分组
        step("清空用户分组")
        DataOperator().clear_groups(self.userId, self.sid)

    def testcast05_major(self):
        """【获取分组】主流程"""
        step('【INIT】新增一条分组数据')
        note_datas = DataOperator().create_groups(1, self.userId, self.sid)
        step('【STEP】请求获取分组列表的接口')
        url = f'{self.host}/v3/notesvr/get/notegroup'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={self.sid}",
            'X-user-key': self.userId
        }
        body = {"excludeInValid": "true"}
        res = self.ar.post(url=url, body=body, headers= headers, sid=self.sid, user_id=self.userId)
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