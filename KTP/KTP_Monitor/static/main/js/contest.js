function show()
{
	var paramValue = window.location.href.split("?")[1].split("&")[1].split("=")[1];
	document.querySelectorAll(".usual_header")[0].innerHTML = decodeURIComponent(paramValue);

	// var str = '{"problems":[{"name":"A"},{"name":"B"},{"name":"C"}],"pupils":[{"name":"Nikita","surname":"Anisimov","secondname":"Nikolayevich","nickname":"aaa","problems":[{"name":"A","status":"+2"},{"name":"B","status":"+"},{"name":"A","status":"-1"}]},{"name":"Dan","surname":"Roytburd","secondname":"Dmitrievich","nickname":"bbb","problems":[{"name":"A","status":"+"},{"name":"B","status":"0"},{"name":"A","status":"-"}]},{"name":"Natalya","surname":"Sobyanina","secondname":"Nikolayevna","nickname":"ccc","problems":[{"name":"A","status":"0"},{"name":"B","status":"+"},{"name":"A","status":"-"}]}]}';
	// return showStats(str);
	var params = "id=" + window.location.href.split("?")[1].split("&")[0].split("=")[1];
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_Json = xhr_d.responseText;
			showStats(get_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/contestStats?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}

function showStats(json_stats)
{
	var stats = JSON.parse(json_stats);
	console.log(stats);
	var table = document.querySelectorAll(".main-table")[0];

	var thead = document.createElement("thead");
	var tr = document.createElement("tr");
	var th = document.createElement("th");
	th.setAttribute("class", "fixed-side");
	th.setAttribute("scope", "col")

	tr.appendChild(th);

	for (var i = 0; i < stats["problems"].length; i++)
	{
		var cur_th = document.createElement("th");
		cur_th.setAttribute("class", "col");
		cur_th.innerHTML = stats["problems"][i]["name"];
		tr.appendChild(cur_th);
	}

	thead.appendChild(tr);
	table.appendChild(thead);

	var tbody = document.createElement("tbody");
	for (var i = 0; i < stats["pupils"].length; i++)
	{
		var cur_tr = document.createElement("tr");
		var cur_th = document.createElement("th");
		cur_th.setAttribute("class", "fixed-side");
		cur_th.innerHTML = stats["pupils"][i]["surname"] + " " + stats["pupils"][i]["name"] + " " + stats["pupils"][i]["secondname"];
		cur_tr.appendChild(cur_th);

		for (var j = 0; j < stats["pupils"][i]["problems"].length; j++)
		{
			console.log(j);
			var cur_td = document.createElement("td");
			cur_td.innerHTML = stats["pupils"][i]["problems"][j]["status"];
			cur_tr.appendChild(cur_td);
			console.log(cur_td.innerHTML);
		}
		tbody.appendChild(cur_tr);
	}
	table.appendChild(tbody);
	
}