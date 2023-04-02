#!/usr/bin/python3
import speedtest
def Testing_Speed(net):
    download = net.download()
    upload = net.upload()
    print(f'下载速度: {download/(1024*1024)} Mbps')
    print(f'上传速度: {upload/(1024*1024)} Mbps')
    print("开始网速的测试 ...")
    #进行调用
net = speedtest.Speedtest()
Testing_Speed(net)