import time
import unittest

import requests


class TestCreatePro(unittest.TestCase):
    def testCase05_major(self):
        """【删除便签  软删除】主流程"""
        url = 'http://note-api.wps.cn/v3/notesvr/delete'
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
        # print(res.status_code)
        # print(res.text)
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.assertIn('responseTime', res.json().keys())
        self.assertEqual(1, len(res.json().keys()))
        self.assertEqual(int, type(res.json()['responseTime']))

        # # 请求查看回收站下便签列表信息接口，校验数据源的正确性
        url = 'http://note-api.wps.cn/v3/notesvr/user/301701083/invalid/startindex/0/rows/9999/notes'
        body = {}
        res = requests.post(url=url, headers=headers, json=body)
        group_ids = []
        for item in res.json()['webNotes']:
            group_ids.append(item['noteId'])
        self.assertIn(note_id, group_ids)

