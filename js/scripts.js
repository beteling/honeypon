
$(document).ready(function () {

$("#form_nuevo_cliente").submit(function(e) {

		e.preventDefault(); // avoid to execute the actual submit of the form.
		e.stopImmediatePropagation(); // avoid to execute the actual submit of the form.

		var form = $(this);
		var url = form.attr('action');
		var formData = new FormData(document.getElementById("form_nuevo_cliente"));

		//alert(formData);
		//var vehiculo_id = $("#modal-dialog-reserva").attr("data-id_vehiculo");
		//formData.append('vehiculo_id', vehiculo_id);

		var inputarrendpppoe = $('#inputarrendpppoe').prop('checked')
		var inputcgnat = $('#inputcgnat').prop('checked')
		var inputsip = $('#inputsip').prop('checked')
		var inputbridge = $('#inputbridge').prop('checked')
		var plan_nombre = $('#cliente_selectplan option:selected').html(); // Esta variable no se pasa a AJAX

		formData.append('alta_cliente_ajax','alta_cliente_ajax');
		formData.set('inputarrendpppoe',inputarrendpppoe);
		formData.set('inputcgnat',inputcgnat);
		formData.set('inputbridge',inputbridge);
		formData.set('inputsip',inputsip);

		var inputname = $('#inputnamecliente').val()
		var inputdireccion = $('#inputdireccion').val()
		var inputtelf = $('#inputtelf').val()
		var inputdni = $('#inputdni').val()

		var selectplan = $('#cliente_selectplan').val()
		var selectolt = $('#cliente_selectolt').val()

		var inputextensionsip = $('#inputextensionsip').val()
		var inputsecretsip = $('#inputsecretsip').val()
		var inputserversip = $('#inputserversip').val()



		// AJAX PARA DAR DE ALTA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS


		$.ajax({
					 type: "POST",
					 url: url,
					 //data: form.serialize(), // serializes the form's elements.
					 data: formData,
					 dataType: 'json',
					 cache: false,
					 contentType: false,
					 processData: false,
					 success: function(data)
					 {
						//alert(data.result);

						if(inputarrendpppoe == true){
							var pppoe_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='PPPOE Activado' class='fas fa-address-card'></i>";
						}else{
							var pppoe_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='PPPOE Desactivado' class='fas fa-address-card'></i>";
						}


						if(inputsip == true){
							var sip_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='Servicio Configurado' class='fas fa-phone'></i>";
						}else{
							var sip_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='Sin Servicio' class='fas fa-phone-slash'></i>";
						}

						if(inputbridge == true){
							var bridge_class = "<span title='Modo Bridge'><i style='margin-left:-15px;color:#FEA126;float: right;padding: 10px;'  class='fas fa-hdd'></i><i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' class='fas fa-arrows-alt-v'></i></span>";
						}else{
							var bridge_class = "<i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' title='Modo NAT' class='fas fa-filter'></i>";
						}


						var trnew = `<tr id="`+data.jsonclienteidnext+`" class="warning">
						<td  class='tableontlist'></td>
						<td  class='tableontlist'></td>
						<td  class='tableontlist'></td>
						<td class='tableontlist'> `+data.jsonclienteidnext+` </td>
						<td class='tableontlist'>`+plan_nombre+`</td>
						<td class='tableontlist' style='color:#FEA126'>Esperando datos</td>
						<td>
							<button id='clientassoc-"`+data.jsonclienteidnext+`"' title='Informacion del cliente' type='button' class='btn btn-info btn-xs' data-target='#modal-cliente-asociado' onclick='clientassoc("`+data.jsonclienteidnext+`");' data-toggle='modal' style='margin-left:10px'>
								<i class='fas fa-info-circle'></i>
							</button>
							<button title='Editar cliente' class="btn btn-secondary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="fas fa-edit"></i></button>
							<button id='registeront-"`+data.jsonclienteidnext+`"' title='Alta de servicio' type='button' onclick='asociar_ont("`+data.jsonclienteidnext+`")' data-toggle='modal' class='btn btn-success btn-xs' text-align=center' style='margin-left:10px'>
								<i class='fas fa-upload' style='margin-right:0.8px'></i>
							</button>
							<button title="Borrar cliente" type="button" onclick= 'modal_baja_cliente("`+data.jsonclienteidnext+`")' class="btn btn-danger btn-xs" style="margin-left:10px"><i class="fas fa-user-minus" style="margin-right:0.8px"></i></button>
								`+sip_class+`
								`+bridge_class+`
								`+pppoe_class+`
						</td>
						<td class='tableontlist colnif hidden'>"`+data.jsoninputdni+`"</td>
						</tr>`;


						$("#inputextensionsip").val("");
						$("#inputsecretsip").val("");


						$("#modal_alta_cliente").modal("toggle");
						altacliente.reset(); // Restaura los campos
						camposip();
						campopppoe();
						//$('#cuerpotabla').prepend(trnew);
						consultar_registros("consulta_servicio");




					 }
					 });


					 });


$("#form_editar_cliente").submit(function(e) { 


	e.preventDefault(); // avoid to execute the actual submit of the form.
	e.stopImmediatePropagation(); // avoid to execute the actual submit of the form.

	var form = $(this);
	var url = form.attr('action');
	var formData = new FormData(document.getElementById("form_editar_cliente"));

	//alert(formData);
	//var vehiculo_id = $("#modal-dialog-reserva").attr("data-id_vehiculo");
	//formData.append('vehiculo_id', vehiculo_id);

	var inputarrendpppoe = $('#editar_inputarrendpppoe').prop('checked')
	var inputcgnat = $('#editar_inputcgnat').prop('checked')
	var inputsip = $('#editar_inputsip').prop('checked')
	var inputbridge = $('#editar_inputbridge').prop('checked')


	formData.append('editar_cliente_ajax','editar_cliente_ajax'); // Variable POST Action
	formData.set('editar_inputarrendpppoe',inputarrendpppoe);
	formData.set('editar_inputcgnat',inputcgnat);
	formData.set('editar_inputbridge',inputbridge);
	formData.set('editar_inputsip',inputsip);

	var inputname = $('#editar_inputnamecliente').val()
	var inputdireccion = $('#editar_inputdireccion').val()
	var inputtelf = $('#editar_inputtelf').val()
	var inputdni = $('#editar_inputdni').val()

	var selectplan = $('#editar_cliente_selectplan').val()
	var selectolt = $('#editar_cliente_selectolt').val()

	var inputextensionsip = $('#editar_inputextensionsip').val()
	var inputsecretsip = $('#editar_inputsecretsip').val()
	var inputserversip = $('#editar_inputserversip').val()



	// AJAX PARA EDITAR AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS


	$.ajax({
				 type: "POST",
				 url: url,
				 //data: form.serialize(), // serializes the form's elements.
				 data: formData,
				 dataType: 'json',
				 cache: false,
				 contentType: false,
				 processData: false,
				 success: function(data)
				 {

					$("#modal_editar_cliente").modal("toggle");
					consultar_registros("consulta_servicio");


				 }
				 });


				 });

});

// Función que activa el bottón de APROVISIONAR sólo cuando se rellena el campo de SN
$('#inputsn').on('input', function() {
	if ($("#inputsn").val() == ""){
		$("#prov_button").attr("disabled", true)
	}else{
		$("#prov_button").attr("disabled", false)
	}
});



// Función para mostrar u ocultar campos SIP

function camposip(){

	if ($('#inputsip').prop('checked') == true){
		$('#inputbridge').prop('disabled', true);

		$(".sip").removeClass('hidden');
		$("#inputextensionsip").prop('disabled', false);
		$("#inputsecretsip").prop('disabled', false);
        $("#inputserversip").prop('disabled', false);

	}else if ($('#inputsip').prop('checked') == false){
		$('#inputbridge').prop('disabled', false);

		$(".sip").addClass('hidden');
		$("#inputextensionsip").prop('disabled', true);
		$("#inputsecretsip").prop('disabled', true);
        $("#inputserversip").prop('disabled', true);

	}
// VERSION ANTIGUA //
/*	if($(".sip").hasClass("hidden")){

		$(".sip").removeClass('hidden');
		$("#inputextensionsip").prop('disabled', false);
		$("#inputsecretsip").prop('disabled', false);
        $("#inputserversip").prop('disabled', false);
	}else{
		$(".sip").addClass('hidden');
		$("#inputextensionsip").prop('disabled', true);
		$("#inputsecretsip").prop('disabled', true);
        $("#inputserversip").prop('disabled', true);
	}*/

	// VERSION ANTIGUA //

	/*if ($('#inputsip').prop('checked') == true){
		$('#chkbridge').prop('disabled', true);
	}else if ($('#inputsip').prop('checked') == false){
		$('#chkbridge').prop('disabled', false);
	}*/

	}


	function edit_camposip(){

		if ($('#editar_inputsip').prop('checked') == true){
			$('#editar_inputbridge').prop('disabled', true);

			$(".editar_sip").removeClass('hidden');
			$("#editar_inputextensionsip").prop('disabled', false);
			$("#editar_inputsecretsip").prop('disabled', false);
	        $("#editar_inputserversip").prop('disabled', false);

		}else if ($('#editar_inputsip').prop('checked') == false){
			$('#editar_inputbridge').prop('disabled', false);

			$(".editar_sip").addClass('hidden');
			$("#editar_inputextensionsip").prop('disabled', true);
			$("#editar_inputsecretsip").prop('disabled', true);
	        $("#editar_inputserversip").prop('disabled', true);

		}

	}

function campopppoe(){

	if($('#inputarrendpppoe').prop('checked') == true){
	//if($(".pppoefield").hasClass("hidden")){

		$(".pppoefield").removeClass('hidden');

		//var pppoeuser = $("#inputnamecliente").val().toLowerCase().replace(/\ /g, '_');
		//pppoeuser = pppoeuser.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
		//var pppoepass = $("#inputdni").val().toUpperCase();

		var pppoeuser = "Fibra_" + $("#inputdni").val().toUpperCase()
		var pppoepass = $("#inputdni").val().slice(0,-1)

		$("#inputuserpppoe").val(pppoeuser);
		$("#inputpasspppoe").val(pppoepass);

		$("#inputuserpppoe").prop('disabled', false);
		$("#inputpasspppoe").prop('disabled', false);


	}else{
		$(".pppoefield").addClass('hidden');
		$("#inputuserpppoe").val("")
		$("#inputpasspppoe").val("")
		$("#inputuserpppoe").prop('disabled', true);
		$("#inputpasspppoe").prop('disabled', true);
	}



	}

	function edit_campopppoe(){

		if($('#editar_inputarrendpppoe').prop('checked') == true){
		//if($(".pppoefield").hasClass("hidden")){

			$(".editar_pppoefield").removeClass('hidden');

			//var pppoeuser = $("#inputnamecliente").val().toLowerCase().replace(/\ /g, '_');
			//pppoeuser = pppoeuser.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
			//var pppoepass = $("#inputdni").val().toUpperCase();

			var pppoeuser = "Fibra_" + $("#editar_inputdni").val().toUpperCase()
			var pppoepass = $("#editar_inputdni").val().slice(0,-1)

			$("#editar_inputuserpppoe").val(pppoeuser);
			$("#editar_inputpasspppoe").val(pppoepass);

			$("#editar_inputuserpppoe").prop('disabled', false);
			$("#editar_inputpasspppoe").prop('disabled', false);


		}else{
			$(".editar_pppoefield").addClass('hidden');
			$("#editar_inputuserpppoe").val("")
			$("#editar_inputpasspppoe").val("")
			$("#editar_inputuserpppoe").prop('disabled', true);
			$("#editar_inputpasspppoe").prop('disabled', true);
		}



		}

// Función para cargar lista de olt

function loadoltlist(plan){
	// AJAX PARA CARGAR LA LISTA DE OLT EN BASE A LOS PLANES
	var selectoltlist = true;
			$.ajax({
				type: 'POST',
				data: {selectoltlist:selectoltlist,plan:plan},
				dataType: 'json',
				url: '/honeypon/honeyajax.php',
				success: function(data) {
					$('#editar_cliente_selectolt').html('');
					$('#cliente_selectolt').html('');
					for(var i in data.jsonresultolt) {
					var resultadoolt = data.jsonresultolt[i];

						$('#cliente_selectolt').append(resultadoolt.optionolt);
						$('#editar_cliente_selectolt').append(resultadoolt.optionolt);

					};
				}


				});
	}

// Función para desactivar bridge si se marca sip

function functionbridge(){
	if ($('#inputbridge').prop('checked') == true){
		$('#inputsip').prop('disabled', true);

	}else if ($('#inputbridge').prop('checked') == false){
		$('#inputsip').prop('disabled', false);
	}
}
// Función AJAX para baja de cliente

function bajacliente(idcliente){
	// AJAX PARA DAR DE BAJA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS
			$.ajax({
				type: 'POST',
				data: {idclienteparabaja:idcliente},
				dataType: 'json',
				url: 'honeyajax.php',
				success:

				$("#"+idcliente).fadeOut(1000, function(){$(this).remove();}),


				});

	}
	function modal_baja_cliente(idcliente){
		$("#modal-baja-cliente").modal('toggle');
		$("#modal-baja-cliente").attr('data-idcliente', idcliente);
		$("#idcliente_modal_baja").html(idcliente);
	}



	function baja_clienteajax(idcliente){
		// AJAX PARA DAR DE BAJA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS

			$.ajax({
				type: 'POST',
				data: {idcliente_baja:idcliente},
				dataType: 'json',
				url: 'honeyajax.php',
				success:function() {

					$("#modal-baja-cliente").modal('toggle');
					consultar_registros("consulta_servicio");

				}


				});



		}
	// Boton actualmente desactivado
	function modal_borrar_cliente(idcliente){
			$("#modal-borrar-cliente").modal('toggle');
			$("#modal-borrar-cliente").attr('data-idcliente', idcliente);
			$("#idcliente_modal_borrar").html(idcliente);
		}
	function borrar_clienteajax(idcliente){
		// AJAX PARA BORRAR AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS

			$.ajax({
				type: 'POST',
				data: {idcliente_borrar:idcliente},
				dataType: 'json',
				url: 'honeyajax.php',
				success:function() {

					$("#modal-borrar-cliente").modal('toggle');
					$("#"+idcliente).fadeOut(1000, function(){$(this).remove();});

				}



				});



		}

		function modal_reactivar_cliente(idcliente){
			$("#modal-reactivar-cliente").modal('toggle');
			$("#modal-reactivar-cliente").attr('data-idcliente', idcliente);
			$("#idcliente_modal_reactivar").html(idcliente);
		}

		function reactivar_clienteajax(idcliente){
			// AJAX PARA DAR DE ALTA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS

				$.ajax({
					type: 'POST',
					data: {idcliente_reactivar:idcliente},
					dataType: 'json',
					url: 'honeyajax.php',
					success:function() {

						$("#modal-reactivar-cliente").modal('toggle')
						consultar_registros("consulta_servicio");

					}

					});
			}


		function modal_baja_servicio(idcliente){
			$("#modal-baja-servicio").modal('toggle');
			$("#modal-baja-servicio").attr('data-idcliente', idcliente);
			$("#idservicio_modal_baja").html(idcliente);
		}

		$( document ).ajaxStart(function() {
			  $("html").append("<span id='loadicon' style='z-index:100;position: absolute;top: 50%;left: 50%;'><img src='/honeypon/images/loadicon_2.gif' /><p style='text-align:center;font-size:16px;font-wieght:bold;margin-top:10px'>Cargando</p></span>");
			});
		$( document ).ajaxStop(function() {
			  $("#loadicon").remove();
			});

		function clean_modal_result(){
			$("#modal-resultado").modal('toggle')
			$("#modal-body-result").html("");
			$("#modal-footer-result").html("");
		}

		function bajaservicioajax(idcliente){
			// AJAX PARA DAR DE BAJA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS
						$("#prov_client_title").html("Desprovisionando servicio: <b>"+idcliente+"</b>")
						$("#modal-baja-servicio").modal('toggle')
						$("#modal-resultado").modal('toggle')

						//$("#tablalistaont").hide();
						$.ajax({
                    url: '/cgi-bin/event_baja_servicio.py',
                    type: "post",
                    datatype:"json",
                  	data: {idservicio_para_baja:idcliente},
                    success: function(response){
												//alert(response.success);
												//alert(response.message);

												$("#modal-body-result").html(response.message);
												$("#modal-footer-result").html("<button data-dismiss='modal' onclick='clean_modal_result()' class='btn btn-info'>Aceptar</button>");

												//$("#loadicon").remove();
												consultar_registros("consulta_servicio");
                        }
                    });

			}

			function altaservicioajax(idcliente, sn){
				// AJAX PARA APROVISIONAR LA ONT
					$("#prov_client_title").html("Aprovisionando servicio: <b>"+idcliente+"</b>")
					$("#modal_alta_ont").modal('toggle')
					$("#modal-resultado").modal('toggle')
							//$("#tablalistaont").hide();
							$.ajax({
	                    url: '/cgi-bin/event_alta_servicio.py',
	                    type: "post",
	                    datatype:"json",
	                  	data: {idservicio_para_alta:idcliente, sn_ont:sn},
	                    success: function(response){
													//alert(response.success);
													//alert(response.message);

													$("#modal-body-result").html(response.message);
													$("#modal-footer-result").html("<button data-dismiss='modal' onclick='clean_modal_result()' class='btn btn-info'>Aceptar</button>");

													if(window.location.pathname == "/honeypon/main.py"){
														consultar_registros("consulta_pendientes");
													}else{
														consultar_registros("consulta_servicio");
													}
													//$("#loadicon").remove();

	                        }
	                    });

				}

// Función AJAX para alta de cliente (EN DESUSO!)
/*
function altadeclienteajax(){


	var altaclienteajax = true;

	var inputname = $('#inputnamecliente').val()
	var inputdireccion = $('#inputdireccion').val()
	var inputtelf = $('#inputtelf').val()
	var inputdni = $('#inputdni').val()
	var inputarrendpppoe = $('#inputarrendpppoe').prop('checked')
	var inputcgnat = $('#inputcgnat').prop('checked')
	var inputsip = $('#inputsip').prop('checked')
	var inputbridge = $('#chkbridge').prop('checked')
	var selectplan = $('#cliente_selectplan').val()
	var selectolt = $('#cliente_selectolt').val()
	var inputextensionsip = $('#inputextensionsip').val()
	var inputsecretsip = $('#inputsecretsip').val()
	var inputserversip = $('#inputserversip').val()

	var plan_nombre = $('#cliente_selectplan option:selected').html();

	if(inputbridge ==true){
		inputbridge = 'si';
	}else{
		inputbridge = 'no';
	}

	if(inputcgnat ==true){
		inputcgnat = 'si';
	}else{
		inputcgnat = 'no';
	}

	if(inputarrendpppoe ==true){
		inputarrendpppoe = 'si';
	}else{
		inputarrendpppoe = 'no';
	}

	if(inputsip ==true){
		inputsip = 'si';
	}else{
		inputsip = 'no';
	}

	// AJAX PARA DAR DE ALTA AL CLIENTE DINAMICAMENTE EN LA BASE DE DATOS
			$.ajax({
				type: 'POST',
				data: {altaclienteajax:altaclienteajax,inputname:inputname,inputdireccion:inputdireccion,inputtelf:inputtelf,inputdni:inputdni,inputarrendpppoe:inputarrendpppoe,inputcgnat:inputcgnat,inputsip:inputsip,selectplan:selectplan,
					selectolt:selectolt,inputextensionsip:inputextensionsip,inputsecretsip:inputsecretsip,inputserversip:inputserversip,inputbridge:inputbridge},
				dataType: 'json',
				url: 'honeyajax.php',
				success: function(data) {


				if(inputarrendpppoe == 'si'){
					var pppoe_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='PPPOE Activado' class='fas fa-address-card'></i>";
				}else{
					var pppoe_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='PPPOE Desactivado' class='fas fa-address-card'></i>";
				}


				if(data.jsoninputsip == 'si'){
					var sip_class = "<i style='margin-left:10px;color:#31B0D5;float: right;padding: 10px;' title='Servicio Configurado' class='fas fa-phone'></i>";
				}else{
					var sip_class = "<i style='margin-left:10px;color:#c4bdbd;float: right;padding: 10px;' title='Sin Servicio' class='fas fa-phone-slash'></i>";
				}

				if(inputbridge == 'si'){
					var bridge_class = "<span title='Modo Bridge'><i style='margin-left:-15px;color:#FEA126;float: right;padding: 10px;'  class='fas fa-hdd'></i><i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' class='fas fa-arrows-alt-v'></i></span>";
				}else{
					var bridge_class = "<i style='margin-left:10px;color:#FEA126;float: right;padding: 10px;' title='Modo NAT' class='fas fa-filter'></i>";
				}


				var trnew = `<tr id="`+data.jsonclienteidnext+`" class="warning">
				<td  class='tableontlist'></td>
				<td  class='tableontlist'></td>
				<td  class='tableontlist'></td>
				<td class='tableontlist'> `+data.jsonclienteidnext+` </td>
				<td class='tableontlist'>`+plan_nombre+`</td>
				<td class='tableontlist' style='color:#FEA126'>Esperando datos</td>
				<td>
					<button id='clientassoc-"`+data.jsonclienteidnext+`"' title='Informacion del cliente' type='button' class='btn btn-info btn-xs' data-target='#modal-cliente-asociado' onclick='clientassoc("`+data.jsonclienteidnext+`");' data-toggle='modal' style='margin-left:10px'>
						<i class='fas fa-info-circle'></i>
					</button>
					<button title='Editar cliente' class="btn btn-secondary btn-xs" name="modificarcliente" value="botonedit" style="margin-left:10px"><i class="fas fa-edit"></i></button>
					<button id='registeront-"`+data.jsonclienteidnext+`"' title='Alta de servicio' type='button' onclick='asociar_ont("`+data.jsonclienteidnext+`")' data-toggle='modal' class='btn btn-success btn-xs' text-align=center' style='margin-left:10px'>
						<i class='fas fa-upload' style='margin-right:0.8px'></i>
					</button>
					<button title="Borrar cliente" type="button" onclick= 'modal_baja_cliente("`+data.jsonclienteidnext+`")' class="btn btn-danger btn-xs" style="margin-left:10px"><i class="fas fa-user-minus" style="margin-right:0.8px"></i></button>
						`+sip_class+`
						`+bridge_class+`
						`+pppoe_class+`
				</td>
				<td class='tableontlist colnif hidden'>"`+data.jsoninputdni+`"</td>
				</tr>`;

				$('#cuerpotabla').prepend(trnew);


				}


				});

	}
*/

// Función de consulta avanzada de ONT
function asociar_ont(id_servicio) {
	$("#inputsn").val("");
	$("#prov_button").attr("disabled", true)
	$("#modal_alta_ont").modal("toggle");
	$("#inputservice").val(id_servicio);
}


function consultar_registros(consulta) {

	var tipo_consulta = consulta;
	var type = $("#seltype").val();
	var inputtype = $("#inputtype").val();
	var olt = $("#selectolt").val();
	var slot = $("#selectslot").val();
	var port = $("#selectport").val();
	var chk_bajas = $("#chk_bajas").prop("checked");


	$.ajax({
				type: 'POST',
				data: 'action='+tipo_consulta+'&type='+type+'&inputtype='+inputtype+'&olt='+olt+'&slot='+slot+'&port='+port+'&chk_bajas='+chk_bajas,
				dataType: 'json',
				url: 'honeyajax.php',
				success: function(data) {





					var tablatr= `<div class='col-md-12'>
									<table id='tablalistaont' class='table table-striped'>

										<thead>
										  <tr style='color:#195F82'>
											<th class='tableontlist'>Número de serie</th>
											<th class='tableontlist'>F/S/P ONT-ID</th>
											<th class='tableontlist'>Modelo</th>
											<th class='tableontlist'>ID Servicio</th>
											<th class='tableontlist'>Plan</th>
											<th class='tableontlist'>Línea</th>
											<th class='tableontlist'><div class="input-group" style="width:210px; float:right"><input type="text"  class="search form-control" placeholder="Escriba para buscar"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div></th>
											<th class='tableontlist colnif hidden'>DNI</th>
										 </tr>
										</thead>
									<tbody id='cuerpotabla'>
									</tbody>
									</table>
								</div>`;

					if(window.location.pathname == "/honeypon/main.py"){
						tablatr = `<div class='col-md-12'>
										<table id='tablalistaont' class='table table-striped'>

											<thead>
											  <tr style='color:#195F82'>
												<th class='tableontlist'>Nombre</th>
												<th class='tableontlist'>Dirección</th>
												<th class='tableontlist'>DNI</th>
												<th class='tableontlist'>Teléfono</th>
												<th class='tableontlist'>ID Servicio</th>
												<th class='tableontlist'>Plan</th>
												<th class='tableontlist'><div class="input-group" style="width:210px; float:right"><input type="text"  class="search form-control" placeholder="Escriba para buscar"><span class="input-group-addon"><i class="glyphicon glyphicon-search"></i></span></div></th>
												<th class='tableontlist colnif hidden'>DNI</th>
											 </tr>
											</thead>
										<tbody id='cuerpotabla'>
										</tbody>
										</table>
									</div>`;
					};

					$('#spantablaont').html(tablatr);
					$('#cuerpotabla').html();

					for(var i in data.result) {
					var resultconsulta = data.result[i];

						$('#cuerpotabla').append(resultconsulta.registroont);
					};
					//alert(data.consulta);
					// Empty JS for your own code to be here

					var $rows = $('.danger, .info, .default, .warning');
					$('.search').keyup(function() {
						var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();

						$rows.show().filter(function() {
							var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
							return !~text.indexOf(val);
						}).hide();
					});

					$('body').on('hidden.bs.modal', '.modal fade', function () {
							$(this).removeData('bs.modal');
						  });



					// SCRIPTS DATATABLES


					$('#tablalistaont').dataTable({
					dom: 'Bfrtip',
					buttons: [
						{
						extend: 'copyHtml5',
						exportOptions: {
						columns: [ 0,1,2,3,4,5,7]
						}
						},
						{
						extend: 'excelHtml5',
						title: "LISTADO ONT",
						sheetName: "ONT",
						exportOptions: {
						columns: [ 0,1,2,3,4,5,7]
						}
						},

						{
						extend: 'pdfHtml5',
						title: "LISTADO ONT",
						orientation: 'landscape',
						pageSize: 'LEGAL',
						exportOptions: {
						columns: [ 0,1,2,3,4,5,7]
						}
						},
						{
						extend: 'print',
						title: "LISTADO ONT",
						exportOptions: {
						columns: [ 0,1,2,3,4,5,7]
						}
						},


					],
					columnDefs: [
						{ orderable: false, targets: [6] },


						],

					"searching": false,
					scrollY: 600,
					paging: false,
					"language": {
					"infoEmpty": "Ninguna entrada que mostrar",
					"info": "Mostrando _TOTAL_ entradas",
					"emptyTable": "No hay registros disponibles"
					}

				} );

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



					}
				});







}

// Función que ejecuta el seleccionable de tipo de filtro para ONT
function tipofiltroont() {
	if ($("#seltype").val() == "filtro"){
		$(".columnainputtype").addClass("hidden");
		$(".columnafiltro").removeClass("hidden");
	}else{
		$(".columnainputtype").removeClass("hidden");
		$(".columnafiltro").addClass("hidden");
	}
}





function clientassoc(idservicio){
		// AJAX QUE OBTIENE LOS DATOS DE CLIENTE
		$.ajax({
			type: 'POST',
			data: 'action=getclientassoc&idservicio='+idservicio,
			dataType: 'json',
			url: 'honeyajax.php',
			success: function(data) {

				$(".title_id_client").html(idservicio);

				$('#nameassoc').html(data.nombre);
				$('#dirassoc').html(data.dircliente);
				$('#tlfassoc').html(data.tlfcliente);
				$('#nifassoc').html(data.nif);

				$('#planassoc').html(data.plan);
				$('#oltassoc').html(data.olt);
				$('#cgnatstatus').html(data.ifcgnat);

				$('#pppoestatus').html(data.pppoe);
				$('#pppoeuser').html(data.userpppoe);
				$('#pppoesecret').html(data.passpppoe);


				$('#sipstatus').html(data.sip);
				$('#sipextension').html(data.sipextension);
				$('#sipsecret').html(data.sipsecret);
				$('#sipserver').html(data.sipserver);


				$('#bridgestatus').html(data.bridge);

			}

			});
}


function edit_clientassoc(idservicio){
	// AJAX QUE OBTIENE LOS DATOS DE CLIENTE PARA SU EDICIÓN

	$("#modal_editar_cliente").modal("toggle");
	$.ajax({
		type: 'POST',
		data: 'action=getclientassoc&idservicio='+idservicio,
		dataType: 'json',
		url: 'honeyajax.php',
		success: function(data) {



			$(".title_id_client").html(idservicio);
			$("#id_cliente").val(idservicio);

			$('#editar_inputnamecliente').val(data.nombre);
			$('#editar_inputdireccion').val(data.dircliente);
			$('#editar_inputtelf').val(data.tlfcliente);
			$('#editar_inputdni').val(data.nif);

			$("#editar_cliente_selectplan option:contains("+data.plan+")").prop('selected', true)
			loadoltlist($('#editar_cliente_selectplan option:selected').val())
			$("#editar_cliente_olt option:contains("+data.olt+")").prop('selected', true)

			if(data.has_service == true){

			  $(".service-active").prop('disabled',true)


			  if(data.userpppoe == null){
			    $('#editar_inputarrendpppoe').prop('checked',false);
			    $(".editar_pppoefield").addClass('hidden');
			    $("#editar_inputuserpppoe").val("")
			    $("#editar_inputpasspppoe").val("")
			    $("#editar_inputuserpppoe").prop('disabled', true);
			    $("#editar_inputpasspppoe").prop('disabled', true);
			  }else{
			    $('#editar_inputarrendpppoe').prop('checked',true);

			    $("#editar_inputuserpppoe").val(data.userpppoe)
			    $("#editar_inputpasspppoe").val(data.passpppoe)

			    $("#editar_inputuserpppoe").prop('disabled', false);
			    $("#editar_inputpasspppoe").prop('disabled', false);

			    $(".editar_pppoefield").removeClass('hidden');
			  }


			  if(data.sipextension == null){
			    $('#editar_inputsip').prop('checked',false);

			    $(".editar_sip").addClass('hidden');
			    $("#editar_inputserversip").val($("#editar_inputserversip option:first").val());
			    $("#editar_inputextensionsip").val("")
			    $("#editar_inputsecretsip").val("")


			  }else{

			    $("#editar_inputserversip option:contains("+data.sipserver+")").prop('selected', true)

			    $('#editar_inputsip').prop('checked',true);

			    $("#editar_inputextensionsip").val(data.sipextension)
			    $("#editar_inputsecretsip").val(data.sipsecret)

			    $(".editar_sip").removeClass('hidden');
			  }

			}else{

			  $("#editar_cliente_selectplan").prop('disabled', false);
			  $("#editar_cliente_selectolt").prop('disabled', false);
			  $('#editar_inputsip').prop('disabled', false);

			  if(data.userpppoe == null){
			    $('#editar_inputarrendpppoe').prop('checked',false);
			    $(".editar_pppoefield").addClass('hidden');
			    $("#editar_inputuserpppoe").val("")
			    $("#editar_inputpasspppoe").val("")
			    $("#editar_inputuserpppoe").prop('disabled', true);
			    $("#editar_inputpasspppoe").prop('disabled', true);
			  }else{
			    $('#editar_inputarrendpppoe').prop('checked',true);

			    $("#editar_inputuserpppoe").val(data.userpppoe)
			    $("#editar_inputpasspppoe").val(data.passpppoe)

			    $("#editar_inputuserpppoe").prop('disabled', false);
			    $("#editar_inputpasspppoe").prop('disabled', false);

			    $(".editar_pppoefield").removeClass('hidden');
			  }


			  if(data.sipextension == null){
			    $('#editar_inputsip').prop('checked',false);
			    $('#editar_inputbridge').prop('disabled', false);

			    $(".editar_sip").addClass('hidden');
			    $("#editar_inputserversip").val($("#editar_inputserversip option:first").val());
			    $("#editar_inputextensionsip").val("")
			    $("#editar_inputsecretsip").val("")
			    $("#editar_inputextensionsip").prop('disabled', true);
			    $("#editar_inputsecretsip").prop('disabled', true);
			    $("#editar_inputserversip").prop('disabled', true);

			  }else{

			    $("#editar_inputserversip option:contains("+data.sipserver+")").prop('selected', true)

			    $('#editar_inputsip').prop('checked',true);
			    $('#editar_inputbridge').prop('disabled', true);

			    $("#editar_inputextensionsip").val(data.sipextension)
			    $("#editar_inputsecretsip").val(data.sipsecret)

			    $("#editar_inputextensionsip").prop('disabled', false);
			    $("#editar_inputsecretsip").prop('disabled', false);
			    $("#editar_inputserversip").prop('disabled', false);

			    $(".editar_sip").removeClass('hidden');
			  }

			}

		}

		});

}


function showontpppoedata(idservicio){
	$(".pppoedata").toggleClass("hidden");


}

function showontsipdata(idservicio){
	$(".sipdata").toggleClass("hidden");
}


function listar_olt(){
		// AJAX QUE OBTIENE LA LISTA DE LA OLT
		$.ajax({
			type: 'POST',
			data: 'action=get_olt_list',
			dataType: 'json',
			url: 'honeyajax.php',
			success: function(data) {

				for(var i in data.oltlist) {
					var resultconsulta = data.oltlist[i];
					$('#selectolt').append(resultconsulta.registro_olt);

				};


			}

			});
}

function listar_planes(){
		// AJAX QUE OBTIENE LA LISTA DE LA OLT
		$.ajax({
			type: 'POST',
			data: 'action=get_planes_list',
			dataType: 'json',
			url: 'honeyajax.php',
			success: function(data) {

				for(var i in data.planlist) {
					var resultconsulta = data.planlist[i];
					$('#cliente_selectplan').append(resultconsulta.registro_plan);
					$('#editar_cliente_selectplan').append(resultconsulta.registro_plan);

				};


			}

			});
}

function listar_serversip(){
		// AJAX QUE OBTIENE LA LISTA DE LA OLT
		$.ajax({
			type: 'POST',
			data: 'action=get_serversip_list',
			dataType: 'json',
			url: 'honeyajax.php',
			success: function(data) {

				for(var i in data.serversiplist) {
					var resultconsulta = data.serversiplist[i];
					$('#inputserversip').append(resultconsulta.registro_serversip);
					$('#editar_inputserversip').append(resultconsulta.registro_serversip);

				};


			}

			});
}



function has_service(estado){

if(estado == true){

  $(".service-active").prop('disabled',true)


  if(data.userpppoe == null){
    $('#editar_inputarrendpppoe').prop('checked',false);
    $(".editar_pppoefield").addClass('hidden');
    $("#editar_inputuserpppoe").val("")
    $("#editar_inputpasspppoe").val("")
    $("#editar_inputuserpppoe").prop('disabled', true);
    $("#editar_inputpasspppoe").prop('disabled', true);
  }else{
    $('#editar_inputarrendpppoe').prop('checked',true);

    $("#editar_inputuserpppoe").val(data.userpppoe)
    $("#editar_inputpasspppoe").val(data.passpppoe)

    $("#editar_inputuserpppoe").prop('disabled', false);
    $("#editar_inputpasspppoe").prop('disabled', false);

    $(".editar_pppoefield").removeClass('hidden');
  }


  if(data.sipextension == null){
    $('#editar_inputsip').prop('checked',false);

    $(".editar_sip").addClass('hidden');
    $("#editar_inputserversip").val($("#editar_inputserversip option:first").val());
    $("#editar_inputextensionsip").val("")
    $("#editar_inputsecretsip").val("")


  }else{

    $("#editar_inputserversip option:contains("+data.sipserver+")").prop('selected', true)

    $('#editar_inputsip').prop('checked',true);

    $("#editar_inputextensionsip").val(data.sipextension)
    $("#editar_inputsecretsip").val(data.sipsecret)

    $(".editar_sip").removeClass('hidden');
  }

}else{

  $("#editar_cliente_selectplan").prop('disabled', false);
  $("#editar_cliente_selectolt").prop('disabled', false);
  $('#editar_inputsip').prop('disabled', false);

  if(data.userpppoe == null){
    $('#editar_inputarrendpppoe').prop('checked',false);
    $(".editar_pppoefield").addClass('hidden');
    $("#editar_inputuserpppoe").val("")
    $("#editar_inputpasspppoe").val("")
    $("#editar_inputuserpppoe").prop('disabled', true);
    $("#editar_inputpasspppoe").prop('disabled', true);
  }else{
    $('#editar_inputarrendpppoe').prop('checked',true);

    $("#editar_inputuserpppoe").val(data.userpppoe)
    $("#editar_inputpasspppoe").val(data.passpppoe)

    $("#editar_inputuserpppoe").prop('disabled', false);
    $("#editar_inputpasspppoe").prop('disabled', false);

    $(".editar_pppoefield").removeClass('hidden');
  }


  if(data.sipextension == null){
    $('#editar_inputsip').prop('checked',false);
    $('#editar_inputbridge').prop('disabled', false);

    $(".editar_sip").addClass('hidden');
    $("#editar_inputserversip").val($("#editar_inputserversip option:first").val());
    $("#editar_inputextensionsip").val("")
    $("#editar_inputsecretsip").val("")
    $("#editar_inputextensionsip").prop('disabled', true);
    $("#editar_inputsecretsip").prop('disabled', true);
    $("#editar_inputserversip").prop('disabled', true);

  }else{

    $("#editar_inputserversip option:contains("+data.sipserver+")").prop('selected', true)

    $('#editar_inputsip').prop('checked',true);
    $('#editar_inputbridge').prop('disabled', true);

    $("#editar_inputextensionsip").val(data.sipextension)
    $("#editar_inputsecretsip").val(data.sipsecret)

    $("#editar_inputextensionsip").prop('disabled', false);
    $("#editar_inputsecretsip").prop('disabled', false);
    $("#editar_inputserversip").prop('disabled', false);

    $(".editar_sip").removeClass('hidden');
  }
};


}
