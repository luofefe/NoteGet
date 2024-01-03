import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase13_major(self):
        """【删除/清空回收站便签】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
        user_id = '301701083'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
        }
        note_id = str(int(time.time() * 1000)) + '_noteIds'
        body = {
            "noteIds": [-1]
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res.status_code)
        print(res.text)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.assertIn('responseTime', res.json().keys())
        self.assertEqual(1, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))

