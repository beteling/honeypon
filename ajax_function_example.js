function control_errorres_ajax(){

	var jsonData = {
	                    "something":"??"
	                };
	jsonData = JSON.stringify(jsonData);
	var onSuccess = function(data){
	    console.log("Ajax Success!");
	    console.log(data);
	}

	var onError = function(jqXHR, textStatus, errorThrown){
	                    console.log("Ajax Error: "+textStatus);
	                    console.log("More info:");
	                    console.log(errorThrown);
	                    console.log(jqXHR);
	                };
	$.ajax({
		type: 'POST',
		data: jsonData,
		dataType: 'json',
		jsonp: false,
		url: 'prodevents.php',
		error:onError,
		success: onSuccess
		});
}
