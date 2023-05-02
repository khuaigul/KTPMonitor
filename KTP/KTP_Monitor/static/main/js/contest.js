function show()
{
	var paramValue = window.location.href.split("?")[1].split("=");
	console.log(paramValue);

	var params = 'division=' + encodeURIComponent(name);
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			var a = 0;
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/testParams?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}