import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase11_major(self):
        """【查看回收站下便签列表】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/user/301701083/invalid/startindex/0/rows/10/notes'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
        }
        body = {
            "startIndex": 1,
            "rows": 0
            }
        res = requests.get(url=url, headers=headers, json=body)
        print(res)
        print(url)
        print(headers)
        print(body)
        print(res.status_code)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.assertIn('responseTime', res.json().keys())
        self.assertIn('webNotes', res.json().keys())
        self.assertEqual(2, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))
        self.assertEqual(list, type(res.json()['webNotes']))
