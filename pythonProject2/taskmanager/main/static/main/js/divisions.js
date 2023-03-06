function getJson_divs()
{
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			localStorage.setItem('divList', get_div_Json);
			return show_divisions(get_div_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/divisionsRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
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
			document.location='divisions';
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/newDivisionRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);

}

function show_div_page(div)
{
	localStorage.setItem('divToShow', div);
	document.location="div_info";
}

function getJson_students_by_div()
{
	div = localStorage.getItem('divToShow')
	var xhr = new XMLHttpRequest();
	var params = 'div=' + encodeURIComponent(div);
	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_Json = xhr.responseText;
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
	// alert("add division");
	let block = document.querySelectorAll(".block");
	if (document.getElementById("errortext") != null)
		block[0].removeChild(document.getElementById("errortext"));
	let name = document.querySelectorAll("#name > input");
	var divs_list = localStorage.getItem("divList");
	var divs = JSON.parse(divs_list);
	var newName = name[0].value;
	if (name[0].value == "")
	{
		let text = document.createElement("p");
		text.innerHTML = "Заполните поле";
		text.setAttribute("id", "errortext")
		text.setAttribute("class", "note")
		block[0].appendChild(text);
	} 
	else
	{
		make_new_division(name[0].value);
	}
}

function show_divisions(div_json) 
{
	const divs = JSON.parse(div_json);

	let block = document.querySelectorAll(".block");

	for (var j = 0; j < divs["divisions"].length; j++)
	{
		let p = document.createElement("p");
		p.innerHTML = divs["divisions"][j];
		p.setAttribute("class", "link");
		p.addEventListener('click', function(){
			show_div_page(p.innerHTML)});
		block[0].appendChild(p);
	}
}