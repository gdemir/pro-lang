#!/usr/bin/python
#-*-coding:utf-8-*-
from config import *

class Ogrenci:
	def __init__(self, csvname, KEY):
		self.ogr = {}
		self.csv = csvname
		self.KEY = KEY
		self.alan = self.yukle()
	def goster(self):
		for key, bilgi in self.ogr.items(): print key, bilgi

	def bul(self):
		for key in self.ogr.items():
			print key
			yield i

	def diz(self, liste, bliste = None):
		depo = {}
		if bliste == None: bliste = liste
		for i in range(len(liste)): depo[liste[i]] = bliste[i]
		return depo

	def yukle(self):
		okuyucu = csv.DictReader(open(self.csv))
		self.alan = okuyucu.fieldnames
		for kisi in okuyucu: self.ogr[kisi[self.KEY]] = [kisi[a] for a in self.alan]
		return self.alan

	def bosalt(self): #boşalt
		yaz = csv.DictWriter(open("db1.csv", "w"), self.alan)
		yaz.writerow(self.diz(self.alan))
		for bilgi in self.ogr.values(): yaz.writerow(self.diz(self.alan, bilgi))


c = Ogrenci("db.csv", "no")
print c.alan
#~ c.goster() 10060271
c.bul()
c.bosalt()
