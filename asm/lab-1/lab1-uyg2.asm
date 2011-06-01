; 2 16 - bit sayıyı çarpma
; lhld 2000H
; sphl      ; stack 16 bit var.
; lhld 3000H
; xchg      ; de'de 16 bit sayı var.


lxi h, 2000h
mvi m, 00h
lxi h, 2001h
mvi m, 01h


lxi h, 3000h
mvi m, 00h
lxi h, 3001h
mvi m, 01h


lhld 2000H
sphl            ;sp = 0100
lhld 3000H
xchg            ;de = 0100
lxi h, 0000h	;
lxi b, 0000h    ;

next:	dad sp  ;hl = hl + sp
	jc var  ;elde var
	dcx d
	jnz next
	hlt
var:	inx b   ;bc = bc + 1
	jnz next
	hlt
