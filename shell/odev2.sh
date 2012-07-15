#!/bin/sh
# /usr/bin altındaki dosyalardan,
# ismim uzunlugu 3den kucuk olanlari yazan program.

path=/usr/bin/*

for i in $path; do
	son=$(basename $i)
	[ ${#son} -lt 3 ] && echo "3 den kucuk $son"
done

