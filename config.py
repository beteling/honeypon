#! /usr/bin/python3.5
import MySQLdb

# Variables Honeypon 2.0 Beta


con = MySQLdb.connect(host='localhost', user='honeypon', passwd='pon', db='honeyponv2')
cursor = con.cursor()

header_css_scripts="""
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
    <link rel="stylesheet" href="/honeypon/css/all.css">
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
      <link type="text/css" rel="stylesheet" href="/honeypon/chk/skins/all.css">


      <script src="/honeypon/js/jquery.min.js"></script>
      <script src="/honeypon/js/bootstrap.min.js"></script>
  	<script src="/honeypon/js/scripts.js"></script>

  	<!-- iCheck js -->
  	<script type="text/javascript" src="/honeypon/chk/icheck.js"></script>
  	<script type="text/javascript" src="/honeypon/chk/icheck.min.js"></script>

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

     </head><body>
"""

pestañas_navegacion = """

    <div class="container-fluid">
	<div class="col-md-12">
	<h1>
	<img alt="honeypon logo" src="/honeypon/images/honeyponbete.png" style="margin-bottom:15px" />
	<a href="/honeypon/logout.py" style="text-decoration: none;font-size: 15px;float:right">Cerrar sesión&nbsp;<span class="glyphicon glyphicon-log-out"></span></a>
	<img alt="Logo empresa" src="/honeypon/images/logo_empresa.png" style="float:right;margin-top:15px;width: 300px;" />
    </h1>
	</div>

	<div class="row">
		<div class="col-md-12">
				<div class="tabbable" >
				<div class="col-md-12">


				<ul class="nav nav-tabs nav-justified" style='background-color: transparent;' align="center">
                    <li>
						<a id='main' class="menuobject" href="main.py" style="color:#f5f5f5"><span class="glyphicon glyphicon-align-justify"></span><b>&nbsp;&nbsp;INICIO</b></a>
                    </li>

					<li>
						<a id='menuont' class="menuobject" href="menuont.py" style="color:#f5f5f5"><span <span class="fa fa-users"></span><b>&nbsp;&nbsp;SERVICIOS</b></a>
                    </li>


				</ul>
				</div>
				<div class="tab-content">


					"""

filtros_ont = """

  <div class='col-md-12' style='margin-bottom:40px;margin-top:20px'>
    <table class='table table-striped'>

    <thead>
      <tr style='color:#195F82'>
      <th>Tipo</th>
      <th class='columnainputtype hidden'>Valor</th>
      <th class='columnafiltro'>OLT</th>
      <th class='columnafiltro'>Tarjeta</th>
      <th class='columnafiltro'>Puerto</th>
      <th class='columnafiltro'>Clientes de baja</th>


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
            <?php
                $sqlselectolt = "SELECT ID, Nombre, IP FROM olt";
                $resultselectolt=mysqli_query($enlace,$sqlselectolt);
                while($fila=mysqli_fetch_row($resultselectolt))
                {
                  $id = $fila[0];
                  $nombre = $fila[1];
                  $ip = $fila[2];


                  printf("<option class='olt'value='%s'>%s</option>",$id,$nombre);
                }
            ?>

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
      <td class='columnafiltro'>
        <div style='max-width:150px'>
            <input id="chk_bajas" value="" type="checkbox" class="icheck" />
        </div>
    </div>
    <script>
        $(document).ready(function () {
            $('#chk_bajas').iCheck({
                checkboxClass: 'icheckbox_flat-blue',
                radioClass: 'iradio_flat-pink'
            });
        });
    </script>
      </td>

     </tr>
     </tbody>
     </table>
      <button style='float:right' type='button' name='' onclick='consultar_registros("consulta_servicio");' class='btn btn-info'>Consultar</button>
    </div>

  <span id='spantablaont' ></span>

"""

script_multiselect="""
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
"""

script_list_resources="""
    <script>
        listar_olt();
        listar_planes();
        listar_serversip();
    </script>
"""

modal_cliente_asociado = """
    <!-- Modal -->
      <div id="modal-cliente-asociado" class="modal fade" role="dialog">
          <div class="modal-dialog" style="width: 60%;">

                          <!-- Modal content-->
          <div class="modal-content">
              <div class="modal-header" style="text-align:center; background-color:#01bfb9">
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
                  <h4 class="modal-title" style="font-size:20px; color:white;">Datos de cliente: <span class="title_id_client"></span></h4>
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
"""


modalont = """
				<!-- Modal -->
				<div id="modal_alta_ont" class="modal" role="dialog" data-backdrop="static" data-keyboard="false">
				  <div class="modal-dialog" style="width:400px">

					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#01bfb9">
						<button type="button" class="close" data-dismiss="modal">&times;</button>
						<h4 class="modal-title" style="font-size:20px; color:white;">Alta de servicio</h4>
					  </div>
					  <div class="modal-body">
						<form name="altaform" class="form-horizontal" autocomplete="off" role="form" action="/cgi-bin/service.py" method="post" id="ontform" >
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
						<input disabled id="prov_button" onclick='altaservicioajax($("#inputservice").val(),$("#inputsn").val())' class="btn btn-primary btn-block" value="APROVISIONAR" name="altaserv" />
					  </div>
					  </form>
					</div>

				  </div>
				</div>
				"""

modal_alta_cliente="""
<!-- Modal -->
<div id="modal_alta_cliente" class="modal fade" role="dialog">
  <div class="modal-dialog" style="width:60%">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header" style="text-align:center; background-color:#01bfb9">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title" style="font-size:20px; color:white;">Alta de cliente</h4>
      </div>
      <div class="modal-body">
        <form name="altacliente" class="form-horizontal" autocomplete="off" role="form" action="honeyajax.php" method="post" id="form_nuevo_cliente">
                        <h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información personal -</h4>
                    <div class="form-group">

                        <label for="inputnamecliente" class="col-sm-2 control-label" style="color:#286090">
                            Nombre
                        </label>
                        <div class="col-sm-10" style="width:60%">
                            <input type="text" class="form-control" id="inputnamecliente" name="inputname" required maxlength=50 />
                        </div>
                    </div>
                    <div class="form-group">

                        <label for="inputdireccion" class="col-sm-2 control-label" style="color:#286090">
                            Dirección
                        </label>
                        <div class="col-sm-10" style="width:60%">
                            <input type="text" class="form-control" id="inputdireccion" name="inputdireccion" required maxlength=100 />
                        </div>
                    </div>
                    <div class="form-group">

                        <label for="inputtelf" class="col-sm-2 control-label" style="color:#286090">
                            Teléfono
                        </label>
                        <div class="col-sm-10" style="width:200px">
                            <input type="text" pattern="[0-9]{9,15}" class="form-control" id="inputtelf" name="inputtelf" minlength=9 maxlength=15 />
                        </div><i>(Opcional)</i>
                    </div>
                    <div class="form-group">

                        <label for="inputdni" class="col-sm-2 control-label" style="color:#286090">
                            DNI
                        </label>
                        <div class="col-sm-10" style="width:200px">
                            <input type="text" class="form-control" id="inputdni" name="inputdni" required minlength=9 maxlength=9 />
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
                    <span class="hidden">
                        <label class="col-sm-2 control-label" style="color:#286090">
                           CG-NAT
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" class="form-control" style='width:20px;height:20px' id="inputcgnat" name="inputcgnat" value="cgnat"/>
                        </div>
                    </span>
                    <span class="hidden">
                        <label class="col-sm-2 control-label" style="color:#286090">
                           BRIDGE
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" onchange="functionbridge()" class="form-control" style='width:20px;height:20px' id="inputbridge" name="inputbridge" value="bridge"/>
                        </div>
                    </span>
                    	<label class="col-sm-2 control-label" style="color:#286090">
                           VoIP
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
                    				<input type="text"  class="form-control" id="inputuserpppoe" name="inputuserpppoe" minlength=3 maxlength=25 autocomplete="new-password" disabled />
                    			</div>
                    		</div>
                    		<div id='passwordpppoe' class="form-group pppoefield hidden">
                    			<label for="inputpasspppoe" class="col-sm-2 control-label" style="color:#286090">
                    				Contraseña PPPOE
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="password"  class="form-control" id="inputpasspppoe" name="inputpasspppoe" minlength=4 maxlength=25 autocomplete="new-password" disabled />
                    			</div>
                    </div>
                    <div class="form-group">

                        <label for="selectplan" class="col-sm-2 control-label" style="color:#286090">
                            Plan de datos
                        </label>
                        <div class="col-sm-10" style="width:250px">

                            <select onchange="loadoltlist($('#cliente_selectplan option:selected').val())" id='cliente_selectplan' name="selectplan" class="form-control" required>
                            <option value='' selected disabled>Seleccionar</option>

                    	</select>
                    	</div>
                    	</div>

                    	<div class="form-group" id='formgroupolt'>
                        <label for="selectolt" class="col-sm-2 control-label" style="color:#286090">
                          OLT
                        </label>
                        <div class="col-sm-10" style="width:250px">

                          <select id='cliente_selectolt' name="selectolt" class="form-control" required>
                              <option value='' selected disabled>Seleccionar</option>

                          </select>
                          </div>
                    	</div>
                    	<div id='extensionsip' class="form-group sip hidden">
                    			<label for="inputextensionsip" class="col-sm-2 control-label" style="color:#286090">
                    				Extensión SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="text" class="form-control" id="inputextensionsip" name="inputextensionsip" placeholder="Teléfono sin espacios" minlength=4 maxlength=15 required autocomplete="new-password" disabled/>
                    			</div>
                    		</div>
                    		<div id='secretsip' class="form-group sip hidden">
                    			<label for="inputsecretsip" class="col-sm-2 control-label" style="color:#286090">
                    				Secret SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="password"  class="form-control" id="inputsecretsip" name="inputsecretsip" minlength=4 maxlength=25 required autocomplete="new-password" disabled />
                    			</div>
                    		</div>
                            <div id='serversip' class="form-group sip hidden">
                    			<label for="inputserversip" class="col-sm-2 control-label" style="color:#286090">
                    				Servidor SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                                    <select id='inputserversip' name="inputserversip" class="form-control" required disabled>

                                    </select>
                                </div>
                    		</div>
                    </div>

                    				<div class="modal-footer">
                                      <button type='submit'  data-backdrop='false' class='btn btn-primary btn-block' value='REGISTRAR'>REGISTRAR</button>
                                    </form>
                                    </div>




          </div>
        </div>
        </div>
"""
modal_baja_cliente = """<div id='modal-baja-cliente' data-idcliente = '' class='modal fade' role='dialog'>
  <div class='modal-dialog' style='width:600px'>
    <!-- Modal content-->
    <div class='modal-content'>
      <div class='modal-header' style='text-align:center; background-color:#01bfb9'>
        <button type='button' class='close' data-dismiss='modal'>&times;</button>
        <h4 class='modal-title' style='font-size:20px; color:white;'>Confirmarción</h4>
      </div>
      <div class='modal-body'>
        <p style='font-size:14px'>¿Desea dar de baja administrativa al cliente: <b id="idcliente_modal_baja"></b></p>
      </div>
      <div class='modal-footer'>
        <button  onclick='baja_clienteajax($("#modal-baja-cliente").attr("data-idcliente"))'  data-backdrop='false' class='btn btn-warning'>Dar de baja</button>
      </div>

    </div>

  </div>
</div>"""

modal_borrar_cliente = """<div id='modal-borrar-cliente' data-idcliente = '' class='modal fade' role='dialog'>
  <div class='modal-dialog' style='width:600px'>
    <!-- Modal content-->
    <div class='modal-content'>
      <div class='modal-header' style='text-align:center; background-color:#01bfb9'>
        <button type='button' class='close' data-dismiss='modal'>&times;</button>
        <h4 class='modal-title' style='font-size:20px; color:white;'>Confirmarción</h4>
      </div>
      <div class='modal-body'>
        <p style='font-size:14px'>¿Seguro de que desea eliminar definitivamente al cliente: <b id="idcliente_modal_borrar"></b>?</p>
      </div>
      <div class='modal-footer'>
        <button ondblclick='borrar_clienteajax($("#modal-borrar-cliente").attr("data-idcliente"))'  data-backdrop='false' class='btn btn-danger'>Borrar cliente</button>
      </div>

    </div>

  </div>
</div>"""

modal_reactivar_cliente = """<div id='modal-reactivar-cliente' data-idcliente = '' class='modal fade' role='dialog'>
  <div class='modal-dialog' style='width:600px'>
    <!-- Modal content-->
    <div class='modal-content'>
      <div class='modal-header' style='text-align:center; background-color:#01bfb9'>
        <button type='button' class='close' data-dismiss='modal'>&times;</button>
        <h4 class='modal-title' style='font-size:20px; color:white;'>Confirmarción</h4>
      </div>
      <div class='modal-body'>
        <p style='font-size:14px'>¿Desea reactivar el cliente: <b id="idcliente_modal_reactivar"></b></p>
      </div>
      <div class='modal-footer'>
        <button onclick='reactivar_clienteajax($("#modal-reactivar-cliente").attr("data-idcliente"))'  data-backdrop='false' class='btn btn-success'>Reactivar cliente</button>
      </div>

    </div>

  </div>
</div>"""

modal_editar_cliente="""
<!-- Modal -->
<div id="modal_editar_cliente" class="modal fade" role="dialog">
  <div class="modal-dialog" style="width:60%">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header" style="text-align:center; background-color:#01bfb9">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title" style="font-size:20px; color:white;">Modificar cliente: <span class="title_id_client"></span></h4>
      </div>
      <div class="modal-body">
        <form name="editar_cliente" class="form-horizontal" autocomplete="off" role="form" action="honeyajax.php" method="post" id="form_editar_cliente">
                        <h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información personal -</h4>
                    <div class="form-group">

                        <label for="editar_inputnamecliente" class="col-sm-2 control-label" style="color:#286090">
                            Nombre
                        </label>
                        <div class="col-sm-10" style="width:60%">
                            <input type="text" class="form-control" id="editar_inputnamecliente" name="editar_inputname" required maxlength=50 />
                        </div>
                    </div>
                    <div class="form-group">

                        <label for="editar_inputdireccion" class="col-sm-2 control-label" style="color:#286090">
                            Dirección
                        </label>
                        <div class="col-sm-10" style="width:60%">
                            <input type="text" class="form-control" id="editar_inputdireccion" name="editar_inputdireccion" required maxlength=100 />
                        </div>
                    </div>
                    <div class="form-group">

                        <label for="editar_inputtelf" class="col-sm-2 control-label" style="color:#286090">
                            Teléfono
                        </label>
                        <div class="col-sm-10" style="width:200px">
                            <input type="text" pattern="[0-9]{9,15}" class="form-control" id="editar_inputtelf" name="editar_inputtelf" minlength=9 maxlength=15 />
                        </div><i>(Opcional)</i>
                    </div>
                    <div class="form-group">

                        <label for="editar_inputdni" class="col-sm-2 control-label" style="color:#286090">
                            DNI
                        </label>
                        <div class="col-sm-10" style="width:200px">
                            <input type="text" class="form-control" id="editar_inputdni" name="editar_inputdni" required minlength=9 maxlength=9 />
                        </div>
                    </div>
                    <hr>
                    <h4 style="color:#286090;margin-bottom:20px;text-align:center">- Información del servicio -</h4>
                    <div class="form-group">
                        <label class="col-sm-2 control-label" style="color:#286090">
                           PPPOE
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" class="form-control" style='width:20px;height:20px' id="editar_inputarrendpppoe" name="editar_inputarrendpppoe" value="pppoe" onclick="edit_campopppoe()"/>
                        </div>
                    <span class="hidden">
                        <label class="col-sm-2 control-label" style="color:#286090">
                           CG-NAT
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" class="form-control service-active" style='width:20px;height:20px' id="editar_inputcgnat" name="editar_inputcgnat" value="cgnat"/>
                        </div>
                    </span>
                    <span class="hidden">
                        <label class="col-sm-2 control-label" style="color:#286090">
                           BRIDGE
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" onchange="functionbridge()" class="form-control service-active" style='width:20px;height:20px' id="editar_inputbridge" name="editar_inputbridge" value="bridge"/>
                        </div>
                    </span>
                    	<label class="col-sm-2 control-label" style="color:#286090">
                           VoIP
                        </label>
                        <div class="col-sm-10" style="width:25px">
                           <input type="checkbox" class="form-control service-active" style='width:20px;height:20px' id="editar_inputsip" name="editar_inputsip" value="sip" onclick="edit_camposip()"/>
                        </div>
                    </div>
                    <div id='userpppoe' class="form-group editar_pppoefield hidden">
                    			<label for="editar_inputuserpppoe" class="col-sm-2 control-label" style="color:#286090">
                    				Usuario PPPOE
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="text"  class="form-control" id="editar_inputuserpppoe" name="editar_inputuserpppoe" minlength=3 maxlength=25 autocomplete="new-password" disabled />
                    			</div>
                    		</div>
                    		<div id='passwordpppoe' class="form-group editar_pppoefield hidden">
                    			<label for="editar_inputpasspppoe" class="col-sm-2 control-label" style="color:#286090">
                    				Contraseña PPPOE
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="password"  class="form-control" id="editar_inputpasspppoe" name="editar_inputpasspppoe" minlength=4 maxlength=25 autocomplete="new-password" disabled />
                    			</div>
                    </div>
                    <div class="form-group checkboxes_services">

                        <label for="editar_selectplan" class="col-sm-2 control-label" style="color:#286090">
                            Plan de datos
                        </label>
                        <div class="col-sm-10" style="width:250px">

                            <select onchange="loadoltlist($('#editar_cliente_selectplan option:selected').val())" id='editar_cliente_selectplan' name="editar_selectplan" class="form-control service-active" required>
                            <option value='' selected disabled>Seleccionar</option>

                    	</select>
                    	</div>
                    	</div>

                    	<div class="form-group" id='formgroupolt'>
                        <label for="editar_selectolt" class="col-sm-2 control-label" style="color:#286090">
                          OLT
                        </label>
                        <div class="col-sm-10" style="width:250px">

                          <select id='editar_cliente_selectolt' name="editar_selectolt" class="form-control service-active" required>
                              <option value='' selected disabled>Seleccionar</option>

                          </select>
                          </div>
                    	</div>
                    	<div id='extensionsip' class="form-group editar_sip hidden">
                    			<label for="editar_inputextensionsip" class="col-sm-2 control-label" style="color:#286090">
                    				Extensión SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="text" class="form-control service-active" id="editar_inputextensionsip" name="editar_inputextensionsip" placeholder="Teléfono sin espacios" minlength=4 maxlength=15 required autocomplete="new-password" disabled/>
                    			</div>
                    		</div>
                    		<div id='secretsip' class="form-group editar_sip hidden">
                    			<label for="editar_inputsecretsip" class="col-sm-2 control-label" style="color:#286090">
                    				Secret SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                    				<input type="password"  class="form-control service-active" id="editar_inputsecretsip" name="editar_inputsecretsip" minlength=4 maxlength=25 required autocomplete="new-password" disabled />
                    			</div>
                    		</div>
                            <div id='serversip' class="form-group editar_sip hidden">
                    			<label for="editar_inputserversip" class="col-sm-2 control-label" style="color:#286090">
                    				Servidor SIP
                    			</label>
                    			<div class="col-sm-10" style="width:200px">
                                    <select id='editar_inputserversip' name="editar_inputserversip" class="form-control service-active" required disabled>

                                    </select>
                                </div>
                    		</div>
                    </div>

                    				<div class="modal-footer">
                                    <input type="hidden" class="form-control" id="id_cliente" name="id_cliente" minlength=4 maxlength=25 required />
                                      <button type='submit'  data-backdrop='false' class='btn btn-primary btn-block' value='ACTUALIZAR'>ACTUALIZAR</button>
                                    </form>
                                    </div>




          </div>
        </div>
        </div>
"""

modal_baja_servicio = """
				<!-- Modal -->
				<div id="modal-baja-servicio" data-idcliente = '' class="modal" role="dialog">
				  <div class="modal-dialog" style="width:400px">
					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#01bfb9">

						<h4 class="modal-title" style="font-size:20px; color:white;">Ventana de confirmación</h4>
					  </div>
					  <div id='modal-body-baja'class="modal-body">
						<p style='font-size:14px'>¿Está seguro de que desea desprovisionar el servicio <b id="idservicio_modal_baja"></b>?</p>
					  </div>
					  <div id='modal-footer-baja' class="modal-footer">
						<button onclick='bajaservicioajax($("#modal-baja-servicio").attr("data-idcliente"))' name='bajacliente' value='botonbaja' class='btn btn-danger'>Aceptar</button>
					  </div>

					</div>

				  </div>
				</div>
				"""
modal_resultado = """
				<!-- Modal -->
				<div id="modal-resultado" data-idcliente = '' data-backdrop="static" data-keyboard="false" class="modal fade" role="dialog">
				  <div class="modal-dialog" style="width:50%">
					<!-- Modal content-->
					<div class="modal-content">
					  <div class="modal-header" style="text-align:center; background-color:#01bfb9">

						<h4 class="modal-title" style="font-size:20px; color:white;"><span id="prov_client_title"></span></h4>
					  </div>
					  <div id='modal-body-result' class="modal-body">

					  </div>
					  <div id='modal-footer-result'  class="modal-footer">
					  </div>

					</div>

				  </div>
				</div>
				"""

javacode = """
    <script type="text/javascript" src="/honeypon/js/scripts.js"></script>

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

HTMLFIN = """</div></div></div></div></body></html>"""
