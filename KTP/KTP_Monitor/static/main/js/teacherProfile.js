function editProfile()
{
	document.location="editTeacherProfile";
}

function showProfileInfo()
{
	// var a = '{"surname": "Иванов", "firstname": "Иван", "secondname" : "Иванович","division" : "A", "mail" : "ivan@gmail.com", "phone" : "+79999999999"}';
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
	let name = document.getElementById("fullTeacherName");
	name.innerHTML = data["surname"] + " " + data["firstname"] + " "  + data["secondname"];

	let divText = document.getElementById("div");
	divText.innerHTML = "Преподаватель дивизиона " + data["division"];

	let mailText = document.getElementById("mail");
	mailText.innerHTML = data["email"];

	let phoneText = document.getElementById("telegram");
	phoneText.innerHTML = data["phone"];
}

function save_changes()
{
	var lastname = document.querySelectorAll("#lastname input")[0].value;
	var firstname = document.querySelectorAll("#firstname input")[0].value;
	var secondname = document.querySelectorAll("#secondname input")[0].value;
	var nickname = document.querySelectorAll("#nickname input")[0].value;
	var div = document.querySelectorAll("#division select")[0];
	var phone = document.querySelectorAll("#phone input")[0].value;

	div = div.options[div.selectedIndex].text;

	var xhr = new XMLHttpRequest();

	var params = 'surname=' + encodeURIComponent(lastname) +
		'&name=' + encodeURIComponent(name) + 
		'&secondname=' + encodeURIComponent(secondname)+
		'&nickname=' + encodeURIComponent(nickname)+
		'&phone=' + encodeURIComponent(phone) + 
		'&division=' + encodeURIComponent(div);

	console.log(params);

	// xhr.open("POST", 'http://127.0.0.1:8000/updateTeacherProfileData?', true);
	// xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr.send(params);

	// xhr.onload = function(){
	// 	if (xhr.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else {
	// 		getJson = xhr.responseText;
	// 		const obj = JSON.parse(getJson);
	// 		console.log(obj["status"]);
	// 		if (obj["status"] == true){
	// 			document.location = "main";
	// 		}
	// 	}
	// }
}

function add_divisions_select(div_json)
{
	const divs = JSON.parse(div_json);
	console.log("fgg");
	console.log(divs);

	let select = document.querySelectorAll(".usual_selector");

	for (var j = 0; j < divs["divisions"].length; j++)
	{
		let opt = document.createElement("option");
		opt.innerHTML = divs["divisions"][j];
		select[0].appendChild(opt);
	}
}

function getJson_divs()
{
	var xhr_d = new XMLHttpRequest();

	// var a = '{"divisions":["A", "B", "C"]}';
	// return add_divisions_select(a);

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			return add_divisions_select(get_div_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divisionsRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showInfo(info) 
{
	console.log(info);
	const data = JSON.parse(info);
	let surname = document.querySelectorAll("#lastname input")[0];
	surname.value = data["surname"];
	let name = document.querySelectorAll("#firstname input")[0];
	name.value = data["firstname"];
	let secondname = document.querySelectorAll("#secondname input")[0];
	secondname.value = data["secondname"];
	let nickname = document.querySelectorAll("#nickname input")[0];
	nickname.value = data["nickname"];
	let phone = document.querySelectorAll("#phone input")[0];
	phone.value = data["phone"];
	let div = document.querySelectorAll("#usual_selector")[0];
	let opts = document.querySelectorAll("#usual_selector option");
	// alert(opts.length);
	for (var j = 0; j < opts.length; j++)
	{
		console.log(opts[j].innerHTML);
		if (opts[j].innerHTML == data["divisions"])
			div.selectedIndex = j;
	}
}

function fill_profile()
{
	// var a = '{"nickname": "ivann", "surname": "Иванов", "firstname": "Иван", "secondname" : "Иванович","division" : "B", "mail" : "ivan@gmail.com", "phone" : "+79999999999"}';
	// return showInfo(a);
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			console.log(xhr_d.responseText);
			get_profile_Json = xhr_d.responseText;
			return showInfo(get_profile_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/currentProfileData?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

