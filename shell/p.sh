#!/bin/sh

if [ $# -eq 1 ];then
	ps ax | grep -i $1
else
	ps ax
	echo "tumunu listeledim -->"
fi
