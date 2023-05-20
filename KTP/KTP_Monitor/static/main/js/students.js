function showPupilHeader()
{
	var nickname = window.location.href.split('?')[1].split('=')[1];
	
}

function getJson_profile()
{
	// var profile_info = '{"email" : "a@a", "nickname" : "abcd", "surname" : "Иванов", "name" : "Иван", "secondname" : "Иванович", "division" : "A", "datebirth" : "12.05.2005", "school" : "Школа № 99", "grade" : 10, "phone" : "89212222222"}';
	var nickname = window.location.href.split('?')[1].split('=')[1];
	var params = 'nickname=' + encodeURIComponent(nickname);
	// return showStudent(profile_info);
	var xhr = new XMLHttpRequest();
	xhr.onload = function(){
		if (xhr.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		} 
		else
		{
			// alert(xhr.responseText);
			showStudent(xhr.responseText);
		}
	}
	xhr.open("POST", 'http://127.0.0.1:8000/pupilInfo?', true);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send(params);
}

function showStudent(pupil_json)
{
	var pupil = JSON.parse(pupil_json);
	document.querySelectorAll("h1")[0].innerHTML = pupil["surname"] + " " + pupil["name"] + " " + pupil["secondname"];
	make_info_element(pupil, "email");
	make_info_element(pupil, "phone");
	make_info_element(pupil, "datebirth");
	make_info_element(pupil, "school");
	make_info_element(pupil, "grade");
	make_info_element(pupil, "division");
}

function make_info_element(pupil, value)
{
	document.getElementById(value).innerHTML += pupil[value];
}



function show_student(student_info)
{
	document.location="student_profile?nickname=" + encodeURIComponent(student_info);
	
}


function show()
{
	//alert("show");
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			console.log(get_div_Json);
			showPupils(get_div_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divs_with_pupil?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showPupils(json_divs)
{
	var inf = JSON.parse(json_divs)["divisions"];
	console.log(inf);
	var divlist = [];
	for (var i = 0; i < inf.length; i++)
	{
		divlist.push(inf[i]["name"]);
	}
	for (var i = 0; i < inf.length; i++)
	{
		var div = document.createElement("p");
		div.innerHTML = "Дивизион " + inf[i]["name"];
		var pupils = inf[i]["pupils"];
	//	alert(div);
	//	alert(pupils);

		document.querySelectorAll(".block")[0].appendChild(div);

		for (var j = 0; j < pupils.length; j++)
		{
			var div1 = document.createElement("div");
			div1.setAttribute("class", "pupil");

			var p = document.createElement("p");
			var a = document.createElement("a");
			a.setAttribute("class", "link");
			a.setAttribute("name", pupils[j]["nickname"]);
			a.addEventListener('click', function(){
				show_student(this.getAttribute("name"))});
			a.innerHTML = pupils[j]["surname"] + " " + pupils[j]["name"] + " " + pupils[j]["secondname"];
			var sel = document.createElement("select");
			sel.setAttribute("name", inf[i]["name"]);

			for (var q = 0; q < divlist.length; q++)
			{
				var opt = document.createElement("option");
				opt.setAttribute("value", divlist[q]);
				opt.innerHTML = divlist[q];
				if (divlist[q] == inf[i]["name"])
					opt.setAttribute("selected", "selected");
				sel.appendChild(opt);
			}

			p.appendChild(a);
			div1.appendChild(p);
			div1.appendChild(sel);

			document.querySelectorAll(".block")[0].appendChild(div1);
		}
	}
}




function save_changes()
{
	var params = "";
	var cnt = 0;
	var pupils = document.querySelectorAll(".pupil");
	for (var i = 0; i < pupils.length; i++)
	{
		var sel = pupils[i].querySelectorAll("select")[0];
		var a = pupils[i].querySelectorAll("a")[0];

		var nickname = a.getAttribute("name");
		var oldDiv = sel.getAttribute("name");

		var newDiv = sel.value;

		if (oldDiv != newDiv)
		{
			console.log(nickname);
			console.log(newDiv);
			console.log(oldDiv);

			cnt = cnt + 1;
			if (cnt == 1)
			{
				params = "pupil1=" + encodeURIComponent(nickname) + "&division1=" + encodeURIComponent(newDiv);
			}
			else
			{
				params = params + "&pupil" + cnt + "=" + encodeURIComponent(nickname) + "&division" + cnt + "=" + encodeURIComponent(newDiv);
			}
		}
	}

	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			document.location="students";
		}
	}
	xhr_d.open("POST", 'http://127.0.0.1:8000/updatePupilDivison?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(params);
}

function toShowPupilStat()
{
	var nickname = window.location.href.split('?')[1].split('=')[1];
	document.location="studentStatsPage?nickname=" + encodeURIComponent(nickname);
}

function showPupilStats()
{
	var nickname = window.location.href.split('?')[1].split('=')[1];
	var params = "nickname=" + encodeURIComponent(nickname);
	var str = '{"stats" : [{"name" : "Дерево отрезков", "solved" : "6", "count" : "10"}, {"name" : "Графы", "solved" : "4", "count" : "12"}]}';
	showStats(str);
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		var get_json = xhr_d.responseText;
	// 		console.log(get_json);
	// 		showStats(get_json);
	// 	}
	// }
	// xhr_d.open("POST", 'http://127.0.0.1:8000/pupilStats?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);
}

function showStats(json_stats)
{
	var stats = JSON.parse(json_stats)["stats"];
	var table = document.querySelectorAll("table")[0];

	console.log(stats);

	var thead = document.createElement("thead");

	var tr = document.createElement("tr");
	var th1 = document.createElement("th");
	var th2 = document.createElement("th");

	th1.innerHTML = 'Контесты';
	th2.innerHTML = 'Решено';

	tr.appendChild(th1);
	tr.appendChild(th2);
	table.appendChild(thead);


	thead.appendChild(tr);

	var tbody = document.createElement("tbody");

	for (var i = 0; i < stats.length; i++)
	{
		var tr_cur = document.createElement("tr");
		var tdC = document.createElement("td");
		var tdP = document.createElement("td");

		var a = document.createElement("a");
		a.innerHTML = stats[i]["name"];
		a.addEventListener("click", function(){
			document.location("contest?id=" + encodeURIComponent(stats[i]["id"] + "&name=" + encodeURIComponent(stats[i]["name"])));
		});
		tdC.appendChild(a);
		tdP.innerHTML = stats[i]["solved"] + "/" + stats[i]["count"];

		tr_cur.appendChild(tdC);
		tr_cur.appendChild(tdP);

		tbody.appendChild(tr_cur);
	}
	table.appendChild(tbody);
}