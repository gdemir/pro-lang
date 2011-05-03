#!/bin/bash

echo -n "kac kisi ?"
read n
du -s $(readlink -f $HOME/..)/* 2>/dev/null | sort -gr  | while read kisi; do
								mb=`echo $kisi | cut -d ' ' -f1`
	                                                        user=`echo $kisi | cut -d ' ' -f2`
								echo "$mb ->$(basename $user)<-"
								n=$(($n-1))
								[ $n -eq 0 ] && break
							done
