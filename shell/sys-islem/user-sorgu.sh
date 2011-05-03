#!/bin/sh

# home'dan bir geri dizinimize bakiyoruz .
path=$(readlink -f $HOME/..)

# klavyeden girdi aliyoruz .
echo "your username :"
read name

# kontrol ediyoruz .
if  ls $path/$name 2>/dev/null 1>&2; then
	echo "$name isminde kullanici var"
else
	echo "$name isminde kullanici yok"
fi
