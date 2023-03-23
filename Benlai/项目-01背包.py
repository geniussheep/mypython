import pandas as pd
import numpy as np


#0-1背包
def process1(value, weight, N, V):
    #value:价值分  weight:每个项目团队的工作时长  N：项目数  V：团队迭代周期总时长
    print('N:', N, ' V:', V)
    # dp[0~N][0~V]
    dp = [[0] * (V + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(V + 1):
            ans1 = dp[i - 1][j]
            ans2 = 0
            if j - weight[i - 1] >= 0:
                ans2 = dp[i - 1][j - weight[i - 1]] + value[i - 1]
            dp[i][j] = max(ans1, ans2)
    n = N
    v = V
    res = []
    while n > 0:
        if dp[n][v] > dp[n - 1][v]:
            print('第', n, '个物品被装入背包')
            v = v - weight[n - 1]
            res.append(1)
            #n=n-1
        else:
            print('第', n, '个物品未被装入背包')
            res.append(0)
        n = n - 1

    return dp[N][V], res


teamscore = pd.read_excel(
    '/Users/yangjing/Desktop/project/d5.xlsx')  #项目价值以及时长表格

#各组总时间（约束条件）
team = ['一气道盟', '快乐星球', '桃花岛', '水哥全球粉丝后援']
total_time = [100, 120, 80, 180]

team_time = pd.DataFrame(data={
    'team': team,
    'total_time': total_time,
})
teamprocnt = teamscore.groupby([
    'team', 'ismasterteam'
]).PO.count().reset_index().pivot(index='team',
                                  columns='ismasterteam',
                                  values='PO').reset_index()
teamprocnt.columns = ['team', 'all', 'secondary', 'master']
team_time = pd.merge(team_time, teamprocnt, how='left', on='team')
team_time_bymaster = team_time.sort_values(by='master',
                                           ascending=False)  #按照前置项目数降序
#team_time_bysecond=team_time.sort_values(by='secondary',ascending=False)
'''
逻辑：
1.分组统计01背包,约束条件为每组的总时长【自然是满足整体技术部的时长限制】
2.对于需要合作的项目，存在依赖关系的，必须前置放入背包中，后置组才可以进入背包
3.因为依赖关系，优先选取前置项目比较多的组进行背包统计
4. ismasterteam ,-1:单独团队,1:主导团队,0:配合团队
'''

project = pd.DataFrame()
tapd_team = pd.DataFrame()
for index, tt in team_time_bymaster.iterrows():
    teamname = tt.team
    print('teamname:', teamname)
    if len(project) == 0:
        t_team = teamscore.query('team==@teamname and ismasterteam in (-1,1)')
        V = tt.total_time
        second_team = teamscore.query('team==@teamname and ismasterteam ==0')
    else:
        firstpro = project.query('isInBag==1 & ismasterteam==1 ')
        if len(firstpro) == 0:
            t_team = teamscore.query(
                'team==@teamname and ismasterteam in (-1,1)')
            V = tt.total_time
            second_team = teamscore.query(
                'team==@teamname and ismasterteam ==0')
        else:
            tapdID = list(firstpro.tapdID.unique())  ###
            t_team = teamscore.query(
                'team==@teamname & tapdID not in @tapdID and ismasterteam in (-1,1)'
            )
            second_team = teamscore.query(
                'team==@teamname and ismasterteam ==0 and tapdID not in @tapdID'
            )
            tapd_team = teamscore.query('team==@teamname & tapdID in @tapdID')
            tapd_team['isInBag'] = 1
            V = tt.total_time - sum(tapd_team.time)

    N = len(t_team)
    value = list(t_team.score)
    weight = list(t_team.time)
    print('N:', N, ' V:', V)
    dp, res = process1(value, weight, N, V)
    res.reverse()
    t_team.loc[:,'isInBag'] = res
    second_team['isInBag'] = 0
    project = pd.concat([project, t_team])
    project = pd.concat([project, second_team])
    if len(tapd_team) > 0:
        project = pd.concat([project, tapd_team])
        tapd_team = pd.DataFrame()

#统计各组数据
teamstat_total = project.groupby(['team']).agg({
    'score': np.sum,
    'time': np.sum
}).reset_index()
teamstat_inbag = project.query('isInBag==1').groupby(['team']).agg({
    'score':
    np.sum,
    'time':
    np.sum
}).reset_index()
teamstat = pd.merge(teamstat_total,
                    teamstat_inbag,
                    how='left',
                    on='team',
                    suffixes=['_total', '_inbag'])
teamstat[
    'score_per'] = teamstat['score_inbag'] * 100.0 / teamstat['score_total']
teamstat['time_per'] = teamstat['time_inbag'] * 100.0 / teamstat['time_total']

#导出数据
with pd.ExcelWriter(
        '/Users/yangjing/Desktop/project//d5-result.xlsx') as writer:
    project.to_excel(writer, sheet_name='project', index=False)
    teamstat.to_excel(writer, sheet_name='teamstat')
