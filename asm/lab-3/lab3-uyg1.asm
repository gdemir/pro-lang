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
mvi a, 10h


mvi e, 0a1h ; sayimiz

mvi b, 00h  ; kucuk sayisi
mvi c, 00h  ; buyuk sayisi
mvi d, 00h  ; esit sayisi


dongu:  sta 1000h;	

	call  karsilastir

	lda 1000h;
	inx h
	dcr a

	jnz dongu
	hlt



karsilastir: mov a, m
	mov a, e   ; a = e
	cmp m      ; e - m ?

	jnz esit_degil
	inr c      ; eşit
	jmp son

esit_degil: jp buyuk_degil
	inr b      ; buyuk
	jmp son

buyuk_degil: inr d ; kucuk
son:	ret
