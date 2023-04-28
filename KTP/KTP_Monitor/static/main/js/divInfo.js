function setName()
{
	var paramValue = window.location.href.split("?")[1].split("=")[1];
	document.querySelectorAll(".name_header")[0].innerHTML = "Дивизион " + paramValue;
}

function getTeachers()
{
	var div = window.location.href.split("?")[1].split("=")[1];
	var str = '{"teachers" : [{"name": "Собянина Наталья Николаевна"}, {"name" : "Анисимов Никита Николаевич"}]}';
	return showTeachers(str); 
	var params = "name=" + div;
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_teachers_Json = xhr_d.responseText;
	// 		showTeachers(get_teachers_Json);
	// 	}
	// }
	// xhr_d.open("GET", 'http://127.0.0.1:8000/teachers_by_div?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);
}

function showTeachers(teachers_json)
{
	teachers = JSON.parse(teachers_json);
	console.log(teachers["teachers"]);

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
	var str = '{"students" : [{"name": "Дан", "secondname" : "Дмитриевич", "surname" : "Ройтбурд", "nickname" : "ccc"}, {"name": "Айгуль", "secondname" : "Рустемовна", "surname" : "Хуснутдинова", "nickname" : "bbb"}, {"name": "Никита", "secondname" : "Николаевич", "surname" : "Анисимов", "nickname" : "aa"}]}';
	return showStudents(str);
	var div = window.location.href.split("?")[1].split("=")[1];
	var params = "name=" + div;  
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_students_Json = xhr_d.responseText;
	// 		showTeachers(get_students_Json);
	// 	}
	// }
	// xhr_d.open("GET", 'http://127.0.0.1:8000/students_by_div?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);
}

function getContests()
{

}

function showStudents(students_json)
{
	var title = document.createElement("div");
	var p = document.createElement("p");
	p.innerHTML = "Ученики";
	// title.appendChild(p);

	title.setAttribute("class", "listTitle");

	document.getElementById("students").appendChild(title);

	document.querySelectorAll(".listTitle")[0].appendChild(p);
	console.log(document.querySelectorAll(".listTitle")[0]);


	students = JSON.parse(students_json)["students"];

	console.log(students);

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

function showStudent(student)
{
	document.location="pupil?nickname=" + student;
}