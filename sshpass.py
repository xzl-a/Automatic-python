#!/usr/bin/python3
import subprocess
def scan_port(ip, user, passwd):
    cmd = "id"
    # try:'{CMD}'
    COMMAND = "timeout 10 sshpass -p '{PASSWD}' ssh -o StrictHostKeyChecking=no {USER}@{IP} '{CMD}' ".format(PASSWD=passwd, USER=user, IP=ip, CMD=cmd)
    print(COMMAND)
    output = subprocess.Popen(COMMAND, shell=True, stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    oerr = output.stderr.readlines()
    oout = output.stdout.readlines()
    oinfo = oerr + oout
    if len(oinfo) != 0:
        oinfo = oinfo[0].decode()
    else:
        oinfo = '未知异常.'
    if user in oinfo:
        res = "{USER}登录正常".format(USER=user)
    elif "reset" in oinfo:
        res = "没加入白名单"
    elif "Permission" in oinfo:
        res = "{USER}密码错误".format(USER=user)
    elif 'No route to host' in oinfo or ' port 22: Connection refused' in oinfo:
        res = '22端口不通'
    else:
        res = oinfo
    # print(res,'============',oinfo)
    return res
ret = scan_port("192.168.236.140","root","itnsa2023")
print(ret)