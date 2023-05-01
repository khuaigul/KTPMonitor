function toProfile()
{
	document.location="teacherProfile";
}
function toDivisions()
{
	document.location="divisions";
}
function toContests()
{
	document.location="contests";
}
function toStudents()
{
	document.location="students";
}
function toStats()
{
	document.location="statistics";
}
function toController()
{
	document.location="controller";
}
function toNotifications()
{
	document.location="notifications";
}
function toExit()
{
	alert("Выйти из профиля?");
	document.location="main";
}
function getJson_divs()
{
	var str = '{"divisions" : ["A", "B", "C"]}';
	return show_divisions(str); 
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_div_Json = xhr_d.responseText;
	// 		alert(get_div_Json)
	// 		// localStorage.setItem('divList', get_div_Json);
	// 		return show_divisions(get_div_Json);
	// 	}
	// }
	// xhr_d.open("POST", 'http://127.0.0.1:8000/divisionsRe?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(null);
}

function get_divs()
{
	var str = '{"divisions" : ["A", "B", "C"]}';
	return str; 
	// var xhr_d = new XMLHttpRequest();
	// alert("get_divs");

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_div_Json = xhr_d.responseText;
	// 		alert(get_div_Json)
	// 		// localStorage.setItem('divList', get_div_Json);
	// 		return get_div_Json;
	// 	}
	// }
	// xhr_d.open("POST", 'http://127.0.0.1:8000/divisionsRe?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(null);
}
 
function make_new_division(name)
{
	var xhr_d = new XMLHttpRequest();
	var params = "name=" + encodeURIComponent(name);

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			return (get_div_Json["status"])

		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/newDivisionRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);

}

function show_div_page(div)
{
	localStorage.setItem('divToShow', div);
	document.location="div_info?division=" + div;
}

function getJson_students_by_div()
{
	div = localStorage.getItem('divToShow')
	var xhr = new XMLHttpRequest();
	var params = 'name=' + encodeURIComponent(div);
	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_Json = xhr.responseText;
			// localStorage.setItem("divlist", get_div_Json)
			return show_div(get_Json);
		}
	}
	xhr.open("POST", 'http://127.0.0.1:8000/students_by_div?');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);
}

function make_info_element(nickname, lastname, name, secondname)
{
	let block = document.querySelectorAll(".block");
	let p = document.createElement("p");
	p.innerHTML = nickname + ": " + lastname + " " + name + " " + secondname;
	block[0].appendChild(p);
}

function show_div(students_list)
{
	let dv = document.querySelectorAll(".header_empty");
	let header = document.createElement("h1");
	var divName = localStorage.getItem('divToShow');
	header.innerHTML = "Дивизион " + divName;
	dv[0].appendChild(header);

	let block = document.querySelectorAll(".block");
	let h2_st = document.createElement("h2");
	h2_st.innerHTML = "Ученики";
	block[0].appendChild(h2_st);

	const students = JSON.parse(students_list);

	for (var i = 0; i <  students["students"].length; i++)
	{
		make_info_element(students["students"][i]["nickname"], students["students"][i]["surname"], students["students"][i]["name"], students["students"][i]["secondname"]);
	}
}

function add_division()
{
	let error = document.getElementById("errortext");
	error.setAttribute("hidden", "hidden");
	let name = document.querySelectorAll("#new_division_name input")[0].value;
	if (name == "")
	{
		error.innerHTML = "Введите имя дивизиона";
		error.removeAttribute("hidden");
	}
	else
	{
		if (make_new_division(name) == false)
		{
			error.innerHTML = "Такой дивизион уже существует";
			error.removeAttribute("hidden");
		}
		else
			document.location = "divisions";
	}
}

function show_divisions(div_json) 
{
	const divs = JSON.parse(div_json);

	let block = document.querySelectorAll(".block");

	for (var j = 0; j < divs["divisions"].length; j++)
	{
		let p = document.createElement("p");
		let a = document.createElement("a");
		a.innerHTML = divs["divisions"][j];
		a.setAttribute("class", "link");
		a.addEventListener('click', function(){
			show_div_page(a.innerHTML)});
		p.appendChild(a);
		block[0].appendChild(p);
	}
	
}

function new_division_field()
{
	let name = document.querySelectorAll("#new_division_name input")[0];
	let p = document.getElementById("new_division_name");
	console.log(name);
	p.removeAttribute("hidden");

	document.getElementById("newDivisionButton").setAttribute("hidden", "hidden");
	document.getElementById("addDivisionButton").removeAttribute("hidden");
}

