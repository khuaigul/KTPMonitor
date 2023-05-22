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
		p.innerHTML = teachers["teachers"][i]["surname"] + " " + teachers["teachers"][i]["name"] + " " + teachers["teachers"][i]["secondname"];
		document.getElementById("teachers").appendChild(p);
	}

}

function getStats()
{
	var div = window.location.href.split("?")[1].split("=")[1];
	// var str = '{"stat" : {"pupils" : [{"nickname" : "aaa", "name" : "Nikita", "surname" : "Anisimov", "secondname" : "Nikolayevich", "results" : [{"id" : "123", "solved" : "6"}, {"id" : "321", "solved" : "5"}]}, {"nickname" : "bbb", "name" : "Natalya", "surname" : "Sobyanina", "secondname" : "Nikolayevna", "results" : [{"id" : "123", "solved" : "4"}, {"id" : "321", "solved" : "2"}]}], "contests" : [{"name" : "DO", "id" : "123", "count" : "10"}, {"name" : "DP", "id" : "321", "count" : "10"}]}}';
	// return showStats(str);
	var params = "name=" + div;
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			var get_Json = xhr_d.responseText;
			console.log(get_Json);
			showStats(get_Json);
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/divisionStats?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}

function showStats(stats_json)
{
	var stats = JSON.parse(stats_json)["stat"];
	var table = document.querySelectorAll("table")[0];

	var thead = document.createElement("thead");
	var tr = document.createElement("tr");
	var th = document.createElement("th");
	th.setAttribute("class", "fixed-side");
	th.setAttribute("scope", "col")

	tr.appendChild(th);
	console.log('dfrg');
	console.log(stats);
	for (var i = 0; i < stats["contest"].length; i++)
	{
		var cur_th = document.createElement("th");
		cur_th.setAttribute("class", "col");
		cur_th.innerHTML = stats["contest"][i]["name"];
		tr.appendChild(cur_th);
	}
	thead.appendChild(tr);
	table.appendChild(thead);

	var tbody = document.createElement("tbody");
	for (var i = 0; i < stats["pupils"].length; i++)
	{
		var cur_tr = document.createElement("tr");
		var cur_th = document.createElement("td");
		cur_th.setAttribute("class", "fixed-side");
		cur_th.innerHTML = stats["pupils"][i]["surname"] + " " + stats["pupils"][i]["name"] + " " + stats["pupils"][i]["secondname"];
		cur_tr.appendChild(cur_th);

		for (var j = 0; j < stats["pupils"][i]["results"].length; j++)
		{
			console.log(j);
			var cur_td = document.createElement("td");
			cur_td.innerHTML = stats["pupils"][i]["results"][j]["solved"] + "/" + stats["contest"][j]["count"];
			cur_tr.appendChild(cur_td);
			console.log(cur_td.innerHTML);
		}
		tbody.appendChild(cur_tr);
	}
	table.appendChild(tbody);
}