#!/bin/sh
# /usr/bin altındaki dosyalardan
# sembolik ve calistirilabilir olanlari gosteren program.

path=/usr/bin/*

for i in $path; do
	[ -L "$i" -a -x "$i" ] && echo "calistirilir ve sembolik -> $i"
done
