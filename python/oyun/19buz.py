#!/usr/bin/python
#-*- coding:utf-8 -*-
from gasp import *; from time import sleep
begin_graphics(background = color.BLACK)
def kontrol(b_x, b_y, ust_snr, alt_snr, sol_snr, sag_snr):
	if   b_x >= sag_snr: return 1
	elif b_x <= sol_snr: return 2
	elif b_y >= ust_snr: return 3
	elif b_y <= alt_snr: return 4
	else: return 0
def uret():
	while True:
		x = random_between(2, 5)
		if x != 3: return x
def rand():
	rast = ["ust", "alt"]
	return rast[random_between(0, 1)]
def p1_cubuk(b_y, b_x, r_x, r_y):
	return b_y > r_y and b_y < r_y + 100 and b_x < r_x + 10
def p2_cubuk(b_y, b_x, r_x, r_y):
	return b_y > r_y and b_y < r_y + 100 and b_x + 10 > r_x
def sifirla(): return 0, 0, 1, 1, "", "", 0, 0, 75, 270, 5, 220, 625, 220
def score(p1_tablo, x, p_can):
	remove_from_screen(p1_tablo)
	return p_can-1, Text(str(p_can-1),(x,430),size=24,color=(255,200,0))
def sil(*silinen):
	for i in silinen: remove_from_screen(i)
def yaz(mesaj, yer, boyut, renk):
	return Text(mesaj, yer, size = boyut, color = renk)
def die(p1_can, p2_can):
	if p1_can and p2_can: return 0
	else: return 1
def sinirlar():
	return 400, 100, 5, 630
def winner(p1_can, p2_can):
	if p1_can: L = yaz("PLAYER1 YENDI", (100, 300), 60, (255, 0, 0))
	if p2_can: L = yaz("PLAYER2 YENDI", (100, 300), 60, (255, 0, 0))
	sleep(1), sil(L)
def r1_ciz():
	r1_x = 5; r1_y = 220
	return r1_x, r1_y,\
		  Box((r1_x, r1_y), 5, 60, color = (78, 255, 200), filled = True)
def r2_ciz():
	r2_x = 625; r2_y = 220
	return r2_x, r2_y,\
		  Box((r2_x, r2_y), 5, 60, color = (78, 255, 200), filled = True)
def b_ciz():
	b_x = 75; b_y = 270
	return b_x, b_y,\
		    Circle((b_x, b_y), 10, color = (255, 255, 255), filled = True)
def ana_menu():
	return yaz("o : oyna   ", (100, 350), 40, (78, 200, 200)),\
		   yaz("h : hakkinda ", (100, 300), 40, (78, 200, 200)),\
		   yaz("y : yardim  ", (100, 250), 40, (78, 200, 200)),\
		   yaz("q : cikis  ", (100, 200), 40, (78, 200, 200))

def hakkinda():
	L1 = yaz("19 Buz! ", (100, 325), 50, (78, 200, 200))
	L2 = yaz("gokhan demir tarafindan 2010 yilinda", (100, 275), 20, (78, 200, 200))
	L3 = yaz("yapilmistir. Tum haklari mahfuzdur.", (100, 225), 20, (78, 200, 200))
	L4 = yaz("(copyright) gdemir@bil.omu.edu.tr", (100, 175), 20, (78, 200, 200))
	L5 = yaz("http://gdemir.me", (100, 125), 20, (78, 200, 200))
	sleep(4), sil(L1, L2, L3, L4, L5)

def yardim():
	L1 = yaz("Hareket tuslari:", (100, 350), 25, (78, 200, 200))
	L2 = yaz("Player 1     Player 2 ", (170, 300), 25, (78, 200, 200))
	L3 = yaz("   W                  8",(180, 250), 23, (78, 200, 200))
	L4 = yaz("A  S  D          4  5  6",(180, 200), 23, (78, 200, 200))
	sleep(4), sil(L1, L2, L3, L4)

def amblem_19():
	Circle((50, 475), 5, color = (78, 255, 200), filled = True)
	Circle((50, 425), 5, color = (78, 255, 200), filled = True)
	Circle((50, 450), 5, color = (78, 200, 200), filled = True)
	Circle((75, 475), 5, color = (78, 200, 200), filled = True)
	Line((50, 450), (100, 450), color = (78, 200, 200))
	Line((50, 450), (100, 450), color = (78, 200, 200))
	Line((75, 425), (75, 475), color = (78, 200, 200))
	Line((75, 425), (75, 475), color = (78, 200, 200))
	Circle((100, 475), 5, color = (78, 255, 200), filled = True)
	Circle((100, 450), 5, color = (78, 200, 200), filled = True)
	Circle((100, 425), 5, color = (78, 255, 200), filled = True)
	Circle(( 75, 425), 5, color = (78, 200, 200), filled = True)
	yaz("19", (56, 440), 30, (255, 255, 255))
	yaz("Buz!", (105, 420), 24, (78, 255, 200))
	Line((45,415),(160,415),color = (78,200,200))
	Box((50, 425), 50, 50, color = (78,255,200))
	Box((50, 425), 50, 50, color = (78,255,200))
	Box((50, 425), 50, 50, color = (78,255,200))
	Box((50, 425), 50, 50, color = (78,255,200))

def oyna():
	saha = Box((5, 100), 625, 300, color = color.WHITE)
	b_x , b_y , b  =  b_ciz()
	r1_x, r1_y, r1 = r1_ciz()
	r2_x, r2_y, r2 = r2_ciz()
	ust_snr, alt_snr, sol_snr, sag_snr = sinirlar() # sol, sag, alt, ust sinirlar
	p1_can = 3; p2_can = 3 # player canlari
	dx = 3; dy = uret()
	o = gc = rand()
	stop, secim, kilit, ilk, ua, ss,\
	p1, p2, b_x, b_y, r1_x, r1_y, r2_x, r2_y = sifirla()
	L1 = yaz("PLAYER-1", (150, 460), 24, (78, 200, 200))
	L2 = yaz("PLAYER-2", (350, 460), 24, (78, 200, 200))
	p1_tab = yaz(str(p1_can), (200, 430), 24, (255, 200, 0))
	p2_tab = yaz(str(p2_can), (400, 430), 24, (255, 200, 0))
	zaman = 1
	while True:
		sleep(zaman)
		if p1 == 1: # player1 cubugu vurunca yap
			if kilit: gc = "sol"; ss = "sol"; kilit = 0
			if ua == "ust": b_y -= dy; b_x += dx
			if ua == "alt": b_y += dy; b_x += dx
		if p2 == 1: # player2 cubugu vurunca yap
			if kilit: gc = "sag"; ss = "sag"; kilit = 0
			if ua == "ust": b_y -= dy; b_x -= dx
			if ua == "alt": b_y += dy; b_x -= dx
		if ilk == 1 and p1 == 0 and p2 == 0: # ilkleme
			if kilit: gc = "sol"; ss = "sol"; zaman = 0.016; kilit = 0
			if o == "ust": b_y -= dy; b_x += dx
			if o == "alt": b_y += dy; b_x += dx
		if ilk == 0 and p1 == 0 and p2 == 0: # topun gidecegi yerler
			if secim == 1 or secim == 2: # sahanin sag ve sol tarafi
				if secim == 1: p2_can, p2_tab = score(p2_tab, 400, p2_can)
				if secim == 2: p1_can, p1_tab = score(p1_tab, 200, p1_can)
				stop, secim, kilit, ilk, ua, ss,\
				p1, p2, b_x, b_y, r1_x, r1_y, r2_x, r2_y = sifirla()
				dy = uret()
				o = gc = rand()
			if secim == 3: # sahanin ust tarafina top gelirse
				if kilit: gc = "ust"; ua = "ust"; kilit = 0
				if (o == "alt" and ss == "sol") or o == "sol": b_x += dx; b_y -= dy
				if (o == "alt" and ss == "sag") or o == "sag": b_x -= dx; b_y -= dy
			if secim == 4 :# sahanin alt tarafina top gelirse
				if kilit: gc = "alt"; ua = "alt"; kilit = 0
				if (o == "ust" and ss == "sol") or o == "sol": b_x += dx; b_y += dy
				if (o == "ust" and ss == "sag") or o == "sag": b_x -= dx; b_y += dy
		if kontrol(b_x, b_y, ust_snr, alt_snr, sol_snr, sag_snr):
			o = gc
			secim = kontrol(b_x, b_y, ust_snr, alt_snr, sol_snr, sag_snr)
			if kilit == 0: kilit = 1
			if ilk   == 1: ilk = 0
			if (p1 == 1 or p2 == 1) and zaman >= 0: zaman -=  0.0005 #top hizlandir
			if p1    == 1: p1 = 0
			if p2    == 1: p2 = 0
		if b_x >= r2_x and b_x <= r1_x:   stop = 1
		if p1_cubuk(b_y, b_x, r1_x, r1_y) and stop == 0: p1 = 1; ss = "sol"
		if p2_cubuk(b_y, b_x, r2_x, r2_y) and stop == 0: p2 = 1; ss = "sag"
		move_to(b, (b_x, b_y)) #topu tasi
		if key_pressed('w') and r1_y <= 335: r1_y += 5
		if key_pressed('s') and r1_y >= 105: r1_y -= 5
		if key_pressed('d') and r1_x <= 75:  r1_x += 5
		if key_pressed('a') and r1_x >= 10:  r1_x -= 5
		if key_pressed('8') and r2_y <= 335: r2_y += 5
		if key_pressed('5') and r2_y >= 105: r2_y -= 5
		if key_pressed('6') and r2_x <= 620: r2_x += 5
		if key_pressed('4') and r2_x >= 555: r2_x -= 5
		if die(p1_can,p2_can):
			sil(L1, L2, r1, r2, p1_tab, p2_tab, saha, b); break
		move_to(r1, (r1_x, r1_y)) # player1 cubugunu tasi
		move_to(r2, (r2_x, r2_y)) # player2 cubugunu tasi
	if p1_can == 0 or p2_can == 0: winner(p1_can, p2_can)

L1, L2, L3, L4 = ana_menu()
amblem_19()
yaz("Copyright gdemir", (200,  25), 24, (255, 200, 0))
while True:
	sleep(0.01)
	if key_pressed('o'): sil(L1, L2, L3, L4); oyna();    L1, L2, L3, L4 = ana_menu()
	if key_pressed('h'): sil(L1, L2, L3, L4); hakkinda();L1, L2, L3, L4 = ana_menu()
	if key_pressed('y'): sil(L1, L2, L3, L4); yardim();  L1, L2, L3, L4 = ana_menu()
	if key_pressed('q'): sil(L1, L2, L3, L4); break
sleep(0.5), end_graphics()
