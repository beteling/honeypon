#! /usr/bin/python3.5

# Script de variables globales

HTMLHEADER = """
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
    <link href="/honeypon/css/bootstrap.min.css" rel="stylesheet">
    <link href="/honeypon/css/style.css" rel="stylesheet">


    <script src="/honeypon/js/jquery.min.js"></script>
    <script src="/honeypon/js/bootstrap.min.js"></script>

    <!-- Scripts Datatables -->
    <script type="text/javascript" src="datatables/datatables.js"></script>
	<script type="text/javascript" src="datatables/datatables.min.js"></script>
    <script type="text/javascript" src="datatables/dataTables.buttons.min.js"></script>
    <script type="text/javascript" src="datatables/jszip.min.js"></script>
    <script type="text/javascript" src="datatables/pdfmake.min.js"></script>
    <script type="text/javascript" src="datatables/vfs_fonts.js"></script>
    <script type="text/javascript" src="datatables/buttons.html5.min.js"></script>
	<script type="text/javascript" src="datatables/buttons.print.min.js"></script>

  </head><body>"""


pestañas_navegacion = """

    <div class="container-fluid">
	<div class="col-md-12">
	<h1>
	<img alt="honeypon logo" src="/honeypon/images/honeyponbete.png" style="margin-bottom:15px" />
	<a href="/honeypon/logout.py" style="text-decoration: none;font-size: 15px;float:right">Cerrar sesión&nbsp;<span class="glyphicon glyphicon-log-out"></span></a>
	<img alt="Logo empresa" src="/honeypon/images/logo_empresa.jpg" style="float:right;margin-top:15px;width: 300px;" />
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
						<a id='menuont' class="menuobject" href="menuont.py" style="color:#f5f5f5"><span <span class="fa fa-users"></span><b>&nbsp;&nbsp;SERVICIOS</b></a>
                    </li>
					<li>
						<a id='menucliente' class="menuobject" href="menucliente.py" style="color:#f5f5f5"><span class="fa fa-users"></span><b>&nbsp;&nbsp;CLIENTES ANTIGUO</b></a>
					</li>

					<li>
						<a id='menuolt' class="menuobject" href="menuolt.py"  style="color:#f5f5f5"><span class="glyphicon glyphicon-tasks"></span><b>&nbsp;&nbsp;OLT</b></a>
                    </li>

				</ul>
				</div>
				<div class="tab-content">


					"""

javadatatableont = """<script>


		$('#tablalistaont').dataTable( {
			dom: 'Bfrtip',
			buttons: [
				{
				extend: 'copyHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5]
				}
				},
				{
				extend: 'excelHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5 ]
				}
				},
				{
				extend: 'pdfHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5 ]
				}
				},
				{
				extend: 'print',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5 ]
				}
				},

			],
            columnDefs: [
               { orderable: false, targets: [6,7] }],
			"searching": false,
			scrollY: 600,
			paging: false,
			"language": {
			"infoEmpty": "Ninguna entrada que mostrar",
			"info": "Mostrando _TOTAL_ entradas",
			"emptyTable": "No hay registros disponibles"
			}

		} );

	</script>
"""

javadatatablecliente = """<script>


		$('#tablalistacliente').dataTable( {
			dom: 'Bfrtip',
			buttons: [
				{
				extend: 'copyHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5, 6, 7]
				}
				},
				{
				extend: 'excelHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ]
				}
				},
				{
				extend: 'pdfHtml5',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ]
				}
				},
				{
				extend: 'print',
				exportOptions: {
				columns: [ 0, 1, 2, 3, 4, 5, 6, 7 ]
				}
				},

			],
            columnDefs: [
               { orderable: false, targets: 8 }],
			"searching": false,
			scrollY: 600,
			paging: false,
			"language": {
			"infoEmpty": "Ninguna entrada que mostrar",
			"info": "Mostrando _TOTAL_ entradas",
			"emptyTable": "No hay registros disponibles"
			}

		} );


	</script>
"""

javadatatableplanes = """<script>


		$('.tablalistaplanes').dataTable( {

            "ordering":false,
			"searching": false,
			scrollY: 400,
			paging: false,
			"language": {
			"infoEmpty": "Ninguna entrada que mostrar",
			"info": "Mostrando _TOTAL_ entradas",
			"emptyTable": "No hay registros disponibles",
            "info": ""
			}

		} );


	</script>
"""


javadatatablebuttonstyle = """
    <script>
        $(".buttons-excel span").append('&nbsp;<i class="fa fa-1x fa-file-excel-o"></i>');
			$(".buttons-excel").css({
					   'background':'#37BC9B',
					   'color' : 'white'
					});
			$(".buttons-excel").hover(function(){
					$(this).css("background", "#48CFAD");
					},function(){
					$(this).css("background", "#37BC9B");
				});

			$(".buttons-pdf span").append('&nbsp;<i class="fa fa-1x fa-file-pdf-o"></i>');
			$(".buttons-pdf").css({
					   'background':'#DA4453',
					   'color' : 'white'
					});
			$(".buttons-pdf").hover(function(){
					$(this).css("background", "#ED5565");
					},function(){
					$(this).css("background", "#DA4453");
				});

			$(".buttons-print span").append('&nbsp;<i class="fa fa-1x fa-print"></i>');



	</script>
"""

javacookie = """<script>var timeoutID;

                function setup() {

                    this.addEventListener("keypress", resetTimer, false);
                    this.addEventListener("DOMMouseScroll", resetTimer, false);
                    this.addEventListener("mousewheel", resetTimer, false);
                    this.addEventListener("touchmove", resetTimer, false);
                    this.addEventListener("MSPointerMove", resetTimer, false);

                    startTimer();
                }
                setup();

                function startTimer() {
                    // wait 2 seconds before calling goInactive
                    timeoutID = window.setTimeout(goInactive, 2000);
                }

                function resetTimer(e) {
                    window.clearTimeout(timeoutID);

                    goActive();
                }

                function goInactive() {alert("Hello! I am an alert box!");"""

javacookie2 =  """}

                function goActive() {
                    // do something

                    startTimer();
                }</script>"""
javacode = """
    <script type="text/javascript" src="/honeypon/js/scripts.js"></script>

	"""


javatablocalstorage = """<script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
        localStorage.setItem('activeTab', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab');
    if(activeTab){
        $('#myTab a[href="' + activeTab + '"]').tab('show');
    }
});
</script> """

tabladba="""
    <div class="col-md-12" style="margin-top:5px">

	<table class="table tablalistaplanes" id="tablalistadba">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Nombre</th>
                <th style="text-align:center; color:#1A5F82">Subida</th>
				<th style="text-align:center; color:#1A5F82">OLT</th>
				<th style="text-align:center; color:#1A5F82"></th>
			</tr>
		</thead>
	<tbody>

"""
tabladbafin = """</tbody></table></div>"""

tablaplanes="""
    <div class="col-md-12" style="margin-top:5px">

	<table class="table tablalistaplanes" id="tablalistaplanes">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Nombre</th>
                <th style="text-align:center; color:#1A5F82">Descarga CIR</th>
				<th style="text-align:center; color:#1A5F82">Descarga PIR</th>
                <th style="text-align:center; color:#1A5F82">Subida DBA</th>
				<th style="text-align:center; color:#1A5F82">OLT</th>
				<th style="text-align:center; color:#1A5F82"></th>
			</tr>
		</thead>
	<tbody>

"""
tablaplanesfin = """</tbody></table></div>"""

tablatrafico="""
    <div class="col-md-12" style="margin-top:5px">

	<table class="table tablalistaplanes" id="tablalistatrafico">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Nombre</th>
                <th style="text-align:center; color:#1A5F82">CIR</th>
				<th style="text-align:center; color:#1A5F82">PIR</th>
				<th style="text-align:center; color:#1A5F82">OLT</th>
				<th style="text-align:center; color:#1A5F82"></th>
			</tr>
		</thead>
	<tbody>

"""

tablatraficofin = """</tbody></table></div>"""

tablaont = """

	<div class="col-md-12" style="margin-top:5px">

	<table class="table" id="tablalistaont">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Número de serie</th>
				<th style="text-align:center; color:#1A5F82">F/S/P ONT-ID</th>
                <th style="text-align:center; color:#1A5F82">Modelo</th>
				<th style="text-align:center; color:#1A5F82">ID Servicio</th>
				<th style="text-align:center; color:#1A5F82">Estado</th>
				<th style="text-align:center; color:#1A5F82">Línea</th>
                <th style="text-align:center; color:#1A5F82" class="hidden">Cliente</th>
				<th style="text-align:center; color:#1A5F82"><button type="button" title="Refrescar" class="btn btn-info btn-sm" style="float:right;font-size:15px; margin-left:10px" value="Refresh Page" onClick="window.location.reload()"><i class="glyphicon glyphicon-refresh"></i></button><div class="input-group" style="width:210px; float:right"><input type="text"  class="search form-control" placeholder="Escriba para buscar"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div></th>
			</tr>
		</thead>
	<tbody>
	"""
tablaolt = """

	<div class="col-md-12" style="margin-top:5px">
	<table class="table" id="table">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Nombre</th>
				<th style="text-align:center; color:#1A5F82">Direccion IP</th>
				<th style="text-align:center; color:#1A5F82">Cacti ID</th>
				<th style="text-align:center; color:#1A5F82"><div class="input-group" style="width:210px; float:right"><input type="text"  class="search form-control" placeholder="Escriba para buscar"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div></th>
			</tr>
		</thead>

	"""

tablacliente= """

	<div class="col-md-12" style="margin-top:5px">
	<table class="table" id="tablalistacliente">
		<thead>
			<tr>
				<th style="text-align:center; color:#1A5F82">Nombre</th>
				<th style="text-align:center; color:#1A5F82">Dirección</th>
				<th style="cursor:pointer;text-align:center; color:#1A5F82">ID</th>
				<th style="text-align:center; color:#1A5F82">Plan de datos</th>
				<th style="text-align:center; color:#1A5F82">DNI</th>
				<th style="text-align:center; color:#1A5F82">Tlfo. Contacto</th>
                <th style="text-align:center; color:#1A5F82">IP</th>
                <th style="text-align:center; color:#1A5F82">Tipo </th>
				<th style="text-align:center; color:#1A5F82"><div class="input-group" style="width:210px; float:right"><input type="text"  class="search form-control" placeholder="Escriba para buscar"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div></th>
			</tr>
		</thead>

	"""


modalclienteborrado = """
				<!-- Modal -->
				<div id='modal-borrarcliente%s' class='modal fade' role='dialog'>
				  <div class='modal-dialog' style='width:400px'>
					<!-- Modal content-->
					<div class='modal-content'>
					  <div class='modal-header' style='text-align:center; background-color:#FEA126'>
						<button type='button' class='close' data-dismiss='modal'>&times;</button>
						<h4 class='modal-title' style='font-size:20px; color:white;'>Ventana de confirmación</h4>
					  </div>
					  <div class='modal-body'>
						<p style='font-size:14px'>¿Está seguro de que desea borrar el cliente <b>%s</b>?</p>
					  </div>
					  <div class='modal-footer'>
						<button onclick='bajacliente("%s")' data-dismiss='modal' data-backdrop='false' name='bajacliente' value='botonbaja' class='btn btn-danger'>Aceptar</button>
					  </div>

					</div>

				  </div>
				</div>
				"""
modalontborrado = """
				<!-- Modal -->
				<div id="modal-borraront%s" class="modal fade" role="dialog">
				  <div class="modal-dialog" style="width:400px">
					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#FEA126">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title" style="font-size:20px; color:white;">Ventana de confirmación</h4>
					  </div>
					  <div class="modal-body">
						<p style='font-size:14px'>¿Está seguro de que desea dar de baja la ONT?</p>
					  </div>
					  <div class="modal-footer">
						<button type='submit' name='bajaont' value="Baja ONT"  class='btn btn-danger'>Aceptar</button>
					  </div>

					</div>

				  </div>
				</div>
				"""
modaloltborrado = """
				<!-- Modal -->
				<div id="modal-borrarolt%s" class="modal fade" role="dialog">
				  <div class="modal-dialog" style="width:400px">
					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#FEA126">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title" style="font-size:20px; color:white;">Ventana de confirmación</h4>
					  </div>
					  <div class="modal-body">
						<p style='font-size:14px'>¿Está seguro de que desea dar de baja la OLT?</p>
					  </div>
					  <div class="modal-footer">
						<button type='submit' name='bajaolt' value="Baja OLT"  class='btn btn-danger'>Aceptar</button>
					  </div>

					</div>

				  </div>
				</div>
				"""

tablaoltfin = """</tbody></table></div>"""

tablaontfin = """</tbody></table></div>"""

tablaclientefin = """</tbody></table></div>"""

modalont = """
				<!-- Modal -->
				<div id="mymodal" class="modal fade" role="dialog">
				  <div class="modal-dialog" style="width:400px">

					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#FEA126">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title" style="font-size:20px; color:white;">Alta ONT</h4>
					  </div>
					  <div class="modal-body">
						<form name="altaform" class="form-horizontal" autocomplete="off" role="form" action="/cgi-bin/ont.py" method="post" id="ontform" >
				<div class="form-group">

					<label for="inputsn" class="col-sm-4 control-label" style="color:#286090">
						SN
					</label>
					<div class="col-sm-10" style="width:200px">
						<input type="text" class="form-control" id="inputsn" name="sn" required minlength=16 maxlength=16 />
					</div>
				</div>
				<div class="form-group">

					<label for="inputservice" class="col-sm-4 control-label" style="color:#286090">
						ID Servicio
					</label>
					<div class="col-sm-10" style="width:200px">
						<input type="text" pattern="[0-9]{4,10}" class="form-control" id="inputservice" name="service" required minlength=4 maxlength=10 />
					</div>
				</div>
					  </div>
					  <div class="modal-footer">
						<input type="submit" class="btn btn-primary btn-block" value="APROVISIONAR" name="altaserv" />
					  </div>
					  </form>
					</div>

				  </div>
				</div>
				"""
modalolt = """
				<!-- Modal -->
				<div id="myModalolt" class="modal fade" role="dialog">
				  <div class="modal-dialog" style="width:400px">

					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#FEA126">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title" style="font-size:20px; color:white;">Alta OLT</h4>
					  </div>
					  <div class="modal-body">
						<form name="altaoltform" class="form-horizontal" autocomplete="off" role="form" action="/cgi-bin/olt.py" method="post" id="oltform">
				<div class="form-group">

					<label for="inputnameolt" class="col-sm-4 control-label" style="color:#286090">
						Nombre
					</label>
					<div class="col-sm-10" style="width:200px">
						<input type="text" class="form-control" id="inputnameolt" name="altaoltname" required maxlength=30 />
					</div>
				</div>
				<div class="form-group">

					<label for="inputip" class="col-sm-4 control-label" style="color:#286090">
						Direccion IP
					</label>
					<div class="col-sm-10" style="width:200px">
						<input type="text" class="form-control" id="inputip" name="inputip" required minlength=7 maxlength=15 />
					</div>
				</div>
					  </div>
					  <div class="modal-footer">
						<input type="submit" class="btn btn-primary btn-block" value="REGISTRAR" name="altaolt" />
					  </div>
					  </form>
					</div>

				  </div>
				</div>
				"""


modalcliente="""
<!-- Modal -->
<div id="modal_alta_cliente" class="modal fade" role="dialog">
  <div class="modal-dialog" style="width:800px">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header" style="text-align:center; background-color:#FEA126">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title" style="font-size:20px; color:white;">Alta de cliente</h4>
      </div>
      <div class="modal-body">
        <form name="altacliente" class="form-horizontal" autocomplete="off" role="form" action="/cgi-bin/altacliente.py" method="post" id="form1">
    <h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información personal -</h4>
<div class="form-group">

    <label for="inputnamecliente" class="col-sm-2 control-label" style="color:#286090">
        Nombre
    </label>
    <div class="col-sm-10" style="width:300px">
        <input type="text" class="form-control" id="inputnamecliente" name="nombrecliente" required maxlength=50 />
    </div>
</div>
<div class="form-group">

    <label for="inputdireccion" class="col-sm-2 control-label" style="color:#286090">
        Dirección
    </label>
    <div class="col-sm-10" style="width:500px">
        <input type="text" class="form-control" id="inputdireccion" name="direccioncliente" required maxlength=100 />
    </div>
</div>
<div class="form-group">

    <label for="inputtelf" class="col-sm-2 control-label" style="color:#286090">
        Teléfono
    </label>
    <div class="col-sm-10" style="width:200px">
        <input type="text" pattern="[0-9]{9,15}" class="form-control" id="inputtelf" name="telfcliente" minlength=9 maxlength=15 />
    </div><i>(Opcional)</i>
</div>
<div class="form-group">

    <label for="inputdni" class="col-sm-2 control-label" style="color:#286090">
        DNI
    </label>
    <div class="col-sm-10" style="width:200px">
        <input type="text" class="form-control" id="inputdni" name="dnicliente" required minlength=9 maxlength=9 />
    </div>
</div>
<hr>
<h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información del servicio -</h4>
<div class="form-group">
    <label class="col-sm-2 control-label" style="color:#286090">
       PPPOE
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputarrendpppoe" name="inputarrendpppoe" value="pppoe" onclick="campopppoe()"/>
    </div>

    <label class="col-sm-2 control-label" style="color:#286090">
       CG-NAT
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputcgnat" name="inputcgnat" value="cgnat"/>
    </div>
    <label class="col-sm-2 control-label" style="color:#286090">
       BRIDGE
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="chkbridge" name="chkbridge" value="bridge"/>
    </div>
	<label class="col-sm-2 control-label" style="color:#286090">
       SIP
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputsip" name="inputsip" value="sip" onclick="camposip()"/>
    </div>
</div>
<div id='userpppoe' class="form-group pppoefield hidden">
			<label for="inputuserpppoe" class="col-sm-2 control-label" style="color:#286090">
				Usuario PPPOE
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="text"  class="form-control" id="inputuserpppoe" name="inputuserpppoe" minlength=3 maxlength=15/>
			</div>
		</div>
		<div id='passwordpppoe' class="form-group pppoefield hidden">
			<label for="inputpasspppoe" class="col-sm-2 control-label" style="color:#286090">
				Contraseña PPPOE
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="password"  class="form-control" id="inputpasspppoe" name="inputpasspppoe" minlength=4 maxlength=25/>
			</div>
</div>

<div class="form-group">

    <label for="selectplan" class="col-sm-2 control-label" style="color:#286090">
        Plan de datos
    </label>
    <div class="col-sm-10" style="width:250px">

        <select onchange="loadoltlist($('#selectplan option:selected').val())" id='selectplan' name="selectplan" class="form-control" required>
        <option value='' selected disabled>Seleccionar</option>
"""
modalcliente2="""
	</select>
	</div>
	</div>

	<div class="form-group" id='formgroupolt'>
	<label for="selectolt" class="col-sm-2 control-label" style="color:#286090">
		OLT
	</label>
	<div class="col-sm-10" style="width:250px">

		<select id='selectolt' name="selectolt" class="form-control" required>
        <option value='' selected disabled>Seleccionar</option>
"""
modalcliente3="""
		</select>
	</div>
	</div>
	<div id='extensionsip' class="form-group sip hidden">
			<label for="inputextensionsip" class="col-sm-2 control-label" style="color:#286090">
				Extensión SIP
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="text"  class="form-control" id="inputextensionsip" name="inputextensionsip" minlength=9 maxlength=15 disabled/>
			</div>
		</div>
		<div id='secretsip' class="form-group sip hidden">
			<label for="inputsecretsip" class="col-sm-2 control-label" style="color:#286090">
				Secret SIP
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="password"  class="form-control" id="inputsecretsip" name="inputsecretsip" minlength=4 maxlength=25 disabled />
			</div>
		</div>
        <div id='serversip' class="form-group sip hidden">
			<label for="inputserversip" class="col-sm-2 control-label" style="color:#286090">
				Servidor SIP
			</label>
			<div class="col-sm-10" style="width:200px">
                <select id='inputserversip' name="inputserversip" class="form-control" required>"""

modalcliente4="""
				</select>
            </div>
		</div>
</div>
				<div class="modal-footer">
                  <input type="submit" class="btn btn-primary btn-block" value="REGISTRAR" name="clientealta" />
                </div>
			</form>



          </div>
        </div>
        </div>
"""
modalclienteajax="""
<!-- Modal -->
<div id="myModalcliente" class="modal fade" role="dialog">
  <div class="modal-dialog" style="width:800px">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header" style="text-align:center; background-color:#FEA126">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title" style="font-size:20px; color:white;">Alta de cliente</h4>
      </div>
      <div class="modal-body">
        <form name="altacliente" class="form-horizontal" autocomplete="off" role="form" action="/cgi-bin/altacliente.py" method="post" id="form1">
    <h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información personal -</h4>
<div class="form-group">

    <label for="inputnamecliente" class="col-sm-2 control-label" style="color:#286090">
        Nombre
    </label>
    <div class="col-sm-10" style="width:300px">
        <input type="text" class="form-control" id="inputname" name="nombreclientecliente" required maxlength=50 />
    </div>
</div>
<div class="form-group">

    <label for="inputdireccion" class="col-sm-2 control-label" style="color:#286090">
        Dirección
    </label>
    <div class="col-sm-10" style="width:500px">
        <input type="text" class="form-control" id="inputdireccion" name="direccioncliente" required maxlength=100 />
    </div>
</div>
<div class="form-group">

    <label for="inputtelf" class="col-sm-2 control-label" style="color:#286090">
        Teléfono
    </label>
    <div class="col-sm-10" style="width:200px">
        <input type="text" pattern="[0-9]{9,15}" class="form-control" id="inputtelf" name="telfcliente" minlength=9 maxlength=15 />
    </div><i>(Opcional)</i>
</div>
<div class="form-group">

    <label for="inputdni" class="col-sm-2 control-label" style="color:#286090">
        DNI
    </label>
    <div class="col-sm-10" style="width:200px">
        <input type="text" class="form-control" id="inputdni" name="dnicliente" required minlength=9 maxlength=9 />
    </div>
</div>
<hr>
<h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información del servicio -</h4>
<div class="form-group">
    <label class="col-sm-2 control-label" style="color:#286090">
       PPPOE
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputarrendpppoe" name="inputarrendpppoe" value="pppoe"/>
    </div>

    <label class="col-sm-2 control-label" style="color:#286090">
       CG-NAT
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputcgnat" name="inputcgnat" value="cgnat"/>
    </div>
    <label class="col-sm-2 control-label" style="color:#286090">
       BRIDGE
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" onchange="functionbridge()" class="form-control" style='width:20px;height:20px' id="chkbridge" name="chkbridge" value="bridge"/>
    </div>
	<label class="col-sm-2 control-label" style="color:#286090">
       SIP
    </label>
    <div class="col-sm-10" style="width:25px">
       <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputsip" name="inputsip" value="sip" onclick="camposip()"/>
    </div>
</div>
<div class="form-group">

    <label for="selectplan" class="col-sm-2 control-label" style="color:#286090">
        Plan de datos
    </label>
    <div class="col-sm-10" style="width:250px">

        <select onchange="loadoltlist($('#selectplan option:selected').val())" id='selectplan' name="selectplan" class="form-control" required>
        <option value='' selected disabled>Seleccionar</option>
"""

modalcliente2ajax="""
	</select>
	</div>
	</div>

	<div class="form-group" id='formgroupolt'>
    <label for="selectolt" class="col-sm-2 control-label" style="color:#286090">
      OLT
    </label>
    <div class="col-sm-10" style="width:250px">

      <select id='selectolt' name="selectolt" class="form-control" required>
          <option value='' selected disabled>Seleccionar</option>
"""

modalcliente3ajax="""
      </select>
      </div>
	</div>
	<div id='extensionsip' class="form-group sip hidden">
			<label for="inputextensionsip" class="col-sm-2 control-label" style="color:#286090">
				Extensión SIP
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="text"  class="form-control" id="inputextensionsip" name="inputextensionsip" minlength=9 maxlength=15 disabled/>
			</div>
		</div>
		<div id='secretsip' class="form-group sip hidden">
			<label for="inputsecretsip" class="col-sm-2 control-label" style="color:#286090">
				Secret SIP
			</label>
			<div class="col-sm-10" style="width:200px">
				<input type="password"  class="form-control" id="inputsecretsip" name="inputsecretsip" minlength=4 maxlength=25 disabled />
			</div>
		</div>
        <div id='serversip' class="form-group sip hidden">
			<label for="inputserversip" class="col-sm-2 control-label" style="color:#286090">
				Servidor SIP
			</label>
			<div class="col-sm-10" style="width:200px">
                <select id='inputserversip' name="inputserversip" class="form-control" required>
                    <option value='vozfusion'>Vozfusion</option>
                    <option value='lcrcom'>Lcrcom</option>
                </select>
            </div>
		</div>
</div>

				<div class="modal-footer">
                  <button onclick='altadeclienteajax()' data-dismiss='modal' data-backdrop='false' class='btn btn-primary btn-block' value='REGISTRAR'>REGISTRAR</button>

                </div>
			</form>



          </div>
        </div>
        </div>
"""

slot0 = ['4194304000', '4194304256', '4194304512', '4194304768',
         '4194305024', '4194305280', '4194305536', '4194305792',
         '4194306048', '4194306304', '4194306560', '4194306816',
         '4194307072', '4194307328', '4194307584', '4194307840']

slot1 = ['4194312192', '4194312448', '4194312704', '4194312960',
         '4194313216', '4194313472', '4194313728', '4194313984',
         '4194314240', '4194314496', '4194314752', '4194315008',
         '4194315264', '4194315520', '4194315776', '4194316032']

slot2 = ['4194320384', '4194320640', '4194320896', '4194321152',
         '4194321408', '4194321664', '4194321920', '4194322176',
         '4194322432', '4194322688', '4194322944', '4194323200',
         '4194323456', '4194323712', '4194323968', '4194324224']


slot3 = ['4194328576', '4194328832', '4194329088', '4194329344',
         '4194329600', '4194329856', '4194330112', '4194330368',
         '4194330624', '4194330880', '4194331136', '4194331392',
         '4194331648', '4194331904', '4194332160', '4194332416']


slot4 = ['4194336768', '4194337024', '4194337280', '4194337536',
         '4194337792', '4194338048', '4194338304', '4194338560',
         '4194338816', '4194339072', '4194339328', '4194339584',
         '4194339840', '4194340096', '4194340352', '4194340608']


slot5 = ['4194344960', '4194345216', '4194345472', '4194345728',
         '4194345984', '4194346240', '4194346496', '4194346752',
         '4194347008', '4194347264', '4194347520', '4194347776',
         '4194348032', '4194348288', '4194348544', '4194348800']


HTMLFIN = """</body></html>"""
