<?php
require 'g56.php';

if (!strlen(session_id())) {
	echo "session start!<br/>";
	g56::config(g56::path() . "lib/.g56.ini"); // config filename : .g56.ini
	session_start();
}

// kick
g56::run();
?>
