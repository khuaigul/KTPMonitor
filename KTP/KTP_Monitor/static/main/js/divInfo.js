function setName()
{
	var paramValue = window.location.href.split("?")[1].split("=")[1];
	document.querySelectorAll(".name_header")[0].innerHTML = "Дивизион " + paramValue;
}

function getTeachers()
{
	var div = window.location.href.split("?")[1].split("=")[1];		
	var params = "name=" + div;
	var xhr_d = new XMLHttpRequest();
	
	xhr_d.open("POST", 'http://127.0.0.1:8000/teachers_by_div?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_teachers_Json = xhr_d.responseText;
			showTeachers(get_teachers_Json);
		}
	}
}

function showTeachers(teachers_json)
{
	teachers = JSON.parse(teachers_json);
	// console.log(teachers["teachers"]);

	var title = document.createElement("p");
	title.innerHTML = "Преподаватели:"
	document.getElementById("teachers").appendChild(title);

	for (var i = 0; i < teachers["teachers"].length; i++)
	{
		var p = document.createElement("p");
		p.innerHTML = teachers["teachers"][i]["name"];
		document.getElementById("teachers").appendChild(p);
	}

}

function getStudents()
{	
	var div = window.location.href.split("?")[1].split("=")[1];
	alert(div);
	var params = "name=" + div;  
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_students_Json = xhr_d.responseText;
			showStudents(get_students_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/students_by_div?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}

function getContests()
{
//	var str = '{"contests" : [{"name" : "Динамика", "id" : "4345"}, {"name" : "Дерево отрезков", "id" : "76543"}] }'
//	return showContests(str);
	var div = window.location.href.split("?")[1].split("=")[1];
	var params = "div=" + div;
	var xhr_d = new XMLHttpRequest();

	console.log(params);
	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert(xhr.status + " " + xhr.statusText);
		}
		else
		{
			get_div_Json = xhr_d.responseText;
			alert(get_div_Json);
			showContests(get_div_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/contestsList?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}

function showStudents(students_json)
{
	console.log("showww");
	console.log(students_json)
	var title = document.createElement("div");
	var p = document.createElement("p");
	p.innerHTML = "Ученики";
	// title.appendChild(p);

	title.setAttribute("class", "listTitle");

	document.getElementById("students").appendChild(title);

	console.log(document.getElementById("students"));


	document.querySelectorAll(".listTitle")[0].appendChild(p);
	// console.log(document.querySelectorAll(".listTitle"));


	students = JSON.parse(students_json)["pupils"];

	// console.log(students);

	for (var i = 0; i < students.length; i++)
	{
		var cur = document.createElement("p");
		var a = document.createElement("a");
		a.innerHTML = students[i]["surname"] + " " + students[i]["name"] + " " + students[i]["secondname"];
		a.setAttribute("class", "link");
		a.setAttribute("name", students[i]["nickname"])
		a.addEventListener('click', function(){
			showStudent(this.getAttribute("name"))});
		cur.appendChild(a);
		document.getElementById("students").appendChild(cur);
	}

}

function showContests(contests_json)
{
	var title = document.createElement("div");
	var p = document.createElement("p");
	p.innerHTML = "Контесты";
	// title.appendChild(p);

	title.setAttribute("class", "listTitle");

	document.getElementById("contests").appendChild(title);
	console.log(document.getElementById("contests"));
	console.log(document.querySelectorAll(".listTitle"));
	document.querySelectorAll(".listTitle")[0].appendChild(p);


	contests = JSON.parse(contests_json)["contests"];

	for (var i = 0; i < contests.length; i++)
	{
		var cur = document.createElement("p");
		var a = document.createElement("a");

		a.innerHTML = contests[i]["name"];
		a.setAttribute("class", "link");
		a.setAttribute("name", contests[i]["id"]);
		a.addEventListener('click', function(){
			showContest(this.getAttribute("name"));
		})

		cur.appendChild(a);
		document.getElementById("contests").appendChild(cur);
	}

}

function showStudent(student)
{
	document.location="pupil?nickname=" + student;
}

function showContest(contest)
{
	document.location="contest?id=" + contest;
}

function deleteDivision()
{
	var div = window.location.href.split("?")[1].split("=")[1];
	if (confirm("Вы действительно хотите удалить дивизион " + div + "?"))
	{
		var params = "division=" + div;  
		var xhr_d = new XMLHttpRequest();
		xhr_d.open("POST", 'http://127.0.0.1:8000/deleteDivision?', true);
		xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr_d.send(params);
		xhr_d.onload = function(){
			if (xhr_d.status != 200){
				alert('Ошибка ${xhr.status} : ${xhr.statusText}');
			}
			else 
			{
				alert("back");	
				document.location = "divisions";
			}
		}		
	}
}

function showStats()
{
	var div = window.location.href.split("?")[1].split("=")[1];
	window.location = "division_stats?division=" + div;
}