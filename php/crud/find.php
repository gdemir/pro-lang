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
$result = mysql_query("select * from kul  where ad = '$nm' and sifre = '$ps'");
while ($row = mysql_fetch_assoc($result)) {
	echo "ogrenci bilgileri <br/>";
	echo $row['ad'] . "<br>";
	echo $row['sifre'];
}
?>
