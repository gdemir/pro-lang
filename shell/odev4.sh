#!/bin/bash

usage() {
    echo -e "\033[1m kullanım \033[0m: ${0##*/} <secim> "
    echo -e "\033[1m secim \033[0m:"
    echo "       u : kullanıcıları gösterir."
    echo "       g : grupları gösterir."
    echo "       d : dizinleri gösterir."
    exit 1
}

[ $# -eq 1 ] || usage

alan=$1
ifs_save="$IFS"
while read line; do
   IFS=":"
   set $line
   IFS=$ifs_save
   case $alan in
	[uU]) echo "user  => $1" ;;
	[gG]) echo "grub  => $5" ;;
	[dD]) echo "dizin => $7" ;;
	*) usage ;;
    esac
done </etc/passwd
