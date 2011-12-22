#!/usr/bin/python
#-*- coding:utf-8 -*-

from random import *
from Tkinter import *
from kernel import *

pc = Tk()
pc.title("Hesap Makinası")
pc.geometry("512x360+200+100")
pc.resizable(width = FALSE, height = FALSE)
pc.tk_setPalette("gray")

global thema_index, exp_ok
exp_ok = False
thema_index = 1

giris = Entry()
giris.place(relx = 0.2, rely = 0.2, relheight = 0.15, relwidth = 0.6)

def buton(pc_ismi, MOD, x, y, h, w, x_step, y_step):
	for message, function in MOD:
		btn = Button(pc_ismi, text = message, command = function)
		btn.place(relx = x, rely = y, relheight = h, relwidth = w)
		x += x_step
		y += y_step

def label(pc_ismi, message, x, y, f, color):
	etkt = Label(pc_ismi, text = message, font = f, fg = color)
	etkt.place(relx = x, rely = y)

def clc_exp():
	global exp_ok
	if exp_ok == True:
		giris.delete(0, END)
		exp_ok = False

def new_exp():
	global exp_ok
	if exp_ok == True:
		exp_ok = False

def choice9():     clc_exp();giris.insert(END, "9")
def choice8():     clc_exp();giris.insert(END, "8")
def choice7():     clc_exp();giris.insert(END, "7")
def choice6():     clc_exp();giris.insert(END, "6")
def choice5():     clc_exp();giris.insert(END, "5")
def choice4():     clc_exp();giris.insert(END, "4")
def choice3():     clc_exp();giris.insert(END, "3")
def choice2():     clc_exp();giris.insert(END, "2")
def choice1():     clc_exp();giris.insert(END, "1")
def choice0():     clc_exp();giris.insert(END, "0")
def choice00():     clc_exp();giris.insert(END, "00")
def choiceopen():  clc_exp();giris.insert(END, "(")
def choiceclose(): clc_exp();giris.insert(END, ")")
def choiceadd():   new_exp();giris.insert(END, "+")
def choicedel():   new_exp();giris.insert(END, "-")
def choicemul():   new_exp();giris.insert(END, "*")
def choicediv():   new_exp();giris.insert(END, "/")
def choicepoint(): new_exp();giris.insert(END, ".")
def delete():      new_exp();giris.delete(0, END)
def choiceback():
	giris.insert(END, "/")
	girdi = giris.get()
	giris.delete(0, END)
	giris.insert(0, girdi[0:-2])

def result():
	global exp_ok

	result = main(giris.get())
	if str(result).find(".") != -1:
		part = str(result).split(".")
		if part[1] == "0": result = part[0]
	giris.delete(0, END)
	giris.insert(0, result)
	exp_ok = True

def thema():
	global thema_index
	thema_index = 1 - thema_index
	thema = ["white", "gray"]
	pc.tk_setPalette(thema[thema_index])

def help():
	pc2 = Toplevel()
	pc2.title("Yardim")
	pc2.geometry("512x200+200+100")
	pc2.resizable(width = FALSE, height = FALSE)
	label(pc2, '\tGirdiğiniz işlemleri hesaplayan \n'
				+ ' ufak bir program.\n',
				0.1, 0.1, "Helvetica", "black")
	label(pc2, 'author   : jack, gdemir\n', 0.2, 0.4, "Helvetica 11 bold", "black")
	buton(pc2, [
	     ('kapat', pc2.destroy),
	    ],
       0.4, 0.75, 0.15, 0.15, 0, 0)

buton(pc, [
	('7', choice7),
	('8', choice8),
	('9', choice9),
	('/', choicediv),
	('←',choiceback),
	('c', delete),
   ],
   0.2, 0.5, 0.07, 0.1, 0.1, 0)
buton(pc, [
	('4', choice4),
	('5', choice5),
	('6', choice6),
	('*', choicemul),
	('(', choiceopen),
	(')', choiceclose),
   ],
   0.2, 0.57, 0.07, 0.1, 0.1, 0)
buton(pc, [
	('1', choice1),
	('2', choice2),
	('3', choice3),
	('+', choiceadd),
   ],
   0.2, 0.64, 0.07, 0.1, 0.1, 0)
buton(pc, [
	('0', choice0),
	('00', choice00),
	('.', choicepoint),

	('-', choicedel),
   ],
   0.2, 0.71, 0.07, 0.1, 0.1, 0)
buton(pc, [
	('tema', thema),
	('yardim', help),
	('çıkış', pc.quit),
   ],
   0.2, 0.1, 0.1, 0.2, 0.2, 0)
buton(pc, [
	('=', result),
   ],
   0.6, 0.64, 0.14, 0.2, 0.3, 0)
label(pc, '© Copyright 2011 designed ondokuz.biz ',
           0.2, 0.8, "Helvetica 9", "black")
mainloop()
