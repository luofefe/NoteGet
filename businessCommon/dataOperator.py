import time
import requests


class DataOperator:

    @staticmethod
    def create_notes(num, user_id, sid, headers=None):
        """
        批量新增便签
        :param num:
        :param user_id:
        :param sid:
        :return:
        """
        notes_info = []
        for i in range(num):
            note_info = {}
            # 前置 便签主体
            url = "https://note-api.wps.cn/notesvr/set/noteinfo"
            if headers is None:
                headers = {
                    'Content-Type': 'application/json',
                    'Cookie': f"wps_sid={sid}",
                    'X-user-key': user_id
                }
            else:
                pass
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id,
                "star": 0
            }
            res = requests.post(url=url, headers=headers, json=body)
            info_version = res.json()['infoVersion']
            for k, v in body.items():
                note_info[k] = v

            # 前置 便签内容
            url = "https://note-api.wps.cn/notesvr/set/notecontent"
            body = {
                "noteId": note_id,
                "thumbnail": None,
                "title": "6MC5h1NpfG9+If6c2eE7UA==",
                "summary": "Kf7eO5uEBcJILXCBYt0skg==",
                "body": "oJHQnXPFCHZgYZXeiGs0cw==",
                "localContentVersion": info_version,
                "bodyType": 0
            }
            requests.post(url=url, headers=headers, json=body)
            for k, v in body.items():
                note_info[k] = v
            notes_info.append(note_info)

        return notes_info


    @staticmethod
    def create_groups(num, user_id, sid):  # 创建大量分组
        """"
        批量创建分组
        :param num:
        :param user_id:
        :param sid:
        :return:
        """
        notes_info = []
        for i in range(num):
            note_info = {}
            # """【前置步骤创建分组】"""
            url = 'http://note-api.wps.cn/v3/notesvr/set/notegroup'
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f"wps_sid={sid}",
                'X-user-key': user_id
            }
            group_id = str(int(time.time() * 1000)) + '_groupId'
            body = {
                'groupId': group_id,
                'groupName': '分组列表A',
                'order': i
            }
            res = requests.post(url=url, headers=headers, json=body)
            if res.status_code == 200:
                for k, v in body.items():
                    note_info[k] = v
                notes_info.append(note_info)
            else:
                print(f"创建出错{i}: {res.text}")

        return notes_info

    @staticmethod
    def clear_notes(user_id, sid):  # 清空便签
        """
        清空用户所有便签数据
        :return:
        """
        # 获取用户下所有的便签信息
        url = f"https://note-api.wps.cn/notesvr/v2/user/{user_id}/home/startindex/0/rows/9999/notes"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={sid}",
            'X-user-key': user_id
        }
        res = requests.get(url=url, headers=headers)

        # 删除所有便签
        d_url = 'https://note-api.wps.cn/v3/notesvr/delete'
        for note in res.json()['webNotes']:
            note_id = note['noteId']
            body = {
                'noteId': note_id
            }
            requests.post(url=d_url, headers=headers, json=body)

        # 清空回收站
        clear_url = 'https://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
        body = {
            'noteIds': -1
        }
        requests.post(url=clear_url, headers=headers, json=body)

    @staticmethod
    def clear_groups(user_id, sid):  # 清空分组
        """
        清空分组
        :param user_id: 用户ID
        :param sid: session id
        :return: 删除操作的结果
        """
        # 获取用户获取分组列表
        url = f"http://note-api.wps.cn/v3/notesvr/get/notegroup"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={sid}",
            'X-user-key': user_id
        }
        body = {
            'excludeInValid': True
        }
        res = requests.get(url=url, headers=headers, json=body)
        data = res.json()
        note_groups = data['noteGroups']
        # print(res.json())
        # 删除所有分组
        s_url = 'https://note-api.wps.cn/notesvr/delete/notegroup'
        for group in note_groups:
            group_id = group['groupId']
            body = {
                'groupId': group_id,
            }
            delete_response = requests.post(s_url, headers=headers, json=body)
            delete_data = delete_response.json()
            print(s_url)
            print(headers)
            print(body)
            print(delete_response.status_code)

            print(delete_data)

    @staticmethod
    def create_remind_notes(num, user_id, sid, headers=None):  # 新增日历下便签
        """
          批量新增日历下便签
          :param num:
          :param user_id:
          :param sid:
          :param remindStartTime: 便签提醒的起始时间
                 remindEndTime: 便签提醒的结束时间
          :return:
          """
        notes_info = []
        for i in range(num):
            note_info = {}
            # 前置 便签主体
            url = "https://note-api.wps.cn/notesvr/set/noteinfo"
            if headers is None:
                headers = {
                    'Content-Type': 'application/json',
                    'Cookie': f"wps_sid={sid}",
                    'X-user-key': user_id
                }
            else:
                pass
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id,
                "star": 0,
                "remindTime": 1703942225,
                "remindType": 0
            }
            res = requests.post(url=url, headers=headers, json=body)
            info_version = res.json()['infoVersion']
            for k, v in body.items():
                note_info[k] = v

            # 前置 便签内容
            url = "https://note-api.wps.cn/notesvr/set/notecontent"
            body = {
                "noteId": "abc@@@",
                "title":"test",
                "summary": "test",
                "body": "test",
                "localContentVersion": "1",
                "BodyType":0
            }
            requests.post(url=url, headers=headers, json=body)
            for k, v in body.items():
                note_info[k] = v
            notes_info.append(note_info)

        return notes_info


    @staticmethod
    def clear_remind_notes(user_id, sid):  # 清空日历便签
        """
        清空日历便签
        :param user_id: 用户ID
        :param sid: session id
        :return: 清空日历便签的结果
        """
        # 获取用户查看日历下便签
        h_url = f"http://note-api.wps.cn/v3/notesvr/web/getnotes/remind"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={sid}",
            'X-user-key': user_id
        }
        body = {
            "remindStartTime": 1703855825,
            "remindEndTime": 1704028625,
            "startIndex":0,
            "rows": 100
        }
        res = requests.post(url=h_url, headers=headers, json=body)
        print(res.json())
        # print(h_url)
        # print(headers)
        # print(body)
        # print(res.status_code)

        # 删除所有日历便签
        d_url = 'http://note-api.wps.cn/v3/notesvr/delete'
        for note in res.json()['webNotes']:
            note_id = note['noteId']
            body = {
                'noteId': note_id
            }
        requests.post(url=d_url, headers=headers, json=body)

        # 清空回收站
        clear_url = 'http://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
        body = {
            'noteId': -1
        }
        requests.post(url=clear_url, headers=headers, json=body)

    @staticmethod
    def create_group_notes(num, user_id, sid, group_id, headers=None):  # 新增分组下便签
        """
        批量新增分组下便签
        :param num:
        :param user_id:
        :param sid:
        :param group_id: 分组ID
        :return:
        """
        notes_info = []
        for i in range(num):
            note_info = {}
            # """【前置步骤上传/更新分组下便签信息主体】"""
            url_p = 'http://note-api.wps.cn/v3/notesvr/set/noteinfo'
            if headers is None:
                headers = {
                    'Content-Type': 'application/json',
                    'Cookie': f"wps_sid={sid}",
                    'X-user-key': user_id
                }
            else:
                pass
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                'noteId': note_id,
                'star': 0,
                'groupId': group_id  # 添加分组ID'
            }
            res = requests.post(url=url_p, headers=headers, json=body)
            info_version = res.json()['infoVersion']
            for k, v in body.items():
                note_info[k] = v
            notes_info.append(note_info)
            print(url_p)
            print(headers)
            print(body)
            print(res.status_code)
        return notes_info

    @staticmethod
    def clear_group_notes(user_id, sid):  # 清空分组便签
        """
        清空分组便签
        :param user_id: 用户ID
        :param sid: session id
        :return: 清空分组便签的结果
        """
        # 获取用户分组下便签
        f_url = f"http://note-api.wps.cn/v3/notesvr/web/getnotes/group"
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f"wps_sid={sid}",
            'X-user-key': user_id
        }
        group_id = str(int(time.time() * 1000)) + '_groupId'
        body = {
            'groupId': group_id,
            'startIndex': 0,
            'rows': 50
        }
        res = requests.post(url=f_url, headers=headers, json=body)
        res_json = res.json()
        # print(f_url)
        # print(headers)
        # print(body)
        # print(res.status_code)
        print(res_json)

        # 删除所有便签
        d_url = 'http://note-api.wps.cn/v3/notesvr/delete'
        for note in res.json()['webNotes']:
            note_id = note['noteId']
            body = {
                'noteId': note_id
            }
        requests.post(url=d_url, headers=headers, json=body)

        # 清空回收站
        clear_url = 'http://note-api.wps.cn/v3/notesvr/cleanrecyclebin'
        body = {
            'noteId': -1
        }
        requests.post(url=clear_url, headers=headers, json=body)


if __name__ == '__main__':
    # r = DataOperator().create_notes(1, user_id='301701083', sid='V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db')
    # r = DataOperator().clear_group_notes(user_id='301701083',sid='V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db',)
    # r = DataOperator().create_group_notes(1, user_id='301701083', sid='V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db')
    # r = DataOperator().clear_remind_notes(user_id='301701083', sid='V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db')
    r = DataOperator().create_remind_notes(1, user_id='301701083', sid='V02SPoTrEtftKaSfjzSmaJyWyprmGzg00a34a6680011fb97db')
    print(r)
