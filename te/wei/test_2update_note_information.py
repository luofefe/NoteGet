import unittest

import requests
import time
from businessCommon.dataOperator import DataOperator
from common.checkTools import CheckTools
import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase03_major(self):
        """【上传/更新便签信主体】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/set/noteinfo'
        user_id = '301701083'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(url)
        print(headers)
        print(body)
        print(res.status_code)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.assertIn('responseTime', res.json().keys())
        self.assertIn('infoVersion', res.json().keys())
        self.assertIn('infoUpdateTime', res.json().keys())
        self.assertEqual(3, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))
        self.assertEqual(int, type(res.json()['infoVersion']))
        self.assertEqual(int, type(res.json()['infoUpdateTime']))

        # 请求获取便签主体信息接口，校验数据源的正确性
        url = 'http://note-api.wps.cn/v3/notesvr/get/notebody'
        body = {}
        res = requests.post(url=url, headers=headers, json=body)
        group_ids = []
        for item in res.json()['noteBodies']:
            group_ids.append(item['noteId'])
        self.assertIn(note_id, group_ids)


