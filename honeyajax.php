<?php


include 'db.php';


// AJAX PARA SELECCIONAR LAS OLTs DISPONIBLES DADO EL PLAN SELECCIONADO
if((isset($_POST['selectoltlist']))){
	$plan = $_POST['plan'];
	$resultarrayolt = array();

	//$sqlgetolt = "SELECT t1.Nombre, t1.ID FROM olt AS t1, planes AS t2 WHERE t2.ID = '$plan' AND t2.OLT = t1.ID";
	$sqlgetolt = "SELECT t1.Nombre, t1.ID FROM olt AS t1, planes AS t2, lineprofile_olt AS t3 WHERE t2.ID = '$plan' AND t2.ID = t3.id_lineprofile AND t1.ID = t3.id_olt";


	$resultgetolt=mysqli_query($enlace,$sqlgetolt);
		while ($rowolt=mysqli_fetch_row($resultgetolt))
			{

			$optionolt = array("optionolt"=>"<option value='".$rowolt[1]."'>".$rowolt[0]."</option>");
			$resultarrayolt[] = $optionolt;

			}

	echo json_encode(array('jsonresultolt'=>$resultarrayolt));
}

// AJAX PARA ELIMINAR EL CLIENTE DE HONEYPON
if((isset($_POST['idcliente_borrar']))){
	$idcliente = $_POST['idcliente_borrar'];

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

    $sqlbridgeverify = "SELECT `ID Cliente` FROM bridge WHERE `ID Cliente`= $idcliente";
	$resultbridgeverify=mysqli_query($enlace,$sqlbridgeverify);
    if (mysqli_num_rows($resultbridgeverify) > 0){
		$sqldeletebridge = "DELETE FROM bridge WHERE `ID Cliente` = $idcliente";
		mysqli_query($enlace,$sqldeletebridge) or trigger_error(mysql_error()." in ".$sqldeletebridge);
	}

	echo json_encode(array('jsoninput_idcliente'=>$idcliente));
}

// AJAX PARA DAR DE BAJA ADMINISTRATIVA AL CLIENTE DE HONEYPON
if((isset($_POST['idcliente_baja']))){
	$idcliente = $_POST['idcliente_baja'];

	$sqldeletecliente = "UPDATE clientes SET estado = 'baja' WHERE ID='$idcliente'";
	mysqli_query($enlace,$sqldeletecliente) or trigger_error(mysql_error()." in ".$sqldeletecliente);


	echo json_encode(array('jsoninput_idcliente'=>$idcliente));


}

// AJAX PARA DAR DE ALTA ADMINISTRATIVA AL CLIENTE DE HONEYPON
if((isset($_POST['idcliente_reactivar']))){
	$idcliente = $_POST['idcliente_reactivar'];

	$sql_reactivar_cliente = "UPDATE clientes SET estado = 'alta' WHERE ID='$idcliente'";
	mysqli_query($enlace,$sql_reactivar_cliente) or trigger_error(mysql_error()." in ".$sql_reactivar_cliente);


	echo json_encode(array('jsoninput_idcliente'=>$idcliente));

}


if((isset($_POST['alta_cliente_ajax']))){
	$arrayresult = array();
	$actualdate = date("Y-m-d");

	$inputname = $_POST['inputname'];
	$inputdireccion = $_POST['inputdireccion'];
	$inputtelf = $_POST['inputtelf'];
	$inputdni = $_POST['inputdni'];


	$selectplan = $_POST['selectplan'];
	$selectolt = $_POST['selectolt'];

	$inputextensionsip = $_POST['inputextensionsip'];
	$inputsecretsip = $_POST['inputsecretsip'];
	$inputserversip = $_POST['inputserversip'];

	$pppoeuser = $_POST['inputuserpppoe'];
	$pppoesecret = $_POST['inputpasspppoe'];

	if($_POST['inputcgnat'] == "true"){
		$cgnat = 'si';
	}else{
		$cgnat = 'no';
	}

	// Obtener el siguiente ID de cliente
	$sqlnextindex = "SELECT `auto_increment` FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'clientes' AND TABLE_SCHEMA = 'honeyponv2'";
	$resultnextindex=mysqli_query($enlace,$sqlnextindex);
	$prodindex=mysqli_fetch_row($resultnextindex);
	$clienteidnext = $prodindex[0];

	// Inserta al cliente en la base de datos
	$sqlinsertcliente = "INSERT INTO clientes (Nombre, Direccion, Telefono, DNI, Plan, olt, CGNAT, Fecha) VALUES ('$inputname', '$inputdireccion', '$inputtelf', '$inputdni', '$selectplan', '$selectolt', '$cgnat', '$actualdate')";
	mysqli_query($enlace,$sqlinsertcliente) or trigger_error(mysql_error()." in ".$sqlinsertcliente);

	if($_POST['inputarrendpppoe'] == "true"){
		$sqlinsertpppoe = "INSERT INTO pppoe (`ID Cliente`, Usuario, Password) VALUES ('$clienteidnext', '$pppoeuser', '$pppoesecret')";
		mysqli_query($enlace,$sqlinsertpppoe) or trigger_error(mysql_error()." in ".$sqlinsertpppoe);
		};

	if($_POST['inputbridge'] == "true"){
			$sqlinsertbridge = "INSERT INTO bridge (`ID Cliente`, puerto) VALUES ('$clienteidnext','1')";
			mysqli_query($enlace,$sqlinsertbridge) or trigger_error(mysql_error()." in ".$sqlinsertbridge);
		};

	if($_POST['inputsip'] == "true"){
			$sqlinsertsip = "INSERT INTO sip (`ID SIP`, Cliente, Secret, Extension, servidor) VALUES ('$clienteidnext','$inputname','$inputsecretsip', '$inputextensionsip','$inputserversip')";
			mysqli_query($enlace,$sqlinsertsip) or trigger_error(mysql_error()." in ".$sqlinsertsip);
		};






		#echo json_encode(array('result'=>$arrayresult));
		echo json_encode(array('jsoninputname'=>$inputname,'jsoninputdireccion'=>$inputdireccion,'jsoninputtelf'=>$inputtelf,'jsoninputdni'=>$inputdni,'jsonselectplan'=>$selectplan,'jsonselectolt'=>$selectolt,'jsoninputextensionsip'=>$inputextensionsip,'jsoninputsecretsip'=>$inputsecretsip,'jsonactualdate'=>$actualdate,'jsonclienteidnext'=>$clienteidnext));



};

if((isset($_POST['editar_cliente_ajax']))){

	$arrayresult = array();


	$input_id_cliente = $_POST['id_cliente'];
	$inputname = $_POST['editar_inputname'];
	$inputdireccion = $_POST['editar_inputdireccion'];
	$inputtelf = $_POST['editar_inputtelf'];
	$inputdni = $_POST['editar_inputdni'];


	$selectplan = $_POST['editar_selectplan'];
	$selectolt = $_POST['editar_selectolt'];

	$inputextensionsip = $_POST['editar_inputextensionsip'];
	$inputsecretsip = $_POST['editar_inputsecretsip'];
	$inputserversip = $_POST['editar_inputserversip'];

	$pppoeuser = $_POST['editar_inputuserpppoe'];
	$pppoesecret = $_POST['editar_inputpasspppoe'];

	if($_POST['editar_inputcgnat'] == "true"){
		$cgnat = 'si';
	}else{
		$cgnat = 'no';
	}


	// Actualiza los datos del cliente en la base de datos
	if($selectplan){
	    $sqlupdatecliente = "UPDATE clientes SET Nombre= '$inputname', Direccion= '$inputdireccion', Telefono= '$inputtelf', DNI= '$inputdni', Plan= $selectplan, olt= $selectolt, CGNAT= '$cgnat' WHERE ID = $input_id_cliente";
	}else{
	    $sqlupdatecliente = "UPDATE clientes SET Nombre= '$inputname', Direccion= '$inputdireccion', Telefono= '$inputtelf', DNI= '$inputdni', CGNAT= '$cgnat' WHERE ID = $input_id_cliente";		
	}
	
	mysqli_query($enlace,$sqlupdatecliente) or trigger_error(mysql_error()." in ".$sqlupdatecliente);

	// Actualiza los datos PPPOE
	if($_POST['editar_inputarrendpppoe'] == "true"){
		// Verificar si ya existen datos PPPOE
		$sql_pppoe_verify = "SELECT `ID Cliente` FROM pppoe WHERE `ID Cliente` = $input_id_cliente ";
		$result_sql_pppoe_verify=mysqli_query($enlace,$sql_pppoe_verify);
		if(mysqli_num_rows($result_sql_pppoe_verify) > 0){
			$sqlupdatepppoe = "UPDATE pppoe SET Usuario='$pppoeuser', Password='$pppoesecret' WHERE `ID Cliente` = $input_id_cliente";
		}else{
			$sqlupdatepppoe = "INSERT INTO pppoe (`ID Cliente`, Usuario, Password) VALUES ('$input_id_cliente', '$pppoeuser', '$pppoesecret')";
		}

	}else{
			$sqlupdatepppoe = "DELETE FROM pppoe WHERE `ID Cliente` = $input_id_cliente";
		}

		mysqli_query($enlace,$sqlupdatepppoe) or trigger_error(mysql_error()." in ".$sqlupdatepppoe);





	// Actualiza los datos SIP

	if($_POST['editar_inputsip'] == "true"){
		// Verificar si ya existen datos SIP
		$sql_sip_verify = "SELECT `ID SIP` FROM sip WHERE `ID SIP` = $input_id_cliente ";
		$result_sql_sip_verify=mysqli_query($enlace,$sql_sip_verify);
		if(mysqli_num_rows($result_sql_sip_verify) > 0){
			$sqlupdatesip = "UPDATE sip SET Extension='$inputextensionsip', Secret='$inputsecretsip', servidor = '$inputserversip' WHERE `ID SIP` = $input_id_cliente";
		}else{
			$sqlupdatesip = "INSERT INTO sip (`ID SIP`, Extension, Secret, servidor) VALUES ('$input_id_cliente', '$inputextensionsip', '$inputsecretsip', '$inputserversip')";
		}

	}else{
			$sqlupdatesip = "DELETE FROM sip WHERE `ID SIP` = $input_id_cliente";
		}

			mysqli_query($enlace,$sqlupdatesip) or trigger_error(mysql_error()." in ".$sqlupdatesip);

// PENDIENTE LO DE ABAJO

	// Actualiza los datos BRIDGE
	if($_POST['editar_inputbridge'] == "true"){
		// Verificar si ya existen datos BRIDGE
		$sql_bridge_verify = "SELECT `ID Cliente` FROM bridge WHERE `ID Cliente` = $input_id_cliente ";
		$result_sql_bridge_verify=mysqli_query($enlace,$sql_bridge_verify);
		if(mysqli_num_rows($result_sql_bridge_verify) < 1){

			$sqlupdatebridge = "INSERT INTO bridge (`ID Cliente`, Puerto) VALUES ('$input_id_cliente', 1)";
		}

	}else{
			$sqlupdatebridge = "DELETE FROM bridge WHERE `ID Cliente` = $input_id_cliente";
		}

			mysqli_query($enlace,$sqlupdatebridge) or trigger_error(mysql_error()." in ".$sqlupdatebridge);



		#echo json_encode(array('result'=>$arrayresult));
		echo json_encode(array('result'=>$sqlupdatecliente));


};

// AJAX PARA ALTA DE CLIENTE
if((isset($_POST['altaclienteajax']))){
	$actualdate = date("Y-m-d");

	$inputname = $_POST['inputname'];
	$inputdireccion = $_POST['inputdireccion'];
	$inputtelf = $_POST['inputtelf'];
	$inputdni = $_POST['inputdni'];


	$selectplan = $_POST['selectplan'];
	$selectolt = $_POST['selectolt'];

	$inputsip = $_POST['inputsip'];
	$inputextensionsip = $_POST['inputextensionsip'];
	$inputsecretsip = $_POST['inputsecretsip'];
	$inputserversip = $_POST['inputserversip'];

	$inputcgnat = $_POST['inputcgnat'];



	$inputbridge = $_POST['inputbridge'];

	$inputarrendpppoe = $_POST['inputarrendpppoe'];
	$pppoeuser = $_POST['inputuserpppoe'];
	$pppoesecret = $_POST['inputpasspppoe'];

	if($inputcgnat == 'si'){ // Si es CGNAT
		$cgnat = 'si';
	}else{
		$cgnat = 'no';
	}

	// Obtener el siguiente ID de cliente
	$sqlnextindex = "SELECT `auto_increment` FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'clientes' AND TABLE_SCHEMA = 'honeyponv2'";
	$resultnextindex=mysqli_query($enlace,$sqlnextindex);
	$prodindex=mysqli_fetch_row($resultnextindex);
	$clienteidnext = $prodindex[0];

	//$sqlplan = "SELECT ID FROM planes WHERE ID = '$selectplan' AND OLT = '$selectolt'";
	//$resultsqlplan=mysqli_query($enlace,$sqlplan);
	//$planid=mysqli_fetch_row($resultsqlplan);

	// Inserta al cliente en la base de datos
	$sqlinsertcliente = "INSERT INTO clientes (Nombre, Direccion, Telefono, DNI, Plan, olt, CGNAT, Fecha) VALUES ('$inputname', '$inputdireccion', '$inputtelf', '$inputdni', '$selectplan', '$selectolt', '$cgnat', '$actualdate')";

	mysqli_query($enlace,$sqlinsertcliente) or trigger_error(mysql_error()." in ".$sqlinsertcliente);


	if($inputarrendpppoe == 'si'){ // Si el arrendamiento es por PPPOE

		//$pppoenamelower = strtolower($inputname);
	//$pppoeuser = str_replace(" ", "_", $pppoenamelower);
		//$pppoesecret = $inputdni;

		// Inserta los datos de pppoe
        $sqlinsertpppoe = "INSERT INTO pppoe (`ID Cliente`, Usuario, Password) VALUES ('$clienteidnext', '$pppoeuser', '$pppoesecret')";
				mysqli_query($enlace,$sqlinsertpppoe) or trigger_error(mysql_error()." in ".$sqlinsertpppoe);

	}

	if($inputsip == 'si'){ // Si el cliente tiene SIP

		// Inserta los datos sip
		$sqlinsertsip = "INSERT INTO sip (`ID SIP`, Cliente, Secret, Extension, servidor) VALUES ('$clienteidnext','$inputname','$inputsecretsip', '$inputextensionsip','$inputserversip')";
		mysqli_query($enlace,$sqlinsertsip) or trigger_error(mysql_error()." in ".$sqlinsertsip);
	}

	if($inputbridge == 'si'){ // Si el cliente usa bridge

		// Inserta los datos sip
		$sqlinsertbridge = "INSERT INTO bridge (`ID Cliente`, puerto) VALUES ('$clienteidnext','1')";
		mysqli_query($enlace,$sqlinsertbridge) or trigger_error(mysql_error()." in ".$sqlinsertbridge);
	}

	echo json_encode(array('jsoninputname'=>$inputname,'jsoninputdireccion'=>$inputdireccion,'jsoninputtelf'=>$inputtelf,'jsoninputdni'=>$inputdni,'jsonselectplan'=>$selectplan,'jsonselectolt'=>$selectolt,'jsoninputsip'=>$inputsip,'jsoninputextensionsip'=>$inputextensionsip,'jsoninputsecretsip'=>$inputsecretsip,'jsonactualdate'=>$actualdate,'jsonclienteidnext'=>$clienteidnext));
}




if(isset($_POST['action'])){
	if($_POST['action'] == "consulta_servicio"){
		$trclass = 'default';
		$type = $_POST["type"];
		$inputtype = $_POST["inputtype"];
		$olt = $_POST["olt"];
		$slot =  $_POST["slot"];
		$port =  $_POST["port"];
		$chk_bajas =  $_POST["chk_bajas"];


		$sconsultabase= "SELECT t1.SN AS SN, t1.frame AS frame, t1.slot AS slot, t1.port AS port, t1.ont_id AS ont_id, t1.Modelo AS modelo,
							t1.`ID Servicio` AS id_servicio, t1.Linea AS linea,
							t2.DNI AS nif, t2.Nombre AS nombrecliente, t2.Direccion AS dircliente, t2.Telefono AS tlfcliente, t2.CGNAT AS cgnat,
							t5.Nombre AS olt,
							t3.Nombre AS plan,
							t4.Usuario AS usuariopppoe, t4.Password AS contraseñapppoe, t4.`ID Cliente` AS idpppoe_verify, t6.`ID SIP` AS idsip_verify, t7.`ID Cliente` AS idbridge_verify
							FROM ont t1
							LEFT JOIN clientes t2 ON t2.ID = t1.`ID Servicio`
							LEFT JOIN planes t3 ON t3.ID = t2.`Plan`
							LEFT JOIN pppoe t4 ON t4.`ID Cliente` = t1.`ID Servicio`
							LEFT JOIN olt t5 ON t5.ID = t2.olt
							LEFT JOIN sip t6 ON t6.`ID SIP` = t1.ID
							LEFT JOIN bridge t7 ON t7.`ID Cliente` = t1.ID
							WHERE 1";

		$consultabase= "SELECT t1.ID AS id_servicio, t2.SN AS SN, t2.frame AS frame, t2.slot AS slot, t2.port AS port, t2.ont_id AS ont_id, t2.Modelo AS modelo,
							t2.Linea AS linea,
							t1.DNI AS nif, t1.Nombre AS nombrecliente, t1.Direccion AS dircliente, t1.Telefono AS tlfcliente, t1.CGNAT AS cgnat,
							t5.Nombre AS olt,
							t3.Nombre AS plan,
							t4.Usuario AS usuariopppoe, t4.Password AS contraseñapppoe, t4.`ID Cliente` AS idpppoe_verify,
							t6.`ID SIP` AS idsip_verify, t7.`ID Cliente` AS idbridge_verify,
							t1.estado AS estado_cliente
							FROM clientes t1
							LEFT JOIN ont t2 ON t1.ID = t2.`ID Servicio`
							LEFT JOIN planes t3 ON t3.ID = t1.`Plan`
							LEFT JOIN pppoe t4 ON t4.`ID Cliente` = t1.ID
							LEFT JOIN olt t5 ON t5.ID = t1.olt
							LEFT JOIN sip t6 ON t6.`ID SIP` = t1.ID
							LEFT JOIN bridge t7 ON t7.`ID Cliente` = t1.ID
							WHERE 1";



		# CONSULTA OLT
		$sqlseleccionolt = " AND t1.olt= $olt";
		if($olt == 'all'){
			$consulta = $consultabase; # Todas las OLT
		}else{
			$consulta = $consultabase.$sqlseleccionolt; # OLT concreta
		}


		# CONSULTA SLOT
		$constructslot = str_replace(","," OR t2.slot = ", $slot);
		$sqlseleccionslot = " AND (t2.slot=".$constructslot.")";
		$consulta = $consulta.$sqlseleccionslot;

		#CONSULTA PORT
		$constructport = str_replace(","," OR t2.port = ", $port);
		$sqlseleccionport = " AND (t2.port=".$constructport.")";
		$consulta = $consulta.$sqlseleccionport;



		# Filtro por entrada de NIF o SN

		if($type == "nif"){
			$sqlnif = " AND t1.DNI = '$inputtype'";
			$consulta = $consultabase.$sqlnif;

		}else if($type == "sn"){
			$sqlsn = " AND t2.SN = '$inputtype'";
			$consulta = $consultabase.$sqlsn;
		}else if($chk_bajas == "true"){
			$consulta = $consulta."OR t2.SN is null AND (t1.estado = 'baja' OR t1.estado = 'alta')"; # Añade clientes sin ONT asociada
		}else{
			$consulta = $consulta."OR t2.SN is null AND t1.estado = 'alta'"; # Añade clientes sin ONT asociada
		};

		# Lista solo clientes dados de altas




		//$consulta = $consulta."OR t2.SN is null"; # Añade clientes sin ONT asociada
		$sqlorder = " ORDER BY t2.`ID Servicio` ASC";
		$sqlorder = " ORDER BY t1.ID DESC";
		$consulta = $consulta.$sqlorder;
		//$consulta = $consulta.$type.$inputtype;

		$sqlconsulta = mysqli_query($enlace,$consulta);
		$arrayconsulta = array();
		while ($row=mysqli_fetch_assoc($sqlconsulta)){
			$ontsn = $row['SN'];
			$nifclient = $row['nif'];
			$oltcliente = $row['olt'];
			$fspontid=$row['frame']."/".$row['slot']."/".$row['port']." ".$row['ont_id'];
			$modelo = $row['modelo'];
			$idservicio = $row['id_servicio'];
			$linea = $row['linea'];
			$plan = $row['plan'];
			$idsip= $row['idsip_verify'];
			$idbridge= $row['idbridge_verify'];
			$idpppoe = $row['idpppoe_verify'];
			$estado_cliente = $row['estado_cliente'];

			if ($estado_cliente == "alta"){
				$state_class = "warning";
				$state_class_action = "
					<button title='Baja cliente' type='button' onclick = 'modal_baja_cliente(".$idservicio.")' class='btn btn-warning btn-xs' text-align=center' style='margin-left:10px'>
						<i class='fas fa-user-minus' style='margin-right:0.8px'></i>
					</button>";
				$state_class_register_option ="
				<button id='registeront-".$idservicio."' title='Alta de servicio' type='button' onclick='asociar_ont(".$idservicio.")' data-toggle='modal' class='btn btn-success btn-xs' text-align=center' style='margin-left:10px'>
					<i class='fas fa-upload' style='margin-right:0.8px'></i>
				</button>";
			}else{
				$state_class = "danger";
				$state_class_action = "
				<button title='Reactivar cliente' type='button' onclick = 'modal_reactivar_cliente(".$idservicio.")' class='btn btn-success btn-xs' text-align=center' style='margin-left:10px'>
					<i class='fas fa-user-plus' style='margin-right:0.8px'></i>
				</button>";
				$state_class_register_option ="";

			}

			if (!$ontsn){
				$trclass=$state_class;
				$fspontid="";
			  $register_option=$state_class_register_option;
				$button_option = $state_class_action;
				$delete_option = "
				<button disabled title='Borrar cliente' type='button' onclick = 'modal_borrar_cliente(".$idservicio.")' class='btn btn-danger btn-xs' text-align=center' style='margin-left:10px'>
					<i class='fas fa-user-minus' style='margin-right:0.8px'></i>
				</button>";


			}else{
				$trclass="default";
				$fspontid=$row['frame']."/".$row['slot']."/".$row['port']." ".$row['ont_id'];
				$register_option="";
				$button_option = "";
				$delete_option = "
				<button id='ontdel-".$idservicio."' title='Baja de servicio' type='button' onclick = 'modal_baja_servicio(".$idservicio.")' data-toggle='modal' class='btn btn-danger btn-xs' text-align=center' style='margin-left:10px'>
					<i class='fas fa-download' style='margin-right:0.8px'></i>
				</button>";
				$baja_option = "";
			};

			if ($idsip){
				$sip_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='Servicio Configurado' class='fas fa-phone'></i>";
			}else{
				$sip_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='Sin Servicio' class='fas fa-phone-slash'></i>";
			}

			if ($idbridge){
				$bridge_class = "<span title='Modo Bridge'><i style='margin-left:-15px;color:#FEA126;float: right;padding: 10px;'  class='fas fa-hdd'></i><i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' class='fas fa-arrows-alt-v'></i></span>";
			}else{
				$bridge_class = "<i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' title='Modo NAT' class='fas fa-filter'></i>";
			}

			if ($idpppoe){
				$pppoe_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='PPPOE Activado' class='fas fa-address-card'></i>";
			}else{
				$pppoe_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='PPPOE Desactivado' class='fas fa-address-card'></i>";
			}





        if ($linea == "online"){
					$tdlinea = "<td class='tableontlist' style='color:green'>".$linea."</td>";
				}else if ($linea == "offline"){
					$tdlinea = "<td class='tableontlist' style='color:#C9302C'>".$linea."</td>";
				}else{
					$tdlinea = "<td class='tableontlist' style='color:#FEA126'>N/A</td>";
				};


			$data = array(
			"registroont"=>
			"<tr class='".$trclass."' id='".$idservicio."'>
				<td  class='tableontlist'>".$ontsn."</td>
				<td  class='tableontlist'>".$fspontid."</td>
				<td  class='tableontlist'>".$modelo."</td>
				<td  class='tableontlist'>".$idservicio."</td>
				<td  class='tableontlist'>".$plan."</td>
				".$tdlinea."
				<td>

					<button id='clientassoc-".$idservicio."' title='Informacion del cliente' type='button' class='btn btn-info btn-xs' data-target='#modal-cliente-asociado' onclick='clientassoc(".$idservicio.");' data-toggle='modal' style='margin-left:10px'>
						<i class='fas fa-info-circle'></i>
					</button>
					<button id='edit_clientassoc-".$idservicio."' title='Editar cliente' class='btn btn-secondary btn-xs' name='modificarcliente' value='botonedit' onclick='edit_clientassoc(".$idservicio.");' style='margin-left:10px'><i class='fas fa-edit'></i></button>
					".$register_option."
					".$button_option."
					".$delete_option."
					".$sip_class."
					".$bridge_class."
					".$pppoe_class."

				</td>
				<td class='tableontlist colnif hidden'>".$nifclient."</td>
			</tr>");
		$arrayconsulta[] = $data;
		}
		echo json_encode(array('result'=>$arrayconsulta));
		//echo json_encode(array('result'=>$arrayconsulta,'consulta'=>$consulta));


	}elseif($_POST['action'] == "consulta_pendientes"){
		$trclass = 'default';
		$consultabase= "SELECT t1.ID AS id_servicio,
							t1.DNI AS nif, t1.Nombre AS nombrecliente, t1.Direccion AS dircliente, t1.Telefono AS tlfcliente, t1.CGNAT AS cgnat,
							t5.Nombre AS olt,
							t3.Nombre AS plan,
							t4.Usuario AS usuariopppoe, t4.Password AS contraseñapppoe, t4.`ID Cliente` AS idpppoe_verify,
							t6.`ID SIP` AS idsip_verify, t7.`ID Cliente` AS idbridge_verify,
							t1.estado AS estado_cliente
							FROM clientes t1
							LEFT JOIN ont t2 ON t1.ID = t2.`ID Servicio`
							LEFT JOIN planes t3 ON t3.ID = t1.`Plan`
							LEFT JOIN pppoe t4 ON t4.`ID Cliente` = t1.ID
							LEFT JOIN olt t5 ON t5.ID = t1.olt
							LEFT JOIN sip t6 ON t6.`ID SIP` = t1.ID
							LEFT JOIN bridge t7 ON t7.`ID Cliente` = t1.ID
							WHERE 1 AND t2.SN is null AND t1.estado = 'alta'";


							$sqlorder = " ORDER BY t1.ID DESC";
							$consulta = $consultabase.$sqlorder;
							//$consulta = $consulta.$type.$inputtype;

							$sqlconsulta = mysqli_query($enlace,$consulta);
							$arrayconsulta = array();

	while ($row=mysqli_fetch_assoc($sqlconsulta)){
		$nifclient = $row['nif'];
		$nombre_cliente = $row['nombrecliente'];
		$direccion_cliente = $row['dircliente'];
		$telefono_cliente = $row['tlfcliente'];
		$oltcliente = $row['olt'];
		$idservicio = $row['id_servicio'];
		$plan = $row['plan'];
		$idsip= $row['idsip_verify'];
		$idbridge= $row['idbridge_verify'];
		$idpppoe = $row['idpppoe_verify'];
		$estado_cliente = $row['estado_cliente'];



			$state_class = "warning";
			$state_class_register_option ="
			<button id='registeront-".$idservicio."' title='Alta de servicio' type='button' onclick='asociar_ont(".$idservicio.")' data-toggle='modal' class='btn btn-success btn-xs' text-align=center' style='margin-left:10px'>
				<i class='fas fa-upload' style='margin-right:0.8px'></i>
			</button>";



			$trclass=$state_class;
			$fspontid="";
		  $register_option=$state_class_register_option;
			$delete_option = "
			<button disabled title='Borrar cliente' type='button' onclick = 'modal_borrar_cliente(".$idservicio.")' class='btn btn-danger btn-xs' text-align=center' style='margin-left:10px'>
				<i class='fas fa-user-minus' style='margin-right:0.8px'></i>
			</button>";



		if ($idsip){
			$sip_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='Servicio Configurado' class='fas fa-phone'></i>";
		}else{
			$sip_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='Sin Servicio' class='fas fa-phone-slash'></i>";
		}

		if ($idbridge){
			$bridge_class = "<span title='Modo Bridge'><i style='margin-left:-15px;color:#FEA126;float: right;padding: 10px;'  class='fas fa-hdd'></i><i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' class='fas fa-arrows-alt-v'></i></span>";
		}else{
			$bridge_class = "<i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' title='Modo NAT' class='fas fa-filter'></i>";
		}

		if ($idpppoe){
			$pppoe_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='PPPOE Activado' class='fas fa-address-card'></i>";
		}else{
			$pppoe_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='PPPOE Desactivado' class='fas fa-address-card'></i>";
		}





      //if ($linea == "online"){
				//$tdlinea = "<td class='tableontlist' style='color:green'>".$linea."</td>";
			//}else if ($linea == "offline"){
				//$tdlinea = "<td class='tableontlist' style='color:#C9302C'>".$linea."</td>";
			//}else{
				//$tdlinea = "<td class='tableontlist' style='color:#FEA126'>N/A</td>";
			//};


		$data = array(
		"registroont"=>
		"<tr class='".$trclass."' id='".$idservicio."'>
			<td  class='tableontlist'>".$nombre_cliente."</td>
			<td  class='tableontlist'>".$direccion_cliente."</td>
			<td  class='tableontlist'>".$nifclient."</td>
			<td  class='tableontlist'><a href=tel:".$telefono_cliente.">$telefono_cliente</a></td>
			<td  class='tableontlist'>".$idservicio."</td>
			<td  class='tableontlist'>".$plan."</td>

			<td>

				<button id='clientassoc-".$idservicio."' title='Informacion del cliente' type='button' class='btn btn-info btn-xs' data-target='#modal-cliente-asociado' onclick='clientassoc(".$idservicio.");' data-toggle='modal' style='margin-left:10px'>
					<i class='fas fa-info-circle'></i>
				</button>
				".$register_option."
				".$sip_class."
				".$bridge_class."
				".$pppoe_class."

			</td>
			<td class='tableontlist colnif hidden'>".$nifclient."</td>
		</tr>");
		$arrayconsulta[] = $data;
		}
		echo json_encode(array('result'=>$arrayconsulta));

	}elseif($_POST['action'] == "getclientassoc"){ // Extrae datos de cliente al pulsar botón de cliente asociado
		$idservicio = $_POST["idservicio"];

		$ifcgnat = "<i class='fa fa-times' style='color:#ED5565;font-size:15px'>";
		$pppoe = "<i class='fa fa-times' style='color:#ED5565;font-size:15px'>";
		$sip = "<i class='fa fa-times' style='color:#ED5565;font-size:15px'>";
		$bridge = "<i class='fa fa-times' style='color:#ED5565;font-size:15px'>";

		$consulta= "SELECT
							t1.DNI AS nif, t1.Nombre AS nombrecliente, t1.Direccion AS dircliente, t1.Telefono AS tlfcliente, t1.CGNAT AS cgnat,
							t4.Nombre AS olt,
							t2.Nombre AS plan,
							t3.Usuario AS usuariopppoe, t3.Password AS contraseñapppoe,
							t5.Secret AS sipsecret, t5.Extension AS sipextension, t7.Dominio AS sipserver,
							t6.`ID Cliente` AS bridge, t8.SN AS numero_serie
							FROM clientes t1
							LEFT JOIN planes t2 ON t2.ID = t1.`Plan`
							LEFT JOIN pppoe t3 ON t3.`ID Cliente` = t1.ID
							LEFT JOIN olt t4 ON t4.ID = t1.olt
							LEFT JOIN sip t5 ON t5.`ID SIP` = t1.ID
							LEFT JOIN bridge t6 ON t6.`ID Cliente` = t1.ID
							LEFT JOIN serversip t7 ON t7.ID = t5.`servidor`
							LEFT JOIN ont t8 ON t8.`ID Servicio` = t1.ID
							WHERE t1.ID = $idservicio";


		$sqlconsulta = mysqli_query($enlace,$consulta);

		$row=mysqli_fetch_assoc($sqlconsulta);

		$nombre = $row['nombrecliente'];
		$dircliente = $row['dircliente'];
		$tlfcliente = $row['tlfcliente'];
		$nif = $row['nif'];
		$plan = $row['plan'];
		$olt = $row['olt'];
		$cgnat = $row['cgnat'];
		$sn = $row['numero_serie'];

		$userpppoe =  $row['usuariopppoe'];
		$passpppoe =  $row['contraseñapppoe'];

		$sipextension =  $row['sipextension'];
		$sipsecret =  $row['sipsecret'];
		$sipserver =  $row['sipserver'];

		$idbridge =  $row['bridge'];

		if($sn != null){
			$has_service = true;
		}else{
			$has_service = false;
		}

		if($cgnat == 'si'){
			$ifcgnat = "<i class='fa fa-check' style='color:#31CEAD;font-size:15px'>";
		};

		if($userpppoe){
			$pppoe = "<i class='fa fa-check' onclick='showontpppoedata()' style='cursor:pointer;color:#31CEAD;font-size:15px'>";
		};
		if($sipextension){
			$sip = "<i class='fa fa-check' onclick='showontsipdata()' style='cursor:pointer;color:#31CEAD;font-size:15px'>";
		};

		if($idbridge){
			$bridge = "<i class='fa fa-check' style='color:#31CEAD;font-size:15px'>";
		};


		echo json_encode(array('nombre'=>$nombre,'dircliente'=>$dircliente,'tlfcliente'=>$tlfcliente,'nif'=>$nif,'plan'=>$plan,'olt'=>$olt,'ifcgnat'=>$ifcgnat,
		'pppoe'=>$pppoe,'passpppoe'=>$passpppoe,'userpppoe'=>$userpppoe,
		'sip'=>$sip,'sipextension'=>$sipextension,'sipserver'=>$sipserver,'sipsecret'=>$sipsecret,
		'bridge'=>$bridge, 'has_service' => $has_service));

	}elseif($_POST['action'] == "get_olt_list"){
		$sqlselectolt = "SELECT ID, Nombre, IP FROM olt";
		$resultselectolt=mysqli_query($enlace,$sqlselectolt);
		$arrayconsulta = array();
		while($fila=mysqli_fetch_row($resultselectolt))
		{
			$id = $fila[0];
			$nombre = $fila[1];
			$ip = $fila[2];
			$data = array(
			"registro_olt"=>
			"<option class='olt' value=".$id.">".$nombre." (".$ip.")</option>");

			$arrayconsulta_olt[] = $data;


		}

		echo json_encode(array('oltlist'=>$arrayconsulta_olt));

	}elseif($_POST['action'] == "get_planes_list"){
		$sqlselectplan = "SELECT ID, Nombre FROM planes GROUP BY Nombre";
		$resultselectplan=mysqli_query($enlace,$sqlselectplan);
		$arrayconsulta = array();
		while($fila=mysqli_fetch_row($resultselectplan))
		{
			$id = $fila[0];
			$nombre = $fila[1];

			$data = array(
			"registro_plan"=>
			"<option class='plan' value=".$id.">".$nombre."</option>");

			$arrayconsulta_plan[] = $data;


		}

		echo json_encode(array('planlist'=>$arrayconsulta_plan));

	}elseif($_POST['action'] == "get_serversip_list"){
		$sqlselectserversip = "SELECT ID, Dominio FROM serversip GROUP BY ID";
		$resultselectserversip=mysqli_query($enlace,$sqlselectserversip);
		$arrayconsulta = array();
		while($fila=mysqli_fetch_row($resultselectserversip))
		{
			$id = $fila[0];
			$dominio = $fila[1];
			$data = array(
			"registro_serversip"=>
			"<option class='servidor_sip' value=".$id.">".$dominio."</option>");

			$arrayconsulta_serversip[] = $data;


		}

		echo json_encode(array('serversiplist'=>$arrayconsulta_serversip));
	}
}

?>
