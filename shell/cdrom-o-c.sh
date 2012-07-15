#!/bin/sh

while [ 1 = 1 ]
do
	# eject cdrom
	eject
	# pull cd rom tray back in
	eject -t
done
