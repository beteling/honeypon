<?php


$enlace = mysqli_connect("localhost", "honeypon", "pon", "honeyponv2");
$acentos = $enlace->query("SET NAMES 'utf8'");

if (!$enlace) {
						echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
						echo "errno de depuración: " . mysqli_connect_errno() . PHP_EOL;
						echo "error de depuración: " . mysqli_connect_error() . PHP_EOL;
						exit;
					};


?>
