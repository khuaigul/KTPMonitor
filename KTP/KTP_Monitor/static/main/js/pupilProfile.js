
function showPupilProfileInfo()
{
	// var a = '{"surname": "Иванов", "name": "Иван", "secondname" : "Иванович","division" : "A", "mail" : "ivan@gmail.com", "phone" : "+79999999999", "datebirth" : "12.02.2000", "school" : "42", "grade" : "8"}';
	// return showProfile(a);
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
	const data = JSON.parse(profileJson);
	let name = document.getElementById("fullPupilName");
	console.log(name);
	name.innerHTML = data["surname"] + " " + data["firstname"] + " "  + data["secondname"];

	let divText = document.getElementById("div");
	divText.innerHTML = "Ученик дивизиона " + data["division"];

	let mailText = document.getElementById("mail");
	mailText.innerHTML = data["email"];

	let phoneText = document.getElementById("telegram");
	phoneText.innerHTML = data["phone"];

	let datebirth = document.getElementById("datebirth");
	datebirth.innerHTML = "Дата рождения: " + data["datebirth"];

	document.getElementById("school").innerHTML = "Школа: " + data["school"];
	document.getElementById("grade").innerHTML = "Класс: " + data["grade"];

}