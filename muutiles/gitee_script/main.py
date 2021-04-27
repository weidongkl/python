import logging
from gitee_script.pull_request_utils import CreatePullRequest
from gitee_script.config import PULL_REQUEST_URL, PULL_REQUEST_PARAMETERS

logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    for i in PULL_REQUEST_PARAMETERS:
        u = PULL_REQUEST_URL.format(i['dst'], i['dstrepo'])
        logging.debug(u)
        d = {
            'access_token': i['access_token'],
            'title': i['title'],
            'head': i['srcbranch'],
            'base': i['dstbranch'],
            'body': i['body']
        }
        logging.debug(d)
        h = {'Content-Type': i['Content-Type']}
        logging.debug(h)
        test = CreatePullRequest(u, d, h)
        re = test.create_pull_request()
        logging.debug(re)
        if re['code'] == 201:
            logging.info('create {}\'s pull reuest success'.format(u))
            logging.debug(re['msg'])
        else:
            logging.error(re)
        logging.info('https://gitee.com/src-openeuler/{0}/pulls/1'.format(i['dstrepo']))