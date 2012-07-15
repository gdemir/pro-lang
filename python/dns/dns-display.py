#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import string

oku = open("/etc/resolv.conf", "r")
print string.join(list(oku)[1:], "")
oku.close()
print "© Copyright gdemir"
