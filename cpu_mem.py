#!/usr/bin/python3
import psutil
import os
#!/usr/bin/python3
def get_cpu_mem():
    pid = os.getpid()
    p=psutil.Process(pid)
    cpu_percent = p.cpu_percent()
    mem_percent = p.memory_percent()
    print("cpu:{:.2f}%,mem:{:.2f}%".format(cpu_percent,mem_percent))
get_cpu_mem()