import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase04_major(self):
        """【获取便签内容】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/get/notebody'
        user_id = '301701083'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
        }
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            "noteIds": ["note_id"]
        }
        res = requests.post(url=url, headers=headers, json=body)
        print(res)
        print(headers)
        print(body)

        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        print(res.status_code)
        self.assertIn('responseTime', res.json().keys())
        self.assertIn('noteBodies', res.json().keys())
        self.assertEqual(2, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))
        self.assertEqual(list, type(res.json()['noteBodies']))