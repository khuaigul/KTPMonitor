function authorisation(login, password)
{
	var xhr = new XMLHttpRequest();
	var params = 'login=' + encodeURIComponent(login) +'&password=' + encodeURIComponent(password);


	 xhr.open("POST", 'http://127.0.0.1:8000/signin?', true);
	 xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	 xhr.send(params); 
	 	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				document.location = "menu";
			}
			alert(xhr.responseText);
		}
	}
	return false;
}
function enter()
{
	let login = document.querySelectorAll("#login_input > input");
	let password = document.querySelectorAll("#password_input > input");

	if (login[0].value == "" || password[0].value == "")
		document.location="main";
	else
	{
		console.log("else");
		if (authorisation(login[0].value, password[0].value) == true)
		{
			console.log("auth");
			document.location = "menu";
		}
	}
}

function send_registration_data(email, password)
{
	alert("send" + email + " " + password);
	var xhr = new XMLHttpRequest();
	var params = 'email=' + encodeURIComponent(email) +'&password=' + encodeURIComponent(password);


	xhr.open("POST", 'http://127.0.0.1:8000/registrationRe?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);

 	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				alert("Письмо с подтверждением отправлено на вашу почту");
				document.location = "main";
			}
		}
	}
}

function send_profile_data()
{
	let role = document.querySelectorAll("#role_selector > select")[0].value;
	
	var lastname = document.querySelectorAll("#lastname input");
	var firstname = document.querySelectorAll("#firstname input");
	var secondname = document.querySelectorAll("#secondname input");
	var nickname = document.querySelectorAll("#nickname input");

	var params;

	if (role == "student")
	{	
		var datebirth = document.querySelectorAll("#birthdate input");
	    var school = document.querySelectorAll("#school input");
		var form = document.querySelectorAll("#form input");
		params = 'role' + encodeURIComponent(role) + 'nickname=' + encodeURIComponent(nickname) +'&surname=' + encodeURIComponent(lastname) + "&name=" + encodeURIComponent(firstname) + "&secondname=" + encodeURIComponent(secondname) + "&school=" + encodeURIComponent(school) + "&form=" + encodeURIComponent(form) + "&datebirth=" + encodeURIComponent(datebirth);
	}
	else
	{
		params = 'role' + encodeURIComponent(role) + 'nickname=' + encodeURIComponent(nickname) +'&surname=' + encodeURIComponent(lastname) + "&name=" + encodeURIComponent(firstname) + "&secondname=" + encodeURIComponent(secondname);
	}

	var xhr = new XMLHttpRequest();


	xhr.open("POST", 'http://127.0.0.1:8000/profileData?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);

	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				document.location = "main";
			}
		}
	}
}

function register()
{
	if (document.getElementById("errortext") != null)
		document.body.removeChild(document.getElementById("errortext"));
	if (document.getElementById("errortext2") != null)
		document.body.removeChild(document.getElementById("errortext2"));
	let email = document.querySelectorAll("#email > input")
	let password = document.querySelectorAll("#password > input")
	let password2 = document.querySelectorAll("#password2 > input")
	if (email[0].value == "" || password[0].value == "" || password2[0].value == "")
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Незаполненные поля";
		text1.setAttribute("id", "errortext")
		text1.setAttribute("class", "note")
		document.body.appendChild(text1);
	}
	else if (password[0].value != password2[0].value)
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Пароли не совпадают";
		text1.setAttribute("id", "errortext2")
		text1.setAttribute("class", "note")

		document.body.appendChild(text1);
	}
	else if (document.getElementById("infotext") == null)
	{
		let text = document.createElement("p");
		text.innerHTML = "Письмо с подтверждением отправлено на вашу почту";
		text.setAttribute("id", "infotext")
		text.setAttribute("class", "note")

		send_registration_data(email[0].value, password[0].value);
	}
}

function register_save()
{
	if (document.getElementById("errortext") != null)
	{
		let cur_div = document.querySelectorAll(".block")
		cur_div[0].removeChild(document.getElementById("errortext"));
	}
	let fields = document.querySelectorAll(".all_users input");
	var flag = new Boolean(true);
	for (var i = 0; i < fields.length; i++)
		if (fields[i].value == "")
			flag = false;
	let role = document.querySelectorAll("#role_selector > select")[0].value;
	if (role == "student")
	{
		let st_fields = document.querySelectorAll(".student input");
		for (var i = 0; i < st_fields.length; i++)
			if (st_fields[i].value == "")
				flag = false;
	}
	if (!flag)
	{
		let text = document.createElement("p");
		text.innerHTML = "Заполните все поля ввода";
		text.setAttribute("id", "errortext");
		text.setAttribute("class", "note");
		let cur_div = document.querySelectorAll(".block")
		cur_div[0].appendChild(text);
	}
	else
	{
		send_profile_data();
	}
}

function change_role()
{
	let sel = document.querySelectorAll("#role_selector > select");
	let forms = document.querySelectorAll(".student");
	for (var i = 0; i < forms.length; i++)
	{
		console.log(forms[i]);
		if (sel[0].value == "student")
			forms[i].removeAttribute("hidden");
		else
			forms[i].setAttribute("hidden", "hidden");
	}
}
