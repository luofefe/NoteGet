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

    def testCase05_major(self):
        """【恢复回收站便签】主流程"""
        step('【INIT】恢复回收站便签数据')
        url = f'{self.host}/notesvr/v2/user/301701083/notes'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteIds': [note_id],
        }
        res = self.ar.patch(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        print(res.text)
        self.assertEqual(206, res.status_code, msg='状态码校验失败')
        # expect = {
        #     'note_id': '1703316761631_noteId'
        # }
        # CheckTools().output_check(expect, res.json())
        # step('请求获取分组信息接口，校验数据源的正确性')


