#!/usr/bin/python
#-*-coding:utf-8-*-
from Tkinter import *
from time import *
# queue2.py icin
# https://github.com/gdemir/pro-lang/tree/master/python/class
# adresinden aliniz.
from queue2 import *

pc = Tk()
pc.title("sleeping barber")
pc.geometry("512x360+200+100")
pc.resizable(width = FALSE, height = FALSE)
pc.tk_setPalette("grey")

def barber(b_state):
	b_state.delete(0, END)
	if s.size() == 0: b_state.insert(END, "berber uyuyor")
	elif s.size() < s.limit: b_state.insert(END, "berber tirasa hazir")
	else: b_state.insert(END, "berber isyanlarda")

def musteri_ekle():
	global b_state, row, s
	s.enqueue("dolu")
	row[s.limit - s.size()].delete(0, END)
	row[s.limit - s.size()].insert(END, "DOLU")
	barber(b_state)

def tiras_et():
	global b_state, row, s
	if b_state.get() != "berber isyanlarda":
		s.dequeue()
		row[s.limit - s.size() - 1].delete(0, END)
		row[s.limit - s.size() - 1].insert(END, "BOS")
		barber(b_state)

buton = Button(pc, text = "Musteri ekle", command = musteri_ekle)
buton.place(relx = 0.8, rely = 0.7, relheight = 0.2, relwidth = 0.2)
berber = Button(pc, text = "Berber calistir", command = tiras_et)
berber.place(relx = 0.2, rely = 0.7, relheight = 0.2, relwidth = 0.2)

global b_state, row, s
b_state = Entry()
b_state.place(relx = 0.15, rely = 0.9, relheight = 0.1, relwidth = 0.3)
b_state.insert(END, "berber uyuyor")

s = Queue(7)
row = [None] * s.limit
for i in range(s.limit):
	row[i] = Entry()
	row[i].place(relx = i * 0.1 + 0.25, rely = 0.4, relheight = 0.1, relwidth = 0.1)
	row[i].insert(END, "BOS")
Label(pc, text = "Tiras sirasi : ",font = "Helvetica 11 bold").place(relx = 0.06, rely = 0.42)

Label(pc, text = "© Copyright 2010 Design by gdemir\n "+
					  "gdemir@bil.omu.edu.tr | http://gdemir.me",
	  font = "Helvetica 11 bold").place(relx = 0.2, rely = 0.2)
mainloop()
