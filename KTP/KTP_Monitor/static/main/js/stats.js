function show()
{
    // var str = '{"divisions":[{"name":"A","contests":[{"id":"1","name":"Дерево отрезков"},{"id":"2","name":"Динамика"},{"id":"3","name":"Графы"}],"pupils":[{"nickname":"aaa","name":"Никита","surname":"Анисимов","secondname":"Николаевич"},{"nickname":"ccc","name":"Дан","surname":"Ройтбурд","secondname":"Дмитриевич"}]},{"name":"B","contests":[{"id":"1","name":"Дерево отрезков"},{"id":"2","name":"Динамика"}],"pupils":[{"nickname":"aaa","name":"Никита","surname":"Анисимов","secondname":"Николаевич"},{"nickname":"bbb","name":"Наталья","surname":"Собянина","secondname":"Николаевна"},{"nickname":"ccc","name":"Дан","surname":"Ройтбурд","secondname":"Дмитриевич"}]}]}';
    // showInfo(str);
    var xhr_d = new XMLHttpRequest();

	xhr_d.onload = function(){
		if (xhr_d.status != 200){
			alert('Ошибка ${xhr.status} : ${xhr.statusText}');
		}
		else 
		{
			get_Json = xhr_d.responseText;
            console.log(get_Json);
			showInfo(get_Json);
		}
	}
	xhr_d.open("GET", 'http://127.0.0.1:8000/divs_full?', true);
	xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr_d.send(null);   
}

function showInfo(info)
{
    var table = document.querySelectorAll(".statsInfo")[0];
    var divs = JSON.parse(info)["divisions"];
    var tbody = document.createElement("tbody");

    for (var i = 0; i < divs.length; i++)
    {
        var tr = document.createElement("tr");
        // tr.setAttribute("id", divs[i]["name"]);
        tr.setAttribute("class", "divHeader");
        var td = document.createElement("td");
        td.setAttribute("colspan", "2");

        // var check = document.createElement("input");
        // check.setAttribute("type", "checkbox")
        // check.setAttribute("class", "checkbox");
        // check.setAttribute("id", divs[i]["name"]);
        // check.addEventListener("click", function(){
        //     clickDiv(this["id"], this.checked);
        // });
        var a = document.createElement("a");
        a.innerHTML = "Дивизион " + divs[i]["name"];
        // td.appendChild(check);
        td.appendChild(a);


        tr.appendChild(td);
        tbody.appendChild(tr);

        var j = 0;
        while(true)
        {
            if (j >= divs[i]["pupils"].length && j >= divs[i]["contests"].length)
            {
                break;
            }
            var tr = document.createElement("tr");
            var tdP = document.createElement("td");
            var tdC = document.createElement("td");


            if (j < divs[i]["pupils"].length)
            {
                var p = document.createElement("p");
                p.setAttribute("name", "pupil");
                var check = document.createElement("input");
                check.setAttribute("type", "checkbox");
                check.setAttribute("class", "checkbox");
                check.addEventListener('click', function(){
                    checkBt(this);
                });
                var a = document.createElement("a");
                a.innerHTML = divs[i]["pupils"][j]["surname"] + " " + divs[i]["pupils"][j]["name"] + " " + divs[i]["pupils"][j]["secondname"];
                a.setAttribute("name", divs[i]["pupils"][j]["nickname"]);
                a.setAttribute("class", "link");

                p.appendChild(check);
                p.appendChild(a);
                tdP.setAttribute("class", divs[i]["name"]);

                tdP.appendChild(p);
            }
            else{
                tdP.setAttribute("class", "empty");
            }

            if (j < divs[i]["contests"].length)
            {
                var p1 = document.createElement("p");
                p1.setAttribute("name", "contest");
                var check1 = document.createElement("input");
                check1.setAttribute("class", "checkbox");
                check1.setAttribute("type", "checkbox");
                var a1 = document.createElement("a");
                check1.addEventListener('click', function(){
                    checkBt(this);
                });
                a1.innerHTML = divs[i]["contests"][j]["name"];
                a1.setAttribute("name", divs[i]["contests"][j]["id"]);
                a1.setAttribute("class", "link");

    
                p1.appendChild(check1);
                p1.appendChild(a1);

                tdC.setAttribute("class", divs[i]["name"]);


                tdC.appendChild(p1);
            }
            else
            {
                tdC.setAttribute("class", "empty");
            }

            tr.appendChild(tdP);
            tr.appendChild(tdC);

            tbody.appendChild(tr);     
            j++;       
        }
    }
    table.appendChild(tbody);

    bt = document.createElement("button");
    bt.innerHTML = "Показать";

    bt.setAttribute("class", "usual_button");
    bt.setAttribute("onclick", "getStats()");

    document.querySelectorAll(".block")[0].appendChild(bt);
}

function clickDiv(div, status)
{
    // var td = document.querySelectorAll("." + div);
    var checkers = document.querySelectorAll("." + div + " input");
    for (var i = 0; i < checkers.length; i++)
    {
        // alert("1");
        alert(checkers[i].checked);
        if (status)
        {
            checkers[i].removeAttribute("checked");
            checkers[i].setAttribute("checked", true);
        }
        else
        {
            checkers[i].removeAttribute("checked");
            // checkers[i].setAttribute("checked", false);
        }

    }
}

function checkBt(bt)
{
    // alert(bt.checked);
    if (bt.checked)
    {
        bt.removeAttribute("checked");
        bt.setAttribute("checked", true);
    }
    else
    {
        bt.removeAttribute("checked");
    }
}

function getStats()
{
    alert("fgb");
    var params = "";
    var el = document.querySelectorAll("td p");
    var pupil_cnt = 0;
    var contest_cnt = 0;
    for (var i = 0; i < el.length; i++)
    {
        var status = el[i].querySelectorAll("input")[0];
            if (!status.checked)
                continue;
        console.log(el[i]);
        if (el[i].getAttribute("name") == "pupil")
        {
            console.log("fgbgfb");
            var a = el[i].querySelectorAll("a")[0];
            console.log(a);
            pupil_cnt = pupil_cnt + 1;
            if (params == "")
                params = "pupil1=" + encodeURIComponent(a.getAttribute("name"));
            else
                params = params + "&pupil" + pupil_cnt + "=" + encodeURIComponent(a.getAttribute("name")); 
        }
        if (el[i].getAttribute("name") == "contest")
        {
            contest_cnt = contest_cnt + 1;
            var a = el[i].querySelectorAll("a")[0];
            console.log(a);

            if (params == "")
                params = "contest1=" + encodeURIComponent(a.getAttribute("name"));
            else
                params = params + "&contest" + contest_cnt + "=" + encodeURIComponent(a.getAttribute("name")); 
        }
    }
    if (pupil_cnt < 1 || contest_cnt < 1)
    {
        return;
    }

    

    // var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_Json = xhr_d.responseText;
	// 		showStats(get_Json);
	// 	}
	// }
	// xhr_d.open("POST", 'http://127.0.0.1:8000/fullStats?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(params);  
}

function fullStats(json_stats)
{
    var stats = JSON.parse(json_stats)["stat"];
	var table = document.querySelectorAll(".main-table")[0];

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
		var cur_th = document.createElement("th");
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