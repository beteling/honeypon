<?php


include 'db.php';

// AJAX PARA ELIMINAR EL CLIENTE DE HONEYPON
if((isset($_POST['idclienteparabaja']))){
	$idcliente = $_POST['idclienteparabaja'];
	$sqldeletecliente = "DELETE FROM clientes WHERE ID='$idcliente'"; 
	mysqli_query($enlace,$sqldeletecliente) or trigger_error(mysql_error()." in ".$sqlgdelimagen);
	
	$sqlverifysip = "SELECT * FROM sip WHERE `ID SIP` = $idcliente";
	$resultverifysip=mysqli_query($enlace,$sqlverifysip);

   if (mysqli_num_rows($resultverifysip) > 0){

        $sqldeletesip = "DELETE FROM sip WHERE `ID SIP` = $idcliente";
		mysqli_query($enlace,$sqldeletesip) or trigger_error(mysql_error()." in ".$sqldeletesip);
   }

    $sqlpppoeverify = "SELECT `ID Cliente` FROM pppoe WHERE `ID Cliente`= $idcliente";
	$resultpppoeverify=mysqli_query($enlace,$sqlpppoeverify);
    if (mysqli_num_rows($resultpppoeverify) > 0){
		$sqldeletepppoe = "DELETE FROM pppoe WHERE `ID Cliente` = $idcliente";
		mysqli_query($enlace,$sqldeletepppoe) or trigger_error(mysql_error()." in ".$sqldeletepppoe);
	}
        
        
}

// AJAX PARA ALTA DE CLIENTE
if((isset($_POST['altaclienteajax']))){
	$inputname = $_POST['inputname'];
	$inputdireccion = $_POST['inputdireccion'];
	$inputtelf = $_POST['inputtelf'];
	$inputdni = $_POST['inputdni'];
	$inputarrendpppoe = $_POST['inputarrendpppoe'];
	$inputcgnat = $_POST['inputcgnat'];
	$inputsip = $_POST['inputsip'];
	$selectplan = $_POST['selectplan'];
	$selectolt = $_POST['selectolt'];
	$inputextensionsip = $_POST['inputextensionsip'];
	$inputsecretsip = $_POST['inputsecretsip'];
	$actualdate = date("Y-m-d");
	
	
	if($inputcgnat == 'si'){ // Si es CGNAT
		$cgnat = 'si';
	}else{
		$cgnat = 'no';
	}

	// Obtener el siguiente ID de cliente
	$sqlnextindex = "SELECT `auto_increment` FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'clientes' AND TABLE_SCHEMA = 'honeypon'";
	$resultnextindex=mysqli_query($enlace,$sqlnextindex);
	$prodindex=mysqli_fetch_row($resultnextindex);
	$clienteidnext = $prodindex[0];
	
	$sqlplan = "SELECT ID FROM planes WHERE Nombre = '$selectplan' AND OLT = '$selectolt'";
	$resultsqlplan=mysqli_query($enlace,$sqlplan);
	$planid=mysqli_fetch_row($resultsqlplan);

	// Inserta al cliente en la base de datos
	$sqlinsertcliente = "INSERT INTO clientes (Nombre, Direccion, Telefono, DNI, Plan, olt, CGNAT, Fecha) VALUES ('$inputname', '$inputdireccion', '$inputtelf', '$inputdni', '$planid[0]', '$selectolt', '$cgnat', '$actualdate')";

	mysqli_query($enlace,$sqlinsertcliente) or trigger_error(mysql_error()." in ".$sqlinsertcliente);
	
	
	if($inputarrendpppoe == 'si'){ // Si el arrendamiento es por PPPOE
		
		$pppoenamelower = strtolower($inputname);
		$pppoeuser = str_replace(" ", "_", $pppoenamelower);
		$pppoesecret = $inputdni;
		
		// Inserta los datos de pppoe 
        $sqlinsertpppoe = "INSERT INTO pppoe (`ID Cliente`, Usuario, Password) VALUES ('$clienteidnext', '$pppoeuser', '$pppoesecret')";
		mysqli_query($enlace,$sqlinsertpppoe) or trigger_error(mysql_error()." in ".$sqlinsertpppoe);
            
	}
	
	if($inputsip == 'si'){ // Si el cliente tiene SIP
	
		// Inserta los datos sip
		$sqlinsertsip = "INSERT INTO sip (`ID SIP`, Cliente, Secret, Extension) VALUES ('$clienteidnext','$inputname','$inputsecretsip', '$inputextensionsip')";
		mysqli_query($enlace,$sqlinsertsip) or trigger_error(mysql_error()." in ".$sqlinsertsip);
	}
	
	echo json_encode(array('jsoninputname'=>$inputname,'jsoninputdireccion'=>$inputdireccion,'jsoninputtelf'=>$inputtelf,'jsoninputdni'=>$inputdni,'jsonselectplan'=>$selectplan,'jsonselectolt'=>$selectolt,'jsoninputextensionsip'=>$inputextensionsip,'jsoninputsecretsip'=>$inputsecretsip,'jsonactualdate'=>$actualdate,'jsonclienteidnext'=>$clienteidnext));
}
	
	
?>


