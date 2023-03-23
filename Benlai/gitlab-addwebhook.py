# 添加webhook
import gitlab
import requests


def get_projectId(token, url):
    gl = gitlab.Gitlab(url=url, private_token=token)
    gl.auth()
    # 获取所有项目id
    soatest = gl.projects.get('arch/soa-test')
    project_will_add_id_list = []
    project_skip_id_list = {}
    project_cicd_id_list = []
    projects = gl.projects.list(get_all=True)
    for project in projects:
        if project.namespace['name'] == 'cicd':
            project_cicd_id_list.append('proj:{}-{}'.format(project.id, project.name))
            continue
        hooks = project.hooks.list()
        if len(hooks) > 0:
            for h in hooks:
                if h.url.startswith('https://hook.tapd.cn/45789919'):
                    if project.id not in project_skip_id_list:
                        project_skip_id_list[project.id] = []
                    project_skip_id_list[project.id].append({"name":project.name,"url":h.url})
        if project.id in project_skip_id_list:
            continue
        project_will_add_id_list.append(project.id)
    return project_will_add_id_list, project_skip_id_list, project_cicd_id_list


def add_webhook(project_id_list, token, url, webhook_url):
    header = {"PRIVATE-TOKEN": token}
    data = {"url": webhook_url, "push_events": "true", "merge_requests_events": 'True',
            "tag_push_events": 'True'}  # 参数（包括url，事件）
    for project_id in project_id_list:
        res1 = requests.post(url + '/api/v4/projects/{}/hooks'.format(project_id), headers=header, data=data)
        print(res1)

if __name__ == '__main__':
    token = '6Hx6qpnzBNyQSwRLQERz'
    url = 'https://gitlab.benlai.work/'
    webhook_url = 'https://www.tapd.cn/hook/index/62158720/7a95da04f327ae426c72d96c8d5fec4c'
    project_will_add_id_list, project_skip_id_list, project_cicd_id_list = get_projectId(token, url)
    print(project_skip_id_list)
    # add_webhook(project_will_add_id_list, token, url, webhook_url)
    # project_will_add_id_list, project_skip_id_list, project_cicd_id_list = get_projectId(token, url)
    # print(project_skip_id_list)





