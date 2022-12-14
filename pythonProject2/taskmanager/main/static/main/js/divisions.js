function getJson_divs()
{
	const str = '{"divisions" : ["A", "B", "C"]}';
	return str;
}

function make_new_division(name)
{
	console.log(name);
}

function show_div_page(div)
{
	localStorage.setItem('divToShow', div);
	document.location="div_info";
}

function getJson_students_by_div(div)
{
	const students_list = '{"students" : [	{"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "не выбрано"},{"nickname" : "qwer","surname" : "Петров", "name" : "Пётр", "secondname" : "Петрович", "div" : "A"},{"nickname" : "wertyui","surname" : "Смирнов", "name" : "Валерий", "secondname" : "Михайлович", "div" : "B"},	{"nickname" : "aaaanbvc","surname" : "Иванова", "name" : "Мария", "secondname" : "Ивановна", "div" : "A"},{"nickname" : "elele","surname" : "Крылова", "name" : "Анна", "secondname" : "Александровна", "div" : "не выбрано"}]}';
	return students_list;
}

function make_info_element(nickname, lastname, name, secondname)
{
	let block = document.querySelectorAll(".block");
	let p = document.createElement("p");
	p.innerHTML = nickname + ": " + lastname + " " + name + " " + secondname;
	block[0].appendChild(p);
}

function show_div()
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

	const students_list = getJson_students_by_div(divName);
	const students = JSON.parse(students_list);

	for (var i = 0; i <  students["students"].length; i++)
	{
		make_info_element(students["students"][i]["nickname"], students["students"][i]["lastname"], students["students"][i]["name"], students["students"][i]["secondname"]);
	}


}

function add_division()
{
	let block = document.querySelectorAll(".block");
	if (document.getElementById("errortext") != null)
		block[0].removeChild(document.getElementById("errortext"));
	let name = document.querySelectorAll("#name > input");
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
		document.location='divisions';
	}
}

function show_divisions() 
{
	const div_json = getJson_divs();
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