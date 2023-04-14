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
			alert(getJson);
			const obj = JSON.parse(getJson);
			if (obj["status"] == true){
				// if (obj["role"] == "student")
				// 	document.location = "studentProfile";
				// else if (obj["role"] == "teacher")
				document.location = "teacherProfile";
				// else
				// 	document.location = "admin";
			}
			else
			{
				alert(document.querySelectorAll(".note").length);
				document.querySelectorAll(".note")[0].innerHTML = "Некорректные логин или пароль";
				document.getElementById("login_input").value = "";
				document.getElementById("password_input").value = "";				
			}
			alert(xhr.responseText);
			return true;
		}
	}
	return false;
}
function enter()
{
	let login = document.querySelectorAll("#login_input > input");
	let password = document.querySelectorAll("#password_input > input");

	var input = document.querySelectorAll("#password_input > input");

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
	// alert("send" + email + " " + password);
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

function send_profile_data(uid)
{
	let role = document.querySelectorAll("#role_selector > select")[0].value;
	
	var lastname = document.querySelectorAll("#lastname input");
	var firstname = document.querySelectorAll("#firstname input");
	var secondname = document.querySelectorAll("#secondname input");
	var nickname = document.querySelectorAll("#nickname input");
	var phone = document.querySelectorAll("#phone input");
	var params;

	if (role == "student")
	{	
		role = "pupil";
		var datebirth = document.querySelectorAll("#birthdate input");
	    var school = document.querySelectorAll("#school input");
		var grade = document.querySelectorAll("#grade input");
		params = 'uid=' + encodeURIComponent(uid) + '&role=' + encodeURIComponent(role) + '&nickname=' + encodeURIComponent(nickname) +'&surname=' + encodeURIComponent(lastname) + "&firstname=" + encodeURIComponent(firstname) + "&secondname=" + encodeURIComponent(secondname) + "&school=" + encodeURIComponent(school) + "&grade=" + encodeURIComponent(grade) + "&datebirth=" + encodeURIComponent(datebirth)+ "&phone=" + encodeURIComponent(phone);
	}
	else
	{
		params = 'uid=' + encodeURIComponent(uid) + '&role=' + encodeURIComponent(role) + '&nickname=' + encodeURIComponent(nickname) +'&surname=' + encodeURIComponent(lastname) + "&firstname=" + encodeURIComponent(firstname) + "&secondname=" + encodeURIComponent(secondname) + "&phone=" + encodeURIComponent(phone);
	}

	var xhr = new XMLHttpRequest();


	xhr.open("POST", 'http://127.0.0.1:8000/sendProfileData?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);

	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка {xhr.status} : {xhr.statusText}');
		}
		else {
			getJson = xhr.responseText;
			alert(getJson);
			const obj = JSON.parse(getJson);
			console.log(obj["status"]);
			if (obj["status"] == true){
				document.location = "http://127.0.0.1:8000/main";
			}
		}
	}
}

function checkEmail(email)
{
	var re = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
	return re.test(email);
}

function checkPassword(password)
{
	const withoutSpecialChars = /^[^-() /]*$/;
	const containsLetters = /^.*[a-zA-Z]+.*$/;
	const minimum8Chars = /^.{8,}$/;
	const withoutSpaces = /^[\S]$/;

	if (withoutSpaces.test(password))
	{
		return "withoutSpaces";
	}
	if (!withoutSpecialChars.test(password))
	{
		return "withoutSpecialChars";
	}
	if (!containsLetters.test(password))
	{
		return "containsLetters";
	}
	if (!minimum8Chars.test(password))
	{
		return "minimum8Chars";
	}
	return "correct";
}

function register()
{
	let block = document.querySelectorAll(".block")[0];
	if (document.getElementById("errortext") != null)
		block.removeChild(document.getElementById("errortext"));
	if (document.getElementById("errortext2") != null)
		block.removeChild(document.getElementById("errortext2"));
	let email = document.querySelectorAll("#email > input")
	let password = document.querySelectorAll("#password > input")
	let password2 = document.querySelectorAll("#password2 > input")
	if (email[0].value == "" || password[0].value == "" || password2[0].value == "")
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Заполните поля";
		text1.setAttribute("id", "errortext")
		text1.setAttribute("class", "note")

		block.appendChild(text1);
	}
	else if (password[0].value != password2[0].value)
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Пароли не совпадают";
		text1.setAttribute("id", "errortext2")
		text1.setAttribute("class", "note")

		block.appendChild(text1);
	}
	else if (!checkEmail(email[0].value))
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "Неверный формат почты";
		text1.setAttribute("id", "errortext2")
		text1.setAttribute("class", "note")

		block.appendChild(text1);
	}
	else if(checkPassword(password[0].value) != "correct")
	{
		let text1 = document.createElement("p");
		text1.innerHTML = "";
		text1.setAttribute("id", "errortext2")
		text1.setAttribute("class", "note")

		var error = checkPassword(password[0].value);
		if (error == "minimum8Chars")
			text1.innerHTML = "Пароль должен содержать не менее 8-ми символов";
		else if (error == "withoutSpaces")
			text1.innerHTML = "Пароль не должен содержать символы пробела";
		else if (error == "withoutSpecialChars")
			text1.innerHTML = "Пароль не должен содержать специальных символов \"^-() /\"";
		else if (error == "containsLetters")
			text1.innerHTML = "Пароль должен содержать символы латинского алфавита";
		block.appendChild(text1);
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

function register_save(uid)
{
	// alert(uid)
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
	var now = new Date();
	var today = now.getFullYear() + '-';
	var month = now.getMonth() + 1;
	if (month < 10)
		today = today + '0';
	today = today + month + '-';
	if(now.getDate() < 10)
		today = today + '0';
	today = today + now.getDate();
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
		var text = document.querySelectorAll(".note")[1];
		text.innerHTML = "Заполните все поля ввода";
		// let cur_div = document.querySelectorAll(".block")
		// cur_div[0].appendChild(text);
	}
	else if (role == "student" && document.querySelectorAll("#birthdate input")[0].value > today)
	{
		var text = document.querySelectorAll(".note")[1];
		text.innerHTML = "Неверно введённая дата рождения";
	}
	else
	{
		send_profile_data(uid);
	}
}

function change_role()
{
	let sel = document.querySelectorAll("#role_selector > select");
	let forms = document.querySelectorAll(".student");
	var text = document.querySelectorAll(".note")[1];
	text.innerHTML="";
	for (var i = 0; i < forms.length; i++)
	{
		console.log(forms[i]);
		if (sel[0].value == "student")
			forms[i].removeAttribute("hidden");
		else
			forms[i].setAttribute("hidden", "hidden");
	}
}

// var input = document.querySelectorAll("#password_input > input");
// input[0].addEventListener("keyup", function(event) {
//   if (event.keyCode === 13) {
//     event.preventDefault();
//     document.getElementById("enterButton").click();
//   }
// });