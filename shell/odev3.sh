#!/bin/bash
# /home aldindaki dosyalardan
# kota sinirini gecenleri listeleyen program.

echo -n "kota siniri ?"
read n
echo -n "siniri asanlar"
echo    "--------------"
du -s $(readlink -f $HOME/..)/* 2>/dev/null  | while read kisi; do
							mb=`echo $kisi | cut -d ' ' -f1`
							user=`echo $kisi | cut -d ' ' -f2`
							[ $mb -gt $n ] && { echo "->$(basename $user)<-" > kota-asan.txt}
						done
