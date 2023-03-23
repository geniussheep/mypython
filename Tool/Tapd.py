import requests

for x in range(601):
    r =  requests.get('https://api.tapd.cn/stories?workspace_id=68246462&id=1168246462001014090', headers = {'Authorization':'Basic dzBWa20xQnk6NDk0OUIzNzEtMDkwNS0wNDAwLUFDNEYtQTNEOTQ0ODYzNTJF'})
    print(f'{x} -- {r.json()}')
