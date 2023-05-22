function toProfile()
{
	document.location="pupilProfile";
}

function toDivisions()
{
	document.location="pupilDivision";
}

function toExit()
{
	alert("Выйти из профиля?");
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			document.location="main";	
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/logout?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}