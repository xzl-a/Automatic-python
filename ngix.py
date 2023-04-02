#!/usr/bin/python3
import matplotlib.pyplot as plt
nginx_file = '/var/log/nginx/access.log'
a = 1
ip = {}
with open(nginx_file) as f:
    for i in f.readlines():
        s = i.strip().split()[0]
        ip.update({s:a})
        lengh = len(ip.keys())
        if s in ip.keys():
            ip[s] = ip[s] + 1
            a = ip[s]
        else:
            ip[s] = 1
            ip = sorted(ip.items(), key=lambda e: e[1], reverse=True)
    print(ip)
    sorted_dict = sorted(ip.items(), key=lambda x: x[1], reverse=True)[:10]
    x=[]
    y=[]
    for i in sorted_dict:
        print(f"{i[0]}    {i[1]}")
        x.append(i[0])
        y.append(i[1])       
    print(x)
    plt.title('ip access')
    plt.xlabel('ip address')
    plt.ylabel('pv')
    plt.xticks(rotation=-30,fontsize=6)
# 显示每个柱状图的值
    for a, b, i in zip(x, y,range(len(x))):
        plt.text(a, b, '%.0f' % y[i], ha='center', fontsize=6)
        plt.bar(x, y)
        plt.savefig('my_plot.png')
    