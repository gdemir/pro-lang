<?php
if (mysql_connect('localhost', 'root', '12345')) {
	echo 'mysql succesfull connect';
else
	die('Can\'t find ' . mysql_error());

if (mysql_select_db('ogrenci')) {
	echo 'database select succesfull';
else
	die('Can\'t find ' . mysql_error());

$nm = $_POST['name'];
$ps = $_POST['password'];
mysql_query("insert into kul (ad, sifre) values('$nm' , '$ps')");
?>
