; 1900-1906  adres aralığına veri girelim.
lxi h, 01900h

mvi m, 0a0h
inx h
mvi m, 0a1h
inx h
mvi m, 0a2h
inx h
mvi m, 0a3h
inx h
mvi m, 0a4h
inx h
mvi m, 0a5h
inx h
mvi m, 0a6h
inx h
mvi m, 0a7h



lxi h, 01900h
lxi b, 01907h ; 01907

              ; h = 1900
	      ; b = 1906

devam:  mov a, b    ; a = b      ->  a = 19
	sub h       ; a = a - h  ->  a = 19 - 19
	mov d, a    ; d = a      ->  d = 0
	            ; d = b - h

	mov a, c    ; a = c      -> a = 07
	sub l       ; a = a - l  -> a = 07 - 00
	mov e, a    ; e = a      -> e = 7
	            ; d = c - l

	mov a, d    ; a = d
	ora e       ; a = a U e   -> d U e
		    ; de == 0 ?

	jm cikis

	mov a, m    ; a = a0
	sta 1000h   ; [1000] = a0
	ldax b      ; a = a7
	mov m, a    ; m = a = a7
	lda 1000h   ; a = a0
	stax b

	inx h      ; 1901..2..3
	dcx b      ; 1906..5..4

	jmp devam

cikis:	hlt
