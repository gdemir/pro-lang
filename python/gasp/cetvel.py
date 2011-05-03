#!/usr/bin/python
from gasp import *

def raw(n, step = 0, h = 30):
	if n == 0:
		return
	else:
		Line( # sol
		     ((2 ** n - 1) * 10 + step, 0),
		     ((2 ** n - 1) * 10 + step, n * h),
		     color = (255, 255, 200))
		Line( # orta
		     ((2 * (2 ** n) - 1) * 10 + step, 0),
		     ((2 * (2 ** n) - 1) * 10 + step, (n + 1) * h),
		     color = (0, 255, 0))
		Line( # sag
		     ((3 * (2 ** n) - 1) * 10 + step, 0),
		     ((3 * (2 ** n) - 1) * 10 + step, n * h),
		     color = (255, 255, 200))

		raw(n-1, step, h) # sol tarafi verilen adimla ciz
		raw(n-1, step + 2 ** (n + 1) * 10, h) # sag tarafi verilen adimla ciz

n = 3
begin_graphics(40 * (2 ** n) , n * 70, background = (0, 150, 0))
Text("http://gdemir.me", (0, n * 70 - 40), color = (0, 100, 0), size = n * 8)

raw(n, 10, 40)
sleep(3)
