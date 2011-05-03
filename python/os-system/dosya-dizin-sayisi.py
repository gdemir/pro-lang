#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
def dosya_dizin_sayilari(kaynak):
	dizin = 0
	dosya = 0
	for altkaynak in os.listdir(kaynak):
		if os.path.isdir(kaynak + "/" + altkaynak):
			dizin += 1
			altdizin, altdosya = dosya_dizin_sayilari(kaynak + "/" + altkaynak)
			dizin += altdizin
			dosya += altdosya
		else:
			dosya += 1
	return dizin, dosya
print "dizin, dosya", dosya_dizin_sayilari("/home/gdemir/pro-lang")

