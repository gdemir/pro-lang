#!/usr/bin/python
#-*-coding:utf-8-*-
import os
from Tkinter import *
pc = Tk()
baslik = pc.title("SILME")
pc.geometry("360x200+200+100")
pc.tk_setPalette("grey")
def kaynak():
	mesaj = " dosyasi basarili bir sekilde silindi"
	kaynak = grs.get()
	os.chmod(kaynak, 0777)
	os.rmdir(kaynak)
	list = kaynak.split('/')
	grs.delete(0, END)
	grs.insert(END, str(list[len(list) - 1]) + mesaj)
grs = Entry()
grs.place(relx = 0.1, rely = 0.2,relheight = 0.2, relwidth = 0.7)
Button(text = "tamam", command = kaynak).place(relx = 0.5, rely = 0.4)
Label(text = "© Copyright gdemir" ).place(relx = 0.3, rely = 0.6)
mainloop()
