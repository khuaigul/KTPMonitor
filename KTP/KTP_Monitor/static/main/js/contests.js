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
	// var str = '{"divisions" : ["A", "B", "C"]}';
	// return show_divisions(str); 
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			alert(get_div_Json)
			// localStorage.setItem('divList', get_div_Json);
			return show_divisions(get_div_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divisionsRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function show_divisions(divisions)
{
	const divs = JSON.parse(divisions);
	for (var i = 0; i < divs["divisions"].length; i++)
	{
		let block = document.createElement("div");
		block.setAttribute("name", divs["divisions"][i]);
		let p = document.createElement("p");
		let bt = document.createElement("button");
		bt.setAttribute("class", "microButton");
		bt.setAttribute("onclick", "showContests(this)");
		bt.setAttribute("name", divs["divisions"][i]);
		let img = document.createElement("img");
		img.setAttribute("name", "plus");
		img.setAttribute("src", "/static/main/images/plus.png");
		bt.appendChild(img);
		let a = document.createElement("a");
		a.innerHTML = divs["divisions"][i];
		p.appendChild(bt);
		p.appendChild(a);
		block.appendChild(p);
		console.log(document.querySelectorAll(".block")[0]);
		document.querySelectorAll(".block")[0].appendChild(block);
	}
}

function showContests(sender)
{
	let blocks = document.querySelectorAll(".block div");
	for (var i = 0; i < blocks.length; i++)
	{
		if (blocks[i].querySelectorAll("button")[0]["name"] != sender["name"])
			continue;
		console.log(blocks[i]);
		let img = blocks[i].querySelectorAll("img")[0];
		img["src"] = "/static/main/images/minus.png";

		let name = sender["name"];

		if (img["name"] == "plus")
		{
			img.setAttribute("name", "minus");
			get_contests(name, blocks[i]);
		}
		else
		{
			var el = blocks[i].querySelectorAll(".contestLink");
			for (var i = 0; i < el.length; i++)
				el[i].remove();
			img.setAttribute("name", "plus");
			img["src"] = "/static/main/images/plus.png";
		}
		
	}
}

function get_contests(name, block)
{
	var str = '{"contests" : [{"name" : "Дерево отрезков", "id" : "1234"}, {"name" : "Геометрия", "id" : "2354"}, {"name" : "Графы", "id" : "7544"}]}';
	return show_contests(str, block); 

	// var params = 'division=' + encodeURIComponent(name);
	// var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_Json = xhr_d.responseText;
	// 		return show_contests(get_Json, block);
	// 	}
	// }
	// xhr_d.open("GET", 'http://127.0.0.1:8000/contestsList?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);
}

function show_contests(contests_json, block)
{
	contests = JSON.parse(contests_json);
	for (var i = 0; i < contests["contests"].length; i++)
	{
		var p = document.createElement("p");
		var a = document.createElement("a");
		p.setAttribute("class", "contestLink");
		p.setAttribute("name", contests["contests"][i]);
		a.innerHTML = contests["contests"][i]["name"];
		a.setAttribute("name", contests["contests"][i]["id"]);
		a.setAttribute("onclick", "show_contest(this)");
		p.appendChild(a);
		block.appendChild(p);
	}
}

function show_contest(sender)
{
	document.location="contest?id=" + '[' + sender.name + ', fgf]';
}

function addContest()
{
	document.location="addContest";
}

function divCheckBox()
{
	var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_div_Json = xhr_d.responseText;
			return showDivisionsCheckBox(get_div_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divisionsRe?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);
}

function showDivisionsCheckBox(json_divisions)
{
	var divs = JSON.parse(json_divisions)["divisions"];
	for (var i = 0; i < divs.length; i++)
	{
		var p = document.createElement("p");
		p.setAttribute("class", "data");
		var input = document.createElement("input");
		input.setAttribute("type", "checkbox");
		input.setAttribute("class", "movedCheckbox");
		input.setAttribute("name", divs[i]);
		var text = document.createElement("a");
		text.innerHTML = divs[i];
		p.appendChild(input);
		p.appendChild(text);
		document.querySelectorAll(".block")[0].appendChild(p);
		// document.querySelectorAll(".block")[0].appendChild(text);

	}

	var all = document.getElementById("allDivisions");
	all.addEventListener('change', (event) => {
  		if (event.currentTarget.checked) {
    		var el = document.querySelectorAll(".movedCheckbox");
    		for (var i = 0; i < el.length; i++)
    		{
    			el[i].checked = true;
    		}
  		} 
  		else {
    		var el = document.querySelectorAll(".movedCheckbox");
    		for (var i = 0; i < el.length; i++)
    		{
    			el[i].checked = false;
    		}
  		}
	})
}

function addNewContest()
{
	var link = document.getElementById("link").value;
	var name = document.getElementById("name").value;

	var divs = document.querySelectorAll(".movedCheckbox");
	for (var i = 0; i < divs.length; i++)
	{
		if (divs[i].checked == false)
			continue;
		var params = "link=" + encodeURIComponent(link) + "&name=" + encodeURIComponent(name) + "&division=" + encodeURIComponent(divs[i]["name"]); 
		console.log(params);
		// var xhr_d = new XMLHttpRequest();

		// xhr_d.onload = function(){
		// 	if (xhr_d.status != 200){
		// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		// 	}
		// 	else 
		// 	{
		// 		get_div_Json = xhr_d.responseText;
		// 	}
		// }
		// xhr_d.open("GET", 'http://127.0.0.1:8000/newContest?', true);
		// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		// xhr_d.send(params);
	}
}