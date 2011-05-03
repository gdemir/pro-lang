<?php
echo !($connector = mysql_connect('localhost','root','12345')) ? 'Can\'t find ' . mysql_error() : 'databate succesfully connect';
echo !(mysql_select_db('ogrenci', $connector)) ? 'Can\'t find ' . mysql_error() : 'database select succesfully ';
$ad = $_POST['ad'];
$ps = $_POST['ps'];
mysql_query("insert into kul (ad, sifre) VALUES('$ad' , '$ps')");
?>
