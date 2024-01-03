import unittest


class CheckTools(unittest.TestCase):
    def output_check(self, expect, actual):
        """
        接口返回体断言的通用方法
        :param expect:用户需要提供接口期望值的数据，格式参考{
            'responseTime': int,
            'webNotes': [
                {
                    'noteId': 'new_note',
                    'createTime': int,
                    'star': 0,
                    'remindTime': None,
                    'remindType': None,
                    'infoVersion': 1,
                    'infoUpdateTime': int,
                    'groupId': None,
                    'title': 'test',
                    'summary': 'test',
                    'thumbnail': None,
                    'contentVersion': 1,
                    'contentUpdateTime': int
                }
            ]
        }  注：动态值只需要传递类型即可。
        :param actual: 接口返回体json类型
        :return: None
        """
        self.assertEqual(len(expect.keys()), len(actual.keys()), msg='断言的字段数量未对齐')
        for k, v in expect.items():
            self.assertIn(k, actual.keys(), msg=f'{k}字段不存在于返回体中')
            if isinstance(v, list):
                self.assertEqual(len(v), len(actual[k]))
                for i in range(len(v)):
                    if isinstance(v[i], type):
                        self.assertEqual(v[i], type(actual[k][i]), msg=f'{k}列表字段{v[i]}元素值类型断言失败')
                    elif isinstance(v[i], dict):
                        self.output_check(v[i], actual[k][i])
                    else:
                        self.assertEqual(v[i], actual[k][i], msg=f'{k}列表字段{v[i]}元素值断言失败')
                pass
            elif isinstance(v, dict):
                pass
            elif isinstance(v, type):
                self.assertEqual(v, type(actual[k]), msg=f'{k}字段类型断言失败')
            else:
                self.assertEqual(type(v), type(actual[k]), msg=f'{k}字段类型断言失败')
                self.assertEqual(v, actual[k], msg=f'{k}字段值不正确')


if __name__ == '__main__':
    # act_body = {'responseTime': 24, 'webNotes': [
    #     {'noteId': '51ab90317e69859150fb8fcf7ce3c965', 'createTime': 1701845145239, 'star': 0, 'remindTime': 0,
    #      'remindType': 0, 'infoVersion': 1, 'infoUpdateTime': 1701845145239, 'groupId': None,
    #      'title': '6MC5h1NpfG9+If6c2eE7UA==', 'summary': 'Kf7eO5uEBcJILXCBYt0skg==', 'thumbnail': None,
    #      'contentVersion': 6, 'contentUpdateTime': 1701852888720}]}
    # expect_body = {
    #     'responseTime': int,
    #     'webNotes': [
    #         {
    #             'noteId': 'new_note',
    #             'createTime': int,
    #             'star': 0,
    #             'remindTime': None,
    #             'remindType': None,
    #             'infoVersion': 1,
    #             'infoUpdateTime': int,
    #             'groupId': None,
    #             'title': 'test',
    #             'summary': 'test',
    #             'thumbnail': None,
    #             'contentVersion': 1,
    #             'contentUpdateTime': int
    #         }
    #     ]
    # }
    act_body = {'noteId': '51ab90317e69859150fb8fcf7ce3c965', 'createTime': 1701845145239, 'star': 0, 'remindTime': 0,
                'remindType': 0, 'infoVersion': 1, 'infoUpdateTime': 1701845145239, 'groupId': None,
                'title': '6MC5h1NpfG9+If6c2eE7UA==', 'summary': 'Kf7eO5uEBcJILXCBYt0skg==', 'thumbnail': None,
                'contentVersion': 6, 'contentUpdateTime': 1701852888720}
    expect_body = {
        'noteId': 'new_note',
        'createTime': int,
        'star': 0,
        'remindTime': None,
        'remindType': None,
        'infoVersion': 1,
        'infoUpdateTime': int,
        'groupId': None,
        'title': 'test',
        'summary': 'test',
        'thumbnail': None,
        'contentVersion': 1,
        'contentUpdateTime': int
    }
    CheckTools().output_check(expect_body, act_body)