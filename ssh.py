#!/usr/bin/python3
import paramiko
cmd = "ls /"
task_info = "ps -aux"
# 创建客户端对象
ssh = paramiko.SSHClient()
# 接收并保存新的主机名，此外还有RejectPolicy()拒绝未知的主机名
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# hostname:目标主机地址，port:端口号，username:登录用户名，password:密码
ssh.connect(hostname="192.168.236.140", username="root", password="itnsa2023",
port=22)
# 执行命令，timeout为此次会话的超时时间，返回的是(stdin, stdout, stderr)的三元组
stdin, stdout, stderr = ssh.exec_command(cmd, timeout=20)
# 需要解码才能把返回的内容转换为正常的字符串形式
print(stdout.read().decode())
stdin, stdout, stderr = ssh.exec_command(task_info, timeout=20)
print(stdout.read().decode())