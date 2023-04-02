#!/usr/bin/python3
import os,traceback

def ping_ip2 (ip_str):
    try:
        # print(cmd)
        response = os.system("ping -c {} {}".format(5, ip_str))
        if response == 0:
            print(ip_str, 'is up!')
        else:
            print(ip_str, 'is down!')
    
    except Exception as e:
        print(traceback.format_exc())

pingip="192.168.80.140"

pingkey = ping_ip2(pingip)
