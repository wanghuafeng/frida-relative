#!-*- coding:utf-8 -*-
import frida
import sys
rdev = frida.get_remote_device()
processes = rdev.enumerate_processes()
for processe in processes:
	print (processe)
