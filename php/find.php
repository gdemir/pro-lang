<?php
echo !($connector = mysql_connect('localhost','root','12345')) ? 'Can\'t find ' . mysql_error() : 'databate succesfully connect';
echo !(mysql_select_db('Ogr', $connector)) ? 'Can\'t find ' . mysql_error() : 'database select succesfully ';
$ad = $_POST['ad'];
$ps = $_POST['ps'];
$result = mysql_query("select * from kul  where ad = '$ad' and sifre = '$ps'");
while ($row = mysql_fetch_assoc($result)) {
	echo "ogrenci bilgileri <br/>";
	echo $row['ad'] . "<br>";
	echo $row['sifre'];
}
?>
