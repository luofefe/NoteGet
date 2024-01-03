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
    userId2 = envData['userId2']
    sid2 = envData['sid2']
    host = envData['host']
    ar = ApiRe()

    def testCase0301_major(self):
        # """【前置步骤新建一条便签数据】"""
        step('【INIT】新增一条便签数据')
        note_datas = DataOperator().create_notes(1, self.userId, self.sid)
        print(note_datas)
        step('【INIT】用户A重复上传/更新便签主体A--重复数据')
        url = f'{self.host}/v3/notesvr/set/noteinfo'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': self.userId,
            'Cookie': f"wps_sid={self.sid}"
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_datas[0]['noteId'],
            'star': 0,
            'remindTime': 1703009590091,
            'remindType': 1,
            'groupId': "abc"
        }
        res = self.ar.post(url=url, body=body, headers=headers, sid=self.sid, user_id=self.userId)
        self.assertEqual(412, res.status_code, msg='状态码校验失败')
        # expect = {
        #     "errorCode": -1003,
        #     "errorMsg": "content version not equal!"
        # }
        # CheckTools().output_check(expect, res.json())
        # step('请求获取分组信息接口，校验数据源的正确性')