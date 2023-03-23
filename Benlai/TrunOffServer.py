#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

proc_conn_file = open("/Users/sheep.yang/Documents/Benlai/proc_conn.txt", "r")

proc_conn_file_result = open("/Users/sheep.yang/Documents/Benlai/proc_conn_result.txt", "w+")

content_line_list = proc_conn_file.readlines()

result = {}
is_start_proc = False
is_start_netstat = False
ip = ""

for line in content_line_list:
    server_pattern = r"( +CHANGED +\| +rc)"
    if re.search(server_pattern, line, re.M | re.I):
        ip_pattern = r"((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)"
        curr_ip = re.search(ip_pattern, line).group(0)
        if ip != curr_ip:
            ip = curr_ip
            result[ip] = {}
            is_start_netstat = False
            is_start_proc = False
        continue
    proc_pattern = r"(UID +PID +PPID +C)+"
    netstat_pattern = r"(State +PID/Program name)+"
    if re.search(proc_pattern, line, re.M | re.I):
        is_start_netstat = False
        is_start_proc = True
        continue
    if re.search(netstat_pattern, line, re.M | re.I):
        is_start_netstat = True
        is_start_proc = False
        continue
    if is_start_proc:
        proc_list = re.findall(r"\S+", line)
        if len(proc_list) < 14:
            continue
        print(" ip:%s, procList: ", ip, proc_list)
        result[ip][proc_list[3]] = {"proc": ' '.join(map(str, proc_list[14:])), "netstat": []}
    if is_start_netstat and re.search(r"(ESTABLISHED)", line):
        netstat_list = re.findall(r"\S+", line)
        if len(netstat_list) < 7:
            continue
        print(" ip:%s, netstat: ", ip, netstat_list)
        tmp = netstat_list[6].split("/")
        if len(tmp) >= 2:
            if tmp[0] in result[ip]:
                result[ip][tmp[0]]["netstat"].append("\r\n\t\t\t{}->{}".format(netstat_list[3], netstat_list[4]))
            else :
                result[ip][tmp[0]] = {"proc": "", "netstat": ["\r\n\t\t\t{}->{}".format(netstat_list[3], netstat_list[4])]}

resultstr = ""
for ip, p_list in result.items():
    resultstr += "\r\n{0}\r\n".format(ip)
    for pid, proc in p_list.items():
        if len(proc["netstat"]) > 0:
            resultstr += "\tpid：{0}\r\n \t\tproc: {1}\r\n \t\tnetstat: {2}\r\n"\
                .format(pid, proc["proc"],"".join(map(str, proc["netstat"])))
print(resultstr)
proc_conn_file_result.write(resultstr)
proc_conn_file_result.close()


