#!-*- coding:utf-8 -*-
import frida  #导入frida模块
import sys    #导入sys模块

jscode = """
setTimeout(function(){
  Java.perform(function(){
        console.log("hello world!");    
      });
 });
"""

def on_message(message, data): #js中执行send函数后要回调的函数
    print(message)
process = frida.get_remote_device().spawn('com.icbc.im')
script = process.create_script(jscode) #创建js脚本
script.on('message',on_message) #加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load() #加载脚本
sys.stdin.read()

