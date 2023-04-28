function setName(name)
{
	document.querySelectorAll(".name_header")[0].innerHTML = name;
}

function getPupilInfo()
{
	var str = '{"name" : "Никита", "surname" : "Анисимов", "secondname" : "Николаевич", "datebirth" : "03.10.2002", "school" : "42", "grade" : "10", "email" : "email@email", "phone" : "876543"}';
	alert(str);
	return showPupil(str); 
	var params = "nickname=" + window.location.href.split("?")[1].split("=")[1];
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_pupil_Json = xhr_d.responseText;
	// 		showPupil(get_pupil_Json);
	// 	}
	// }
	// xhr_d.open("GET", 'http://127.0.0.1:8000/pupilInfo?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);
}

function showPupil(pupil_json)
{
	pupil = JSON.parse(pupil_json);
	alert(pupil);
	setname(pupil["surname"] + " " + pupil["name"] + "" + pupil["secondname"]);
}