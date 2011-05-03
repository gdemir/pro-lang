#!/usr/bin/env python
#-*-coding:utf-8-*-
n = input('>>> Lutfen asalsayi girin')
for n in range(2, n+1):
	asal = True
	for i in range(2, n):
		if n % i == 0 and asal: asal = False
	if asal: print n,
