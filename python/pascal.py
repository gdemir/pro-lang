#!/usr/bin/env python
#-*-coding:utf-8-*-
def fakt(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fakt(n - 1)

def komb(a, b):
	return fakt(a) / (fakt(b) * fakt(a - b))

def binom(sayi):
	i = 0
	while i <= sayi:
		print komb(sayi, i),
		i = i +1
	print ""

def pascal_ucgeni(sayi):
	i = 1
	j = sayi - 1
	print " " * j, 1
	while i < sayi:
		print " " * (j-1),
		binom(i)
		i = i + 1
		j = j - 1

#test demo
#~ print komb(3,0), komb(3,1), komb(3,2), komb(3,3)
# 1 3 3 1
# >>> binom(3)
# 1 3 3 1
# >>> binom(4)
# 1 4 6 4 1
# >>> pascal_ucgeni(4)
    #~ 1
   #~ 1 1
  #~ 1 2 1
 #~ 1 3 3 1
pascal_ucgeni(5)
