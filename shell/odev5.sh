#!/bin/bash
# /home aldindaki dosyalardan
# en yuksek 5 user'i gosteren program.

echo -n "siniri asanlar"
echo    "--------------"
i=0
du -s $(readlink -f $HOME/..)/* 2>/dev/null | sort -gr | while read kisi; do
							mb=`echo $kisi | cut -d ' ' -f1`
							user=`echo $kisi | cut -d ' ' -f2`
							[ $i -lt 5 ] && echo "->$(basename $user)<-" 
							i=$(($i+1))
						done
