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
	console.log("show");
	let dv = document.querySelectorAll(".header_empty");
	let header = document.createElement("h1");
	var nickName = localStorage.getItem('nicknameToShow');
	header.innerHTML = "Профиль школьника: " + nickName;
	dv[0].appendChild(header);

	console.log(student_info);
	const info = JSON.parse(student_info);

	make_info_element(info["surname"], "Фамилия");
	make_info_element(info["name"], "Имя");
	make_info_element(info["secondname"], "Отчество");
	make_info_element(info["div"], "Дивизион");
	make_info_element(info["nickname"], "Ник на Codeforces");
	make_info_element(info["datebirth"], "Дата рождения");
	make_info_element(info["school"], "Школа");
	make_info_element(info["form"], "Класс");
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



function show_students_list()
{
	var students_list = localStorage.getItem('studentList');
	var div_list = localStorage.getItem('divList');
	console.log("third", students_list);
	const obj = JSON.parse(students_list);
	const div = JSON.parse(div_list);

	console.log(div);

	console.log(obj["students"].length);

	obj["students"].sort(function(a, b){
		console.log("sort");
		if (a["div"] == "не выбрано")
		{
			console.log("sort1");
			return 1;
		}
		else if (b["div]"] == "не выбрано")
		{
			console.log("sort2");
			return 0;
		}
		else
		{
			console.log("sort3");
			return a["div"] < b["div"];
		}
	});

	for (var i = 0; i < obj["students"].length; i++)
	{
		let par = document.createElement("p");
		let nickName = document.createElement("a");
		let name = document.createElement("a");
		nickName.innerHTML = obj["students"][i]["nickname"];
		// nickName.setAttribute("onclick", 'show_student(' + obj["students"][i]["nickname"] + ')');
		nickName.setAttribute("class", "link");
		nickName.addEventListener('click', function(){
			show_student_page(nickName.innerHTML)});
		console.log("MADE");
		name.innerHTML = ": " + obj["students"][i]["surname"] + " " + obj["students"][i]["name"] + " " + obj["students"][i]["secondname"]
		let div_change = document.createElement("select");
		for (var j = 0; j < div["divisions"].length; j++)
		{
			if (div["divisions"][j] == obj["students"][i]["div"])
			{
				let opt = document.createElement("option");
				opt.setAttribute("selected", "selected"); 
				opt.innerHTML = div["divisions"][j];
				div_change.appendChild(opt);
			}
			else
			{
				let opt = document.createElement("option");
				opt.innerHTML = div["divisions"][j];
				div_change.appendChild(opt);
			}
		}
		par.appendChild(nickName);
		par.appendChild(name);
		var id = "nickname_" + obj["students"][i]["nickname"];
//		alert(id);
		div_change.setAttribute('id', id);
		par.appendChild(div_change);
		let dv = document.querySelectorAll("#students_list");
		dv[0].appendChild(par);
//		document.body.appendChild(dv[0]);
	}

//	console.log(obj["students"][0]);
}