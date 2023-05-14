
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

}


function validatePhone(phone) {
  // проверяем, что телефон соответствует формату +7 (XXX) XXX-XXXX
  // const phoneRegex = /^\+7 \(\d{3}\) \d{3}-\d{4}$/;
  // return phoneRegex.test(phone);
	return true;
}

function validateBirthday(birthday) {
  // проверяем, что дата соответствует формату YYYY-MM-DD и является корректной датой
  // const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
  // if (!dateRegex.test(birthday)) {
  //   return false;
  // }
  const date = new Date(birthday);
  const currentDate = new Date();
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
  const name = document.getElementById("name").value;
  //alert("1");
  
  const patronymic = document.getElementById("patronymic").value;
  //alert("1");
  
  const phone = document.getElementById("phone").value;
  //alert("1");
  
  const school = document.getElementById("school").value;
  //alert("1");
  
  const classNumber = document.getElementById("class").value;
  //alert("1");
  
  //alert(document.getElementById("birthday").value);
  const birthday = document.getElementById("birthday").value;
  //alert("1");
  
  const nickname = document.getElementById("nickname").value;
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
    const surname = document.getElementById("surname").value;
	const name = document.getElementById("name").value;
	const patronymic = document.getElementById("patronymic").value;
	const phone = document.getElementById("phone").value;
	const school = document.getElementById("school").value;
	const classNumber = document.getElementById("class").value;
	const birthday = document.getElementById("birthday").value;
	const nickname = document.getElementById("nickname").value;
	

	alert(surname);
	alert(name);
	alert(patronymic);
	alert(phone);
	alert(school);
	alert(classNumber);
	alert(birthday);
	alert(nickname);

    alert("Данные отправлены на сервер");
  }
}

// document.getElementById("save").addEventListener("click", handleSubmit);
