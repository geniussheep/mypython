# 检查所有源码的master分支
from datetime import datetime

import gitlab
import requests


def get_project(token, url):
    gl = gitlab.Gitlab(url=url, private_token=token)
    gl.auth()
    # 获取所有项目id
    # test_pro = gl.projects.get('ApiService/Benlai.Notify')
    # for pb in test_pro.branches.list(as_list=False):
    #     if 'master' == pb.name.strip(' ').lower():
    #         is_has_master = True
    #         master_last_commit_date = pb.commit['committed_date']
    #         continue
    #     if 'release' == pb.name.strip(' ').lower():
    #         is_has_release = True
    #         release_last_commit_date = pb.commit['committed_date']
    #         continue
    project_has_master_list = []
    project_old_master_list = []
    project_no_master_list = []
    projects = gl.projects.list(get_all=True)
    for project in projects:
        if project.namespace['name'].strip(' ').lower() in ['cicd', 'arch', 'java', 'ops', 'test', 'devops', 'jenkins',
                                                            'architecture', 'golang', 'ymir', 'epec', 'archclients',
                                                            'easylife', 'o2oerp', 'o2o-api', 'skywalking','pods',
                                                            'blprivacyframeworks','bkit','csharp']:
            continue
        is_has_master = False
        is_has_release = False
        is_old_master = False
        master_last_commit_date = ''
        release_last_commit_date = ''
        for pb in project.branches.list(as_list=False):
            if 'master' == pb.name.strip(' ').lower():
                is_has_master = True
                master_last_commit_date = pb.commit['committed_date']
                continue
            if 'release' == pb.name.strip(' ').lower():
                is_has_release = True
                release_last_commit_date = pb.commit['committed_date']
                continue
            if is_has_master and is_has_release:
                break
        if not (is_has_master and is_has_release):
            project_no_master_list.append({"name": project.name, "url": project.web_url,
                                           "group": project.namespace['name'].strip(' ').lower(),
                                           "is_has_master": is_has_master,
                                           "is_has_release": is_has_release})
            continue
        m_commit_date = datetime.strptime(master_last_commit_date, '%Y-%m-%dT%H:%M:%S.%f%z')
        r_commit_date = datetime.strptime(release_last_commit_date, '%Y-%m-%dT%H:%M:%S.%f%z')
        duringtime = r_commit_date - m_commit_date
        master_last_commit_date = master_last_commit_date.replace("T", " ").replace(".000+08:00", "")
        release_last_commit_date = release_last_commit_date.replace("T", " ").replace(".000+08:00", "")
        if abs(duringtime.days) > 6:
            is_old_master = True
        if is_old_master and is_has_release:
            project_old_master_list.append({"name": project.name, "url": project.web_url,
                                            "group": project.namespace['name'].strip(' ').lower(),
                                            "master_last_commit": master_last_commit_date,
                                            "release_last_commit": release_last_commit_date,
                                            "during_day": duringtime.days})
            continue
        if is_has_master and is_has_release:
            project_has_master_list.append({"name": project.name, "url": project.web_url,
                                            "group": project.namespace['name'].strip(' ').lower(),
                                            "master_last_commit": master_last_commit_date,
                                            "release_last_commit": release_last_commit_date,
                                            "during_day": duringtime.days})
            continue
    return project_has_master_list, project_old_master_list, project_no_master_list


if __name__ == '__main__':
    token = '6Hx6qpnzBNyQSwRLQERz'
    url = 'https://gitlab.benlai.work/'
    project_has_master_list, project_old_master_list, project_no_master_list = get_project(token, url)

    print(f"代码库名称\tGit地址\t所属组\trelease最后提交时间\tmaster最后提交时间\tmaster过时天数")
    for phm in project_has_master_list:
        print(
            f"{phm['name']}\t{phm['url']}\t{phm['group']}\t{phm['release_last_commit']}\t{phm['master_last_commit']}\t{phm['during_day']}")
    print(f"\n过时代码库名称\tGit地址\t所属组\trelease最后提交时间\tmaster最后提交时间\tmaster过时天数")
    for phm in project_old_master_list:
        print(
            f"{phm['name']}\t{phm['url']}\t{phm['group']}\t{phm['release_last_commit']}\t{phm['master_last_commit']}\t{phm['during_day']}")
    print(f"\n缺失代码库名称\tGit地址\t所属组\trelease是否存在\tmaster是否存在")
    for phm in project_no_master_list:
        print(f"{phm['name']}\t{phm['url']}\t{phm['group']}\t{phm['is_has_release']}\t{phm['is_has_master']}")
