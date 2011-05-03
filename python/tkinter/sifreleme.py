#!/usr/bin/python
#-*- coding:utf-8 -*-

import random
from Tkinter import *

pc = Tk()
pc.title("Sifreleme programi")
pc.geometry("512x360+200+100")
pc.resizable(width = FALSE, height = FALSE)
pc.tk_setPalette("grey")

def label(pc_ismi, message, x, y, f, color):
	etkt = Label(pc_ismi, text = message, font = f, fg = color)
	etkt.place(relx = x, rely = y)

# ascii'n 32 önceki kısımlar alma çünkü
# ekranda zaten görüntülenmiyorlar. (bkz : man ascii)
def calkala():
	random.seed(int(parola.get()))
	dizi = [chr(i) for i in range(32, 127)]
	for i in range(len(dizi)):
		j = random.randint(0, 91)
		dizi[i], dizi[j] = dizi[j], dizi[i]
	return dizi

def tohum(FONKSIYON):
	global parola
	pc2 = Toplevel()
	baslik = pc2.title("Parola")
	pc2.geometry("360x100+200+100")
	parola = Entry(pc2)
	parola.pack()
	buton(pc2, [
			('tamam', FONKSIYON),
			('kapat', pc2.destroy),
						],
			0.4, 0.2, 0.2, 0.2, 0, 0.2)

# metnimizi verilen base göre şifreleyelim.
def yap():
	s = giris.get()
	base = calkala()
	son = "".join(base[ord(item) - 32] for item in s)
	cikis.insert(END, son)

# metnimizi verilen base göre çözelim.
def boz():
	s = giris.get()
	base = calkala()
	son = "".join(chr(base.index(item) + 32) for item in s)
	cikis.insert(END, son)

def yap_tohum(): tohum(yap)
def boz_tohum(): tohum(boz)

def delete():
	giris.delete(0, END)
	cikis.delete(0, END)

def buton(pc_ismi, MOD, x, y, h, w, x_step, y_step):
	for message, function in MOD:
		btn = Button(pc_ismi, text = message, command = function)
		btn.place(relx = x, rely = y, relheight = h, relwidth = w)
		x += x_step
		y += y_step
def help():
	pc2 = Toplevel()
	pc2.title("Yardim")
	pc2.geometry("512x200+200+100")
	pc2.resizable(width = FALSE, height = FALSE)
	label(pc2, '\tGirdiğiniz parolaya göre metninizi;\n'
		 + 'şifrelemeye veya çözmeye yarayan ufak bir program.\n',
       		 0.1, 0.1, "Helvetica", "black")
	label(pc2, 'author   : gdemir\n', 0.2, 0.4, "Helvetica 11 bold", "black")
	label(pc2, 'email     :  gdemir@bil.omu.edu.tr\n', 0.2, 0.5, "Helvetica 11 bold", "black")
	label(pc2, 'website : http://gdemir.me\n', 0.2, 0.6, "Helvetica 11 bold", "black")
	buton(pc2, [
			('kapat', pc2.destroy),
						],
			0.4, 0.75, 0.15, 0.15, 0, 0)
giris = Entry()
giris.place(relx = 0.2, rely = 0.2, relheight = 0.2, relwidth = 0.25)
cikis = Entry()
cikis.place(relx = 0.5, rely = 0.2, relheight = 0.2, relwidth = 0.25)
buton(pc, [
		("şifrele", yap_tohum),
		('çöz', boz_tohum),
		('sil', delete),
		('çıkış', pc.quit),
		('yardim', help),
					],
		0.1, 0.5, 0.07, 0.15, 0.15, 0)
label(pc, '© Copyright 2010 design by gdemir\n',
           0.2, 0.7, "Helvetica 11 bold", "black")
label(pc, 'DİKKAT! Türkçe karakterler kullanmayınız.\n',
           0.2, 0.6, "Helvetica 11 ", "dark gray")
mainloop()
