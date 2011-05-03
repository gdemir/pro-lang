#!/bin/bash

man()
{
	echo -e "\033[1m NAME \033[0m"
	echo "     the assembly of file"
	echo -e "\033[1m USE \033[0m"
	echo "     up FILE..."
	exit 1
}

# program kullanma klavuzu .
if [ $# -eq 0 ];then
	man
fi

# olmayan bir dosya ismi uret .
while [ 1=1 ]
do
	file=up-$[$RANDOM%100]
	if [ ! -f $file ];then
		break
	fi
done

# girilen dosyalari uretilen dosya ismine doldur .
cat $* | while read line;
	do
		echo $line >> $file
	done
