import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase12_major(self):
        """【恢复回收站的便签】主流程"""
        url = 'https://note-api.wps.cn/notesvr/v2/user/301701083/notes'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'wps_sid=V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db'
        }
        note_ids = str(int(time.time() * 1000)) + '_noteIds'
        data = {
            "noteIds": [note_ids]
            }
        res = requests.patch(url, json=data, headers=headers)
        self.assertEqual(206, res.status_code, msg='状态码校验失败')

        # 请求获取便签信息接口，校验数据源的正确性
        url = 'http://note-api.wps.cn/v3/notesvr/user/301701083/home/startindex/0/rows/9999/notes'
        body = {}
        res = requests.post(url=url, headers=headers, json=body)
        group_ids = []
        for item in res.json()['webNotes']:
            group_ids.append(item['noteIds'])
        self.assertIn(note_ids, group_ids)


