function show_student_page(nickname)
{
	localStorage.setItem('nicknameToShow', nickname);
	console.log(nickname);
	document.location="student_profile";
}

function getJson_profile(nickname)
{
	var profile_info = '{"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "A", "datebirth" : "12.05.2005", "school" : "Школа № 99", "form" : 10, "lastActivity" : "2 days ago"}';
	return profile_info;
}

function make_info_element(value, position)
{
	let block = document.querySelectorAll(".block");
	let p = document.createElement("p");
	p.innerHTML = position + ": " + value;
	block[0].appendChild(p);
}

function show_student()
{
	console.log("show");
	let dv = document.querySelectorAll(".header_empty");
	let header = document.createElement("h1");
	var nickName = localStorage.getItem('nicknameToShow');
	header.innerHTML = "Профиль школьника: " + nickName;
	dv[0].appendChild(header);

	const student_info = getJson_profile(nickName);
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

function save_division_update()
{

}

function show_students_list()
{
	const students_list = '{"students" : [	{"nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "div" : "не выбрано"},{"nickname" : "qwer","surname" : "Петров", "name" : "Пётр", "secondname" : "Петрович", "div" : "A"},{"nickname" : "wertyui","surname" : "Смирнов", "name" : "Валерий", "secondname" : "Михайлович", "div" : "B"},	{"nickname" : "aaaanbvc","surname" : "Иванова", "name" : "Мария", "secondname" : "Ивановна", "div" : "A"},{"nickname" : "elele","surname" : "Крылова", "name" : "Анна", "secondname" : "Александровна", "div" : "не выбрано"}]}';
	const div_list = '{"divisions" : ["A", "B", "C", "не выбрано"]}';
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
		par.appendChild(div_change);
		let dv = document.querySelectorAll("#students_list");
		dv[0].appendChild(par);
//		document.body.appendChild(dv[0]);
	}

//	console.log(obj["students"][0]);
}