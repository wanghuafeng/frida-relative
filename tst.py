#!-*- coding:utf-8 -*-
import frida  #导入frida模块
import sys    #导入sys模块

jscode = """
    console.log("脚本载入成功");
     var file = new File("/data/local/encrypt.txt","wb");
     file.write("dfa;dfakdf;a");
     file.flush()
     file.close();
"""

def on_message(message, data): #js中执行send函数后要回调的函数
    print(message)

process = frida.get_remote_device().attach('com.xiangrikui.sixapp') #得到设备并劫持进程com.example.testfrida（该开始用get_usb_device函数用来获取设备，但是一直报错找不到设备，改用get_remote_device函数即可解决这个问题）
script = process.create_script(jscode) #创建js脚本
script.on('message',on_message) #加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load() #加载脚本
sys.stdin.read()