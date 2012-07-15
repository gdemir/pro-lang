#!/usr/bin/python
#!-*- coding:utf-8 -*-
import csv
import os
from contextlib import contextmanager
from copy import deepcopy
from sys import *
from time import *

# Turkce duyarli kucuk harfe cevir.
def kucult(dizgi):
    return dizgi.decode('utf-8').lower().encode('utf-8')

# Turkce duyarli buyuk harfe cevir.
def buyult(dizgi):
    return dizgi.decode('utf-8').upper().encode('utf-8')

# Turkce duyarli ilk harfler buyuk.
def ilkbuyult(dizgi):
    return " ".join(
        s.decode('utf-8').lower().capitalize().encode('utf-8')
        for s in dizgi.split()
    )

def isimbul(name1, name2):
	if name1[0] >= name2[0]:
		return name1[0] + name2[0]
	else:
		return name2[0] + name1[0]

def kafa(patika):
    dosya = open(patika)
    # ilk satir daima baslik satiri.  Alan isimlerini okuyoruz...
    return [i for i in csv.DictReader(dosya, skipinitialspace=True).fieldnames]

@contextmanager
def csvokuyan(patika):
    dosya = open(patika)
    # ilk satir daima baslik satiri.  Alan isimlerini okuyoruz...
    okuyucu = csv.DictReader(dosya, skipinitialspace=True)

    # ve bir yineleyici (iterator) donuyoruz.
    yield csv.DictReader(dosya, [ kucult(f) for f in okuyucu.fieldnames ])

# 'with' ile CSV dosya yazmak icin kullanilabilecek bir yardimci.
# Ornek:
#    with csvyazan("foo.csv", ("bir alan", "baska alan"))) as yazici:
#        yazici.writerow({ "bir alan": "foo", "baska alan": "bar" })
#        ...

@contextmanager
def csvyazan(patika, alanadlari):
    dosya = open(patika, "w")
    # ilk satir daima baslik satiri.  Alan isimlerini okuyoruz...
    alanadlari = [kucult(f) for f in alanadlari]
    yazici = csv.DictWriter(dosya, alanadlari)
    yazici.writerow(dict((n,n) for n in alanadlari))
    # ve bir yineleyici (iterator) donuyoruz.
    yield csv.DictWriter(dosya, alanadlari)

def al(csv, alanlar):
	kisiler = []
	with csvokuyan(csv) as okuyucu:
		for satir in okuyucu:
			kisi = {}
			for alan in alanlar:
				kisi[alan] = satir[alan]
			kisiler.append(kisi)
	return kisiler

def yaz(csv, kisiler, alanlar):
	with csvyazan(csv, tuple(alanlar)) as yazici:
		for kisi in kisiler:
			yazici.writerow(kisi)
def bul(kisiler, aranan, key):
	for kisi in kisiler:
		if kisi[key] == aranan:
			return kisi
	return 0

def main(key, secenek, hedef_csv, kaynak_csv):

	hedef_alanlar = kafa(hedef_csv)
	kaynak_alanlar = kafa(kaynak_csv)
	kaynak_veriler = al(kaynak_csv, kaynak_alanlar)
	hedef_veriler  = al(hedef_csv, hedef_alanlar)

	ortak_veriler = []
	fark_veriler = []
	ek_veriler = deepcopy(hedef_veriler)
	
	key_depo = [hedef_veri[key] for hedef_veri in hedef_veriler]
	for kaynak_veri in kaynak_veriler:

		if secenek in ["-s", "-a"]:
			if kaynak_veri[key] in key_depo:
				ortak_veriler.append(kaynak_veri)

		if secenek in ["-d", "-a"]:
			if not kaynak_veri[key] in key_depo:
				fark_veriler.append(kaynak_veri)

		if secenek in ["-j", "-a"]:
			for ek_veri in ek_veriler:
				if ek_veri[key] == kaynak_veri[key]: # kisiyi bul
					for ek_key in ek_veri.keys(): # kisini bilgileri kap
						if ek_veri[ek_key] == "" and kaynak_veri.has_key(ek_key):
							ek_veri[ek_key] = kaynak_veri[ek_key] # kisiyi guncelle
					break # kisiden cik

	if secenek in ["-j", "-a"]:
		yaz(hedef_csv + "-ekleme", ek_veriler, hedef_alanlar)
	if secenek in ["-s", "-a"]:
		yaz(isimbul(kaynak_csv, hedef_csv) + "-ortak", ortak_veriler, hedef_alanlar)
	if secenek in ["-d", "-a"]:
		yaz(kaynak_csv + "-fark", fark_veriler, kaynak_alanlar)

def help(pname):
	exit("\
	adi      : files comparator \n\
	kullanim : <%s> [islemler] <key> <dest-csv> <src-csv> \n\
	islemler  :\n\
	    -a : tum islemler \n\
	    -d : key baz alinarak, kaynak-csv'nin hedef-csv'den farkinin ciktisi (2 csvnin alan adlariayni olmali)\n\
	    -h : yardim <%s> \n\
	    -s : key baz alinarak, kaynak-csv ile hedef-csv'nin ortak alanlarin ciktisi (2 csvnin alan adlari ayni olmali)\n\
	    -j : kaynak-csv'de olup hedef-csv'de olmayan verilerin eklenmis ciktisi\n\
	"%(pname, pname))

def secim_kontrol(argv):
	islemler = ["-a", "-d", "-s", "-h", "-j"]
	if len(argv) == 5 and argv[1] in islemler:
		return True, argv[1]
	elif len(argv) == 4 and not argv[1] in islemler:
		return False, "-a"
	else:
		exit("%s uygun bir secenek degildir. <%s> -h diyerek yardim aliniz" % (argv[1], argv[0]))

def kullanim(pname):
	exit("kullanım: <%s> [options] <key> <dest-csv> <src-csv>" % pname)

if __name__ == "__main__":
	if len(argv) == 1: kullanim(argv[0])
	if argv[1] == "-h": help(argv[0])
	if len(argv) < 4 and len(argv) <= 5: kullanim(argv[0])

	secim, secenek = secim_kontrol(argv)
	anahtar = argv[secim + 1]
	dosya1  = argv[secim + 2]
	dosya2  = argv[secim + 3]

	if not (os.path.exists(dosya1) and os.path.exists(dosya2)):
		exit("%s %s dosyalaridan enazindan biri yok" % (dosya1, dosya2))

	main(anahtar, secenek, dosya1, dosya2)
