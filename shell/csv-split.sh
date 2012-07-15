#!/bin/sh
while read line; do
	echo $line | awk -F, '{ print $1 }'>>ad.txt
	echo $line | awk -F, '{ print $2 }'>>sd.txt
	echo $line | awk -F, '{ print $3 }'>>no.txt
done <foo.txt
