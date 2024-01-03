import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase09_major(self):
        """【删除分组】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/delete/notegroup'
        user_id = '301701083'
        headers = {
            'Content-Type': 'application/json',
            'X-user-key': user_id,
            'Cookie': 'wps_sid=V02SUvT04cY988UetooXel4wKMrljbg00a8a177a0011fb97db'
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            "groupId": group_id
        }
        res = requests.post(url=url, headers=headers, json=body)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.assertIn('responseTime', res.json().keys())
        self.assertEqual(1, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))

