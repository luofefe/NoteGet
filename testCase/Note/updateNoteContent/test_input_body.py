import time
import unittest

from parameterized import parameterized

from businessCommon.apiRe import ApiRe
from common.caseLog import step, class_case_log
from common.checkTools import CheckTools
from common.configRead import read_env_yaml, read_api_yaml


@class_case_log
class updateNoteContentInput(unittest.TestCase):
    envData = read_env_yaml()  # 小驼峰  工具类对象的实例化、环境变量、【base】
    apiData = read_api_yaml()['updateNoteContent']
    userId = envData['userId']
    sid = envData['sid']
    host = envData['host']
    ar = ApiRe()

    # @parameterized.expand(apiData['mustKeys'])
    @parameterized.expand([[{'key': 'noteId', 'errorCode': -7}], [{'key': 'title', 'errorCode': -7}], [{'key': 'summary', 'errorCode': -7}]
                           , [{'key': 'body', 'errorCode': -7}], [{'key': 'localContentVersion', 'errorCode': -7}], [{'key': 'BodyType', 'errorCode': -7}]])
    def testCase01_input_must_key(self, dic):
        """【更新便签内容】必填字段缺失"""
        step('请求更新便签内容接口')
        url = f'{self.host}{self.apiData["path"]}'
        note_id = str(int(time.time() * 1000)) + '_noteId'
        body = {
            'noteId': note_id,
            'title': 'test',
            'summary': 'test',
            'body': 'test',
            'localContentVersion': '4',
            'BodyType': 0
        }
        body.pop(dic['key'])
        res = self.ar.post(url=url, body=body, sid=self.sid, user_id=self.userId)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
        expect = {
            'errorCode': dic['errorCode'],
            'errorMsg': "参数不合法！"
        }
        CheckTools().output_check(expect, res.json())
        step('请求获取分组信息接口，校验数据源的正确性')