lxi h, 0ffffh
mvi b, 0ffh
mvi c, 0100h

loop:	mov m, b
	dcr b
	dcx h
	dcr c
	jnz loop

; kontrol edelim ->
lxi h, 0ffffh
mvi c, 0100h
cont:	mov d, m
	dcx h
	dcr c
	jnz cont
hlt

;ffff -> ff
;ffde -> fe
;fffd -> fd
;fffc -> fc
;fffb -> fb
;fff0 -> f0
;fff9 -> f9
;fff8 -> f8
;fff7 -> f7
;fff6 -> f6
;fff5 -> f5
;fff4 -> f4
;fff3 -> f3
;fff2 -> f2
;fff1 -> f1
;fff0 -> f0

;fd00 - 256
;fdff - 257
