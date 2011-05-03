#!/usr/bin/python
#-*-coding:utf-8-*-
import os
import string
def sil(silinenyolu, silinendosya):
	os.system("rm -rf " + str(silinenyolu + "/" + silinendosya))
def ara(kaynak):
	silinen = 0
	for yol, dizinler, dosyalar in os.walk(kaynak):
		for dosya in dosyalar:
			dos = string.join(dosya, "")
			ignore = [
						'.py~', '.pyc',
						'.class~', '.class',
						'.c~', '.o',
						'.md~', '.mkd~',
						'.java~', '.txt~',
						'.html~',
										]
			if dos[dos.find('.'):] in ignore:
				sil(yol, dos)
				#~ print str(yol+"/"+dos)
				silinen += 1
	print kaynak, silinen, "tane dosya silindi"
ara("/home/gdemir/pro-lang")
