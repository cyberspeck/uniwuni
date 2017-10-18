#! /usr/bin/python
#-*- coding: utf-8 -*-

# Rudimentäres Beispiel 2
fp=open("/proc/cpuinfo","r")

data=fp.readlines()

fp.close()

for z in data:
 if z.find("cpu MHz")!=-1:
    print z.strip()
