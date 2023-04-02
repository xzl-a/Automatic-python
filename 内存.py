#!/usr/bin/python3
import psutil
def mem_use():
    print('内存信息:')
    mem=psutil.virtual_memory()
    #换算为MB
    memtotal=mem.total/1024/1024
    memused=mem.used/1024/1024
    mem_percent=str(mem.used/mem.total*100)+'%'
    print('%.3fMB'%memused)
    print('%.3fMB'%memtotal)
    print(mem_percent)
mem_use()