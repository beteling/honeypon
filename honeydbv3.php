<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <title>Betelinka</title>
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no">
    <link rel="shortcut icon" href="images/logotitle.png"/>
    <link rel="bookmark" href="favicon_16.ico"/>
    <!-- site css -->
	
    <link rel="stylesheet" href="dist/css/site.min.css">
    <link type="text/css" rel="stylesheet" href="dist/css/style.css">
	<!-- <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'> -->
    <!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
      <script src="js/respond.min.js"></script>
    <![endif]-->
    
  </head>
  <body>
  
  <?php //Script que certifica todos los proyectos de forma automática
					include 'db.php';
					
							$sqlgetprod = "SELECT SN, `ONT ID` FROM ont";
							$resultgetprod=mysqli_query($enlace,$sqlgetprod);

							while ($row=mysqli_fetch_row($resultgetprod))
							{
							 
							$sn = $row[0];
							$ontid = $row[1];
							
							$explode = explode("/",$ontid); // Crea un array $explode
							$frame = $explode[0]; // Extrae indice [0] a $explode
							$slot = $explode[1]; // Extrae indice [1] a $explode
							$port = explode(' ',$explode[2])[0]; // Crea un array y extrae el indice [0]
							$idont = explode(' ',$explode[2])[1]; // Crea un array y extrae el indice [1]

													
							
							$sqlinsertfase = "UPDATE ont set frame = '$frame', slot = '$slot', port = '$port', ont_id='$idont' WHERE SN = '$sn'";
							mysqli_query($enlace,$sqlinsertfase) or trigger_error(mysql_error()." in ".$sqlinsertfase);
							
	
							}
					mysqli_close($enlace);	
					
				?>
	
  </body>
</html>
