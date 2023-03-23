import requests
import torch
import numpy


rt_app_list = []
rb_app_list = []

rb = requests.get("http://localhost:8081/config/changes")
if rb.status_code == requests.codes.ok:
    rb_app_list = sorted(set([int(r["app_id"]) for r in rb.json()]))

rt = requests.get("http://localhost:8080/config/changes")
if rt.status_code == requests.codes.ok:
    # print(result.json())
    # print("\r\n".join(str(s) + ",trunk" for s in sorted(set([int(r["app_id"]) for r in rt.json()]))))
    rt_app_list = sorted(set([int(r["app_id"]) for r in rt.json()]))

branch = sorted(list(set(rb_app_list).difference(set(rt_app_list))))
trunk = sorted(list(set(rt_app_list).difference(set(rb_app_list))))
all = sorted(list(set(rb_app_list).intersection(set(rt_app_list))))

print("\r\n".join(str(b) + ",branch" for b in branch))
print("\r\n".join(str(t) + ",trunk" for t in trunk))
print("\r\n".join(str(a) + ",branch|trunk" for a in all))


