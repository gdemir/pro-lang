#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import string
from gasp import *
import time

def ara(kaynak):
	sozluk = {
				".c" : 0,
				".py" : 0,
				".java" : 0,
				".rb" : 0,
				".sh" : 0
			}
	for yol, dizinler, dosyalar in os.walk(kaynak):
		for dosya in dosyalar:
			dos = string.join(dosya, "")
			uzanti = dos[dos.find('.'):]
			if  uzanti in sozluk.keys():
				sozluk[uzanti] += 1
	top = 0
	for uzanti in sozluk:
		top += sozluk[uzanti]
		print uzanti, sozluk[uzanti]
	print " toplam : ", top
ara("/home/gdemir/pro-lang")
