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
	document.location="main";
}

function showPupilProfileInfo()
{
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_profile_Json = xhr_d.responseText;
			return showProfile(get_profile_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/currentProfileData?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showProfile(profileJson)
{
	var a = '{"surname": "Иванов", "name": "Иван", "secondname" : "Иванович","division" : "A", "mail" : "ivan@gmail.com", "phone" : "+79999999999"}';
	return showProfile(a);
	
	// const data = JSON.parse(profileJson);
	// let name = document.getElementById("fullTeacherName");
	// name.innerHTML = data["surname"] + " " + data["name"] + " "  + data["secondname"];

	// let divText = document.getElementById("div");
	// divText.innerHTML = "Преподаватель дивизиона " + data["division"];

	// let mailText = document.getElementById("mail");
	// mailText.innerHTML = data["mail"];

	// let phoneText = document.getElementById("telegram");
	// phoneText.innerHTML = data["phone"];
}