#!/bin/sh
# bir dizine bir dosyayi tasirken ayni dosya
# varsa onu *.bak olarak yedegini alan program

if [ ! $# -eq 2 ];then
	echo "kullanım : <m> <file> <path>"
	exit 1
fi
if [ -f $2$1 ];then
	mv $1 $2$1.bak
	echo "Oops! $2 dizinini altinda $1 adinda ayni bir dosya var"
	echo "$2$1 altindaki dosyayi  $1 ->  $1.bak olarak sakladim."
fi
mv $1 $2

