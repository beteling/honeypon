<?php

include 'db.php';

?>


<!--Desactiva el user agent stylesheet-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Honeypon</title>
	<link rel="shortcut icon" href="/honeypon/images/logotitle.png">

     <!-- CSS Datatables -->
	<link rel="stylesheet" href="datatables/jquery.dataTables.min.css">
	<link rel="stylesheet" href="datatables/datatables.css">
	<link rel="stylesheet" href="datatables/datatables.min.css">
	<link rel="stylesheet" href="datatables/buttons.dataTables.min.css">

    <link rel="stylesheet" href="css/site.min.css">
	<link rel="stylesheet" href="css/font-awesome.css">
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link rel="stylesheet" href="css/master/main.css">
	<link rel="stylesheet" href="css/master/main.min.css">
	<link rel="stylesheet" href="css/master/main.rtl.css">
	<link rel="stylesheet" href="css/master/main.rtl.min.css">
	<link rel="stylesheet" href="css/master/theme.css">
	<link rel="stylesheet" href="css/master/theme.min.css">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">

	<!-- CSS Multiselect -->
	<link type="text/css" rel="stylesheet" href="multiselect/dist/css/bootstrap-multiselect.css">

	<!-- icheck -->
    <link type="text/css" rel="stylesheet" href="chk/skins/all.css">


    <script src="/honeypon/js/jquery.min.js"></script>
    <script src="/honeypon/js/bootstrap.min.js"></script>
	<script src="/honeypon/js/scripts.js"></script>

	<!-- iCheck js -->
	<script type="text/javascript" src="chk/icheck.js"></script>
	<script type="text/javascript" src="chk/icheck.min.js"></script>

	<!-- Scripts Multiselect -->
	<script type="text/javascript" src="multiselect/dist/js/bootstrap-multiselect.js"></script>

    <!-- Scripts Datatables -->
    <script type="text/javascript" src="datatables/datatables.js"></script>
	<script type="text/javascript" src="datatables/datatables.min.js"></script>
    <script type="text/javascript" src="datatables/dataTables.buttons.min.js"></script>
    <script type="text/javascript" src="datatables/jszip.min.js"></script>
    <script type="text/javascript" src="datatables/pdfmake.min.js"></script>
    <script type="text/javascript" src="datatables/vfs_fonts.js"></script>
    <script type="text/javascript" src="datatables/buttons.html5.min.js"></script>
	<script type="text/javascript" src="datatables/buttons.print.min.js"></script>

  </head>
  <body>

  <div class="container-fluid">
	<div class="col-md-12">
	<h1>
		<img alt="honeypon logo" src="/honeypon/images/honeyponbete.png" style="margin-bottom:15px" />
			<a href="/honeypon/logout.py" style="text-decoration: none;font-size: 15px;float:right">Cerrar sesión&nbsp;<span class="glyphicon glyphicon-log-out"></span></a>
		<img alt="telsinetworx logo" src="/honeypon/images/telsilogo.jpg" style="float:right;margin-top:15px;width: 300px;" />
    </h1>
	</div>

	<div class="row">
		<div class="col-md-12">
				<div class="tabbable" >
					<div class="col-md-12">
					<ul class="nav nav-tabs nav-justified" align="center">
						<li>
							<a id='main' class="menuobject" href="main.py" style="color:#f5f5f5"><span class="glyphicon glyphicon-align-justify"></span><b>&nbsp;&nbsp;INICIO</b></a>
						</li>

						<li>
							<a id='menuont' class="menuobject" href="menuont.php" style="color:#f5f5f5"><span class="glyphicon glyphicon-hdd"></span><b>&nbsp;&nbsp;ONT</b></a>
						</li>
						<li>
							<a id='menucliente' class="menuobject" href="menucliente.py" style="color:#f5f5f5"><span class="fa fa-users"></span><b>&nbsp;&nbsp;CLIENTES</b></a>
						</li>
						<li>
							<a id='menuplanes' class="menuobject" href="menuplanes.py" style="color:#f5f5f5"><img style="width:18px" src="images/fiber.png"></img><b>&nbsp;&nbsp;PLANES</b></a>
						</li>
						<li>
							<a id='menuolt' class="menuobject" href="menuolt.py"  style="color:#f5f5f5"><span class="glyphicon glyphicon-tasks"></span><b>&nbsp;&nbsp;OLT</b></a>
						</li>

					</ul>
					</div>

					<div class="tab-content">

						<div class='col-md-12' style='margin-bottom:20px;margin-top:20px'>
							<table class='table table-striped'>

							<thead>
							  <tr style='color:#195F82'>
								<th>Tipo</th>
								<th class='columnainputtype hidden'>Valor</th>
								<th class='columnafiltro'>OLT</th>
								<th class='columnafiltro'>Tarjeta</th>
								<th class='columnafiltro'>Puerto</th>


							 </tr>
							 </thead>
							<tbody>
							 <tr>
								<td>
										<div class='form-group-sm'>
											<div style='max-width:150px'>
													<select id='seltype' onchange='tipofiltroont()' style='font-size:14px' class='form-control' >
														<option value='filtro' selected>FILTRO</option>
														<option value='nif'>DNI Cliente</option>
														<option value='sn'>ONT SN</option>
													</select>

											</div>
										</div>
								</td>

								<td class='columnainputtype hidden'>
									<div class='form-group-sm'>
											<div style='max-width:150px'>
													<input type='text' class='form-control' id='inputtype' name='inputtype'/>

											</div>
									</div>

								</td>

								<td class='columnafiltro'>
									<div class='form-group-sm'>

										<div style='max-width:150px'>
											<select id='selectolt' style='font-size:14px' class='form-control' >
											<option value='all' selected>TODAS</option>
									

											</select>
										</div>
									</div>
								</td>

								<td class='columnafiltro'>
									<div class='form-group-sm'>

										<div style='max-width:150px'>
											<select id='selectslot' multiple="multiple" style='font-size:14px' class='form-control' >
											<option value='0' >0</option>
											<option value='1' >1</option>
											<option value='2' >2</option>
											<option value='3' >3</option>
											<option value='4' >4</option>
											<option value='5' >5</option>
											<option value='6' >6</option>
											<option value='7' >7</option>
											<option value='8' >8</option>
											</select>
										</div>
									</div>
								</td>

								<td class='columnafiltro'>
									<div class='form-group-sm'>

										<div style='max-width:150px'>
											<select id='selectport' multiple="multiple" style='font-size:14px' class='form-control' >
											<option value='0' >0</option>
											<option value='1' >1</option>
											<option value='2' >2</option>
											<option value='3' >3</option>
											<option value='4' >4</option>
											<option value='5' >5</option>
											<option value='6' >6</option>
											<option value='7' >7</option>
											<option value='8' >8</option>
											<option value='9' >9</option>
											<option value='10' >10</option>
											<option value='11' >11</option>
											<option value='12' >12</option>
											<option value='13' >13</option>
											<option value='14' >14</option>
											<option value='15' >15</option>

											</select>
										</div>
									</div>
								</td>


							 </tr>
							 </tbody>
							 </table>
								<button style='float:right' type='button' name='' onclick='consultaront();' class='btn btn-info'>Consultar</button>
							</div>

						<span id='spantablaont' ></span>
					<!--Comienzo tabla ONT, Cliente u OLT-->





					</div>
				</div>
		</div>
	</div>

	 <!-- Modal -->
		<div id="modal-cliente-asociado" class="modal fade" role="dialog">
			<div class="modal-dialog">

							<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header" style="text-align:center; background-color:#FEA126">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title" style="font-size:20px; color:white;">Datos de cliente</h4>
				</div>
					<div class="modal-body">
						<div class='row'>
							<div class='col-md-12'>
								<h4 style="color:#286090;text-align:center;margin-bottom:20px">- Datos personales -</h4>
								<div style='padding-bottom: 15px;' class="col-md-6">

									<label for="inputnamecliente" style="color:#286090">
										Nombre
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='nameassoc' >

									</span>
								</div>
								<div style='padding-bottom: 15px;' class="col-md-6">

									<label for="inputdireccion" style="color:#286090">
										Dirección
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='dirassoc' >

									</span>

								</div>
								<div style='padding-bottom: 15px;' class="col-md-6">

									<label for="inputtelf"  style="color:#286090">
										Teléfono
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='tlfassoc'>

									</span>
								</div>
								<div style='padding-bottom: 15px;' class="col-md-6">

									<label for="inputdni"  style="color:#286090">
										DNI
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='nifassoc'>

									</span>
								</div>
							</div>
						</div>
						<hr>
						<div class='row'>
							<div class='col-md-12'>
								<h4 style="color:#286090;text-align:center; margin-bottom:20px">- Información del servicio -</h4>
								<div style='padding-bottom: 15px;'  class="col-md-6">
									<label for="selectplan" style="color:#286090">
										Paquete de datos
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='planassoc'>

									</span>
								</div>
								<div style='padding-bottom: 15px;'  class="col-md-6">
									<label for="selectolt"  style="color:#286090">
										OLT
									</label><br>
									<span class="badge badge-info editable" style="font-size: 12px;background-color:#195f82bf;" id='oltassoc'>

									</span>
								</div>
							</div>
						</div>
					</div>
						<div class="modal-footer" style='text-align: left;'>
							<div class='col-md-3'>
								<span class="badge badge-info" style='background-color:#E5DAB7; color:#676262'>
								   PPPOE <span id="pppoestatus"></span>
								</span>
							</div>
							<div class='col-md-3'>
								<span class="badge badge-info" style='background-color:#E5DAB7; color:#676262' >
								   CG-NAT <span id="cgnatstatus"></span>
								</span>
							</div>
							<div class='col-md-3'>
								<span class="badge badge-info" style='background-color:#E5DAB7; color:#676262'  >
								   BRIDGE <span id="bridgestatus"></span>
								</span>
							</div>
							<div class='col-md-3'>
								<span class="badge badge-info" style='background-color:#E5DAB7; color:#676262' >
								   SIP <span id="sipstatus"></span>
								</span>
							</div>


							<div class='row pppoedata hidden'>
								<div class='col-md-12'>
									<h4 style="color:#286090;text-align:center; margin-bottom:20px">- Datos PPPOE -</h4>
									<div style='padding-bottom: 15px;'  class="col-md-6">
										<label for="pppoeuser" style="color:#286090">
											Usuario PPPOE
										</label><br>
										<span class="badge badge-info editable" style="background-color:#E5DAB7; color:#676262" id='pppoeuser'>

										</span>
									</div>
									<div style='padding-bottom: 15px;'  class="col-md-6">
										<label for="pppoesecret"  style="color:#286090">
											Contraseña PPPOE
										</label><br>
										<span class="badge badge-info editable" style="background-color:#E5DAB7; color:#676262" id='pppoesecret'>

										</span>
									</div>
								</div>
							</div>

							<div class='row sipdata hidden'>
								<div class='col-md-12'>
									<h4 style="color:#286090;text-align:center; margin-bottom:20px">- Datos SIP -</h4>
									<div style='padding-bottom: 15px;'  class="col-md-6">
										<label for="sipextension" style="color:#286090">
											Extension SIP
										</label><br>
										<span class="badge badge-info editable" style="background-color:#E5DAB7; color:#676262" id='sipextension'>

										</span>
									</div>
									<div style='padding-bottom: 15px;'  class="col-md-6">
										<label for="sipsecret"  style="color:#286090">
											Secret SIP
										</label><br>
										<span class="badge badge-info editable" style="background-color:#E5DAB7; color:#676262" id='sipsecret'>

										</span>
									</div>
									<div style='padding-bottom: 15px;'  class="col-md-6">
										<label for="sipserver"  style="color:#286090">
											Servidor SIP
										</label><br>
										<span class="badge badge-info editable" style="background-color:#E5DAB7; color:#676262" id='sipserver'>

										</span>
									</div>
								</div>
							</div>

						</div>

			</div>

			</div>
		</div>
					<!-- Modal -->

	<script>
									$(function() {

										$('#selectslot').multiselect({
											includeSelectAllOption: true,
											selectAll: false,
											allSelectedText: 'TODAS'

											})
											.multiselect('selectAll', false)
											.multiselect('updateButtonText');

										$('#selectport').multiselect({
											includeSelectAllOption: true,
											selectAll: false,
											allSelectedText: 'TODOS'

											})
											.multiselect('selectAll', false)
											.multiselect('updateButtonText');
										});





									</script>
  </body>
