function show_student_page(nickname)
{
	console.log("NICK", nickname);
//	document.location="student_profile";
	localStorage.setItem('nicknameToShow', nickname);
	document.location="student_profile";

}

function getJson_profile()
{
//	var profile_info = '{"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "A", "datebirth" : "12.05.2005", "school" : "Школа № 99", "form" : 10, "lastActivity" : "2 days ago"}';
	var nickname = localStorage.getItem('nicknameToShow');
	var params = 'nickname=' + encodeURIComponent(nickname);
//	return profile_info;

	var xhr = new XMLHttpRequest();
	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		} 
		else
		{
//			alert(xhr.responseText);
			show_student(xhr.responseText);
		}
	}
	xhr.open("POST", 'http://127.0.0.1:8000/studentProfile?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);
}

function make_info_element(value, position)
{
	let block = document.querySelectorAll(".block");
	let p = document.createElement("p");
	p.innerHTML = position + ": " + value;
	block[0].appendChild(p);
}

function getJson_students_divs()
{
	var xhr = new XMLHttpRequest();
	// var params = 'status=OK';
	

	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			getJson = xhr.responseText;

			var xhr_d = new XMLHttpRequest();

			xhr_d.onload = function(){
				if (xhr_d.status != 200){
					alert('Ошибка ${xhr.status} : ${xhr.statusText}');
				}
				else 
				{		
					get_div_Json = xhr_d.responseText;
					localStorage.setItem('studentList', getJson);
					localStorage.setItem('divList', get_div_Json);
					return show_students_list(getJson, get_div_Json);
				}
			}
			xhr_d.open("POST", 'http://127.0.0.1:8000/divisionsRe?', true);
			xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			xhr_d.send(null);
		}
	}
	xhr.open("POST", 'http://127.0.0.1:8000/studentData?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(null);
}


function show_student(student_info)
{
	alert(student_info)
	// console.log("show");
	// let dv = document.querySelectorAll(".header_empty");
	// let header = document.createElement("h1");
	// var nickName = localStorage.getItem('nicknameToShow');
	// header.innerHTML = "Профиль школьника: " + nickName;
	// dv[0].appendChild(header);

	// console.log(student_info);
	// const info = JSON.parse(student_info);

	// make_info_element(info["surname"], "Фамилия");
	// make_info_element(info["name"], "Имя");
	// make_info_element(info["secondname"], "Отчество");
	// make_info_element(info["div"], "Дивизион");
	// make_info_element(info["nickname"], "Ник на Codeforces");
	// make_info_element(info["datebirth"], "Дата рождения");
	// make_info_element(info["school"], "Школа");
	// make_info_element(info["form"], "Класс");
}

function set_new_div(name, div)
{
	var params = 'nickname=' + encodeURIComponent(name) + '&div=' + encodeURIComponent(div);
	var xhr = new XMLHttpRequest();
	alert(name, div);
	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		} 
		else
		{
			console.log(xhr.responseText)
		}
	}
	xhr.open("POST", 'http://127.0.0.1:8000/сhangeDiv?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);
}

function save_division_update()
{
	var students_list = localStorage.getItem('studentList');
	var div_list = localStorage.getItem('divList');
	const students = JSON.parse(students_list);
	for (var i = 0; i < students["students"].length; i++)
	{
		var nickname = students["students"][i]["nickname"];
		var sel = document.getElementById('nickname_' + nickname);
		if (sel.value != students["students"][i]["div"])
		{
		    alert(nickname, sel.value);
		    set_new_div(nickname, sel.value);
		}
	}
	document.location="students";
}

function show()
{
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			showPupils(get_div_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divisionsRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showPupils(json_divs)
{
	var divs = JSON.parse(json_divs)["divisions"];
	for (var i = 0; i < divs.length; i++)
	{
		var p = document.createElement("p");
		p.innerHTML = "Дивизион " + divs[i];
		document.querySelectorAll(".block")[0].appendChild(p);

		var str = '{"pupils":[{"surname":"Анисимов","name":"Никита","secondname":"Николаевич","nickname":"aaa"},{"surname":"Ройтбурд","name":"Дан","secondname":"Дмитриевич","nickname":"bbb"},{"name":"Наталья","surname":"Собянина","secondname":"Николаевна","nickname":"ccc"}]}';
		show_students_list(str, divs[i], divs);
		// var params = "name=" + divs[i];  
		// var xhr_d = new XMLHttpRequest();

		// xhr_d.onload = function(){
		// 	if (xhr_d.status != 200){
		// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		// 	}
		// 	else 
		// 	{
		// 		get_students_Json = xhr_d.responseText;
		// 		show_students_list(get_students_Json, divs[i], divs);
		// 	}
		// }
		// xhr_d.open("POST", 'http://127.0.0.1:8000/students_by_div?', true);
		// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		// xhr_d.send(params);
	}
}

function show_students_list(json_students, curDiv, divs)
{
	var students = JSON.parse(json_students)["pupils"];
	for (var i = 0; i < students.length; i++)
	{
		var cur_p = document.createElement("p");
		cur_p.setAttribute("class", "pupil");
		var a = document.createElement("a");
		a.setAttribute("class", "link");
		a.setAttribute("name", students[i]["nickname"]);
		a.addEventListener('click', function(){
			show_student(this.getAttribute("name"))});
		a.innerHTML = students[i]["surname"] + " " + students[i]["name"] + " " + students[i]["secondname"];
		
		var sel = document.createElement("select");
		console.log(divs);
		for (var j = 0; j < divs.length; j++)
		{
			var opt = document.createElement("option");
			opt.innerHTML = divs[j];
			sel.appendChild(opt);
		}
		sel.setAttribute("selected", curDiv);
		sel.setAttribute("name", curDiv);
		sel.setAttribute("class", "div_selector");

		cur_p.appendChild(a);
		cur_p.appendChild(sel);
		document.querySelectorAll(".block")[0].appendChild(cur_p);
	}

	var bt = document.createElement("button");
	bt.setAttribute("class", "usual_button");
	bt.setAttribute("onclick", save_changes());
}

function save_changes()
{
	var pupils = document.querySelectorAll(".pupil");
	for (var i = 0; i < pupils.length; i++)
	{
		if ()
	}
}