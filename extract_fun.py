#!-*- coding:utf-8 -*-
from __future__ import print_function
import frida, sys

def on_message(message, data):
    print(message)

jscode = """
    Process.enumerateModules({
          onMatch:function(exp){
        send(exp.name);
      },
          onComplete:function(){
        send("stop");
      }
})
"""

process = frida.get_usb_device().attach('com.longrise.android.bbt')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()