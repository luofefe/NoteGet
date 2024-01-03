import requests
from common.caseLog import info, error


class ApiRe:
    @staticmethod
    def get(url, sid, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f"wps_sid={sid}"
            }
        info(f're url: {url}')
        info(f're headers: {headers}')
        try:
            res = requests.get(url=url, headers=headers, timeout=3)
        except TimeoutError:
            error('requests Timeout')
            return 'requests Timeout'

        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res

    @staticmethod
    def post(url, body, sid, user_id, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f"wps_sid={sid}",
                'X-user-key': user_id
            }
        info(f're url: {url}')
        info(f're headers: {headers}')
        info(f're headers: {body}')
        try:
            res = requests.post(url=url, headers=headers, json=body, timeout=3)
        except TimeoutError:
            error('requests Timeout')
            return 'requests Timeout'

        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res

    @staticmethod
    def patch(url, body, sid, user_id, headers=None):
        if headers is None:
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f"wps_sid={sid}",
                'X-user-key': user_id
            }
        info(f're url: {url}')
        info(f're headers: {headers}')
        info(f're headers: {body}')
        try:
            res = requests.patch(url=url, headers=headers, json=body, timeout=3)
        except TimeoutError:
            error('requests Timeout')
            return 'requests Timeout'

        info(f'res code: {res.status_code}')
        info(f'res body: {res.text}')
        return res
