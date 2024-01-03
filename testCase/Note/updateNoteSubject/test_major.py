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
        """【上传/更新便签信息主体】主流程"""
        step('【INIT】上传/更新便签信息主体数据')
        url = f'{self.host}/v3/notesvr/set/noteinfo'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        expect = {
            "responseTime": int,
            "infoVersion": int,
            "infoUpdateTime": int
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')


