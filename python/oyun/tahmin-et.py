#!/usr/bin/python
#-*- coding: utf-8 -*-

# örnek denemeler :
# sayi   : 1234 1234 1234 1234 1234 1234 1122 1122 2112 9999 1671 1766 6661
# tahmin : 1567 1537 1111 1112 4321 1234 1234 1991 1991 9139 1266 1621 2346
# çıktı  : +    ++   +    +-   ---- ++++ +-   +-   --   ++   +-   +-   -

from random import randint
def uret(): # 4 basamaklı bir sayı üret
    return str(randint(1000, 9999))

def win(message): # başarı veya başarısız durum için
    print message
    exit(19)

def cry(message): # uyar
    print message

def compo(sayi, tahmin):
    state = ""
    for i in range(len(sayi)): # uyuşan kısımları +'la
        if tahmin[i] == sayi[i]:
            state += "+"
            tahmin[i] = "+"
            sayi[i] = "+"
    for i in range(len(sayi)): # uyuşmayan kısımları -'le
        if tahmin[i] in sayi and not tahmin[i] in "+-":
            state += "-"
            sayi[sayi.index(tahmin[i])] = "-"
            tahmin[i] = "-"
    return state

up = 10
sayi = uret()
while up > 0:
    # tahminin nedir uğurcum ?
    tahmin = raw_input("[hamle hakkı : %d  ] Bana 4 basmaklı bir sayi ver : " % (up))
    # sayın 4 basamaklı hem de rakam olmalı
    if not tahmin.isdigit() or len(tahmin) != 4:
        cry("Bana sadece 4 basamaklı bir sayı ver")
        continue
    # ip ucu üret
    state = compo(list(sayi), list(tahmin))
    if  state == "++++": win("tebrikler kazandınız")
    print state # ip ucu verelim
    up -= 1
print "kaybettiniz saklanan sayı : ", sayi
