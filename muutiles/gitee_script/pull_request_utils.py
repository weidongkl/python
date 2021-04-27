import requests
import json
from gitee_script import PullRequest


class CreatePullRequest(PullRequest):
    """创建pull request 请求类"""

    def __init__(self, url, data, headers):
        super(CreatePullRequest, self).__init__(url)
        self.d = data
        self.h = headers

    def create_pull_request(self):
        ret = requests.post(self.u, data=json.dumps(self.d), headers=self.h)
        re_status = {'code': ret.status_code, 'msg': ret.json()}
        return re_status
