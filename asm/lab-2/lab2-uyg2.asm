lxi h, 0200h

mvi m, 0a1h
inx h
mvi m, 0a0h
inx h
mvi m, 0a2h
inx h
mvi m, 0a3h
inx h
mvi m, 0a4h
inx h
mvi m, 0ffh
inx h
mvi m, 0a6h
inx h
mvi m, 0a7h
inx h
mvi m, 03h
inx h
mvi m, 0a9h
inx h
mvi m, 0b0h
inx h
mvi m, 0b1h
inx h
mvi m, 0b2h
inx h
mvi m, 0b3h
inx h
mvi m, 0b4h
inx h
mvi m, 0b5h


lxi h, 0200h
mvi b, 0fh

mov d, m ; büyükler için
mov e, m ; küçükler için
dcr b 

dongu:   inx h

	mov a, d   ; d = a
	cmp m      ; a = d - m
	jp  kucuk  ; a pozitif mi ? öyle ise atla / değilse m = büyüktür
	mov d, m   ; buyuk ise at

kucuk:  mov a, e   ; e = a
	cmp m      ; a = e - m
	jc  buyuk  ; a negatif mi ? öyle ise atla / değilse m = küçüktür
	mov e, m   ; kucuk ise at

buyuk:	dcr b
	jnz dongu
	hlt
