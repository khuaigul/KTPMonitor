
function showPupilProfileInfo()
{
	// var a = '{"surname": "Иванов", "name": "Иван", "secondname" : "Иванович","division" : "A", "mail" : "ivan@gmail.com", "phone" : "+79999999999", "datebirth" : "12.02.2000", "school" : "42", "grade" : "8"}';
	// return showProfile(a);
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			//alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_profile_Json = xhr_d.responseText;
			showProfile(get_profile_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/currentProfileData?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showProfile(profileJson)
{
	var data = JSON.parse(profileJson);
	let name = document.getElementById("fullPupilName");
	alert(name);
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


	document.getElementById("mydiv").setAttribute("onclick", 'toDivision("' + data["division"] +'")');
  console.log(document.getElementById("mydiv"));
}

function toDivision(division)
{
	document.location = "pupilDivision?division=" + encodeURIComponent(division);
}


function validatePhone(phone) {
  // проверяем, что телефон соответствует формату +7 (XXX) XXX-XXXX
  // var phoneRegex = /^\+7 \(\d{3}\) \d{3}-\d{4}$/;
  // return phoneRegex.test(phone);
	return true;
}

function validateBirthday(birthday) {
  // проверяем, что дата соответствует формату YYYY-MM-DD и является корректной датой
  // var dateRegex = /^\d{4}-\d{2}-\d{2}$/;
  // if (!dateRegex.test(birthday)) {
  //   return false;
  // }
  var date = new Date(birthday);
  var currentDate = new Date();
  // alert(date);
  // alert(currentDate);
  if (date > currentDate) {
    return false;
  }
  return true;
}

function validateForm() {
	//alert("fgbfgb");
  var surname = document.getElementById("surname").value;
  //alert("1");
  var name = document.getElementById("name").value;
  //alert("1");
  
  var patronymic = document.getElementById("patronymic").value;
  //alert("1");
  
  var phone = document.getElementById("phone").value;
  //alert("1");
  
  var school = document.getElementById("school").value;
  //alert("1");
  
  var classNumber = document.getElementById("class").value;
  //alert("1");
  
  //alert(document.getElementById("birthday").value);
  var birthday = document.getElementById("birthday").value;
  //alert("1");
  
  var nickname = document.getElementById("nickname").value;
  //alert("1");

  //alert(surname);
  // проверяем, что все поля заполнены
  if (surname == "" || name == "" || patronymic == "" ||phone == "" || school == "" ||classNumber == "" ||birthday == "" || nickname == "") 
  {
    alert("Пожалуйста, заполните все поля");
    return false;
  }
  //alert("aa");

  // проверяем, что телефон и дата рождения соответствуют формату
  if (!validatePhone(phone)) {
    alert("Пожалуйста, введите корректный номер телефона в формате +7 (XXX) XXX-XXXX");
    return false;
  }
  if (!validateBirthday(birthday)) {
    alert("Пожалуйста, введите корректную дату рождения в формате YYYY-MM-DD");
    return false;
  }

  return true;
}

function save() {
  // event.preventDefault();
	//alert(validateForm());

  if (validateForm()) {
    // отправляем данные на сервер
    //alert("AAA");
    var surname = document.getElementById("surname").value;
	var name = document.getElementById("name").value;
	var patronymic = document.getElementById("patronymic").value;
	var phone = document.getElementById("phone").value;
	var school = document.getElementById("school").value;
	var classNumber = document.getElementById("class").value;
	var nickname = document.getElementById("nickname").value;
	
  var xhr = new XMLHttpRequest();

	var params = 'surname=' + encodeURIComponent(surname) +
		'&firstname=' + encodeURIComponent(name) + 
		'&secondname=' + encodeURIComponent(patronymic)+
		'&nickname=' + encodeURIComponent(nickname)+
		'&phone=' + encodeURIComponent(phone) + 
		'&school=' + encodeURIComponent(school) +
    '&grade=' + encodeURIComponent(classNumber);
	

	xhr.open("POST", 'http://127.0.0.1:8000/updatePupilProfileData?', true);
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
				document.location = "pupilProfile";
			}
		}
	}
	
  }
}

// document.getElementById("save").addEventListener("click", handleSubmit);

function editProfile()
{
  document.location = "edit_pupil_profile";
}

function fill_profile()
{
  var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			console.log(xhr_d.responseText);
			get_profile_Json = xhr_d.responseText;
			showInfo(get_profile_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/currentProfileData?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showInfo(info)
{
  var data = JSON.parse(info);
  console.log(data);
  
  var surname = document.getElementById("surname");
  surname.value = data["surname"];
	var name = document.getElementById("name");
  name.value = data["firstname"];
	var patronymic = document.getElementById("patronymic");
  patronymic.value = data["secondname"];
	var phone = document.getElementById("phone");
  phone.value = data["phone"];
	var school = document.getElementById("school");
  school.value = data["school"];
	var classNumber = document.getElementById("class");
  classNumber.value = data["grade"];
	var nickname = document.getElementById("nickname");
  nickname.value = data["nickname"];
}