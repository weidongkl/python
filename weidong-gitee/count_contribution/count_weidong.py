import requests
import json

id = "weidongkl"
url = "https://gitee.com/weidongkl/contribution_timeline?url=%2Fweidongkl%2Fcontribution_timeline&scope=my&day=&start_date=&end_date=&year=&limit=50"
gitee_get = requests.get(url)
rt = gitee_get.text
print(gitee_get.status_code)
# print(rt)
d = json.loads(rt)
count = 1
count_pr = 1
count_issues = 1
for i in d:
    # if count < 0:
    #     break
    # print(i["action"])
    # print(i["type"])
    if i["action"] == "created":
        if i["type"] == "pull_request":
            # count_pr += 1
            print("id:{id} pr:https://gitee.com{path} title:{title} createdtime:{created}".format(id=count_pr,
                                                                                                  path=i["target"][
                                                                                                      "path"],
                                                                                                  title=i["target"][
                                                                                                      "title"],
                                                                                                  created=i[
                                                                                                      "created_at"]))
            count_pr += 1
            count += 1
        elif i["type"] == "issue":
            print("id:{id} issues:https://gitee.com{path} title:{title} createdtime:{created}".format(id=count_issues,
                                                                                                      path=i["target"][
                                                                                                          "path"],
                                                                                                      title=
                                                                                                      i["target"][
                                                                                                          "title"],
                                                                                                      created=i[
                                                                                                          "created_at"]))
            count_issues += 1
            count += 1

print(count)


def get_pr_status(url):
    ro = requests.get(url)
    d = json.loads(ro.text)
    return d['state']


def get_issues_status(url):
    pass

