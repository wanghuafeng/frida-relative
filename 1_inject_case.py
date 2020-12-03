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

process = frida.get_remote_device().attach('com.xiangrikui.sixapp') #得到设备并劫持进程com.example.testfrida（该开始用get_usb_device函数用来获取设备，但是一直报错找不到设备，改用get_remote_device函数即可解决这个问题）
script = process.create_script(jscode) #创建js脚本
script.on('message',on_message) #加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load() #加载脚本
sys.stdin.read()


"""
1.通过调用frida.get_usb_device()方法来得到一个连接中的USB设备（Device类）实例
2.调用Device类的attach()方法来附加到目标进程并得到一个会话（Session类）实例，该方法有一个参数，参数是需要注入的进程名或者进程pid。如果需要Hook的代码在App的启动期执行，那么在调用attach方法前需要先调用Device类的spawn()方法，这个方法也有一个参数，参数是进程名，该方法调用后会重启对应的进程，并返回新的进程pid。得到新的进程pid后，我们可以将这个进程pid传递给attach()方法来实现附加。
3.接着调用Session类的create_script()方法创建一个脚本，传入需要注入的javascript代码并得到Script类实例
4.调用Script类的on()方法添加一个消息回调，第一个参数是信号名，乖乖传入message就行，第二个是回调函数
5.最后调用Script类的load()方法来加载刚才创建的脚本。
注：如果想在javascript输出日志，可以调用console.log()方法。如果想给客户端发送消息，可以在javascript代码里调用send()方法，并在客户端Python代码里注册一个消息回调来接收服务端发来的消息。
"""