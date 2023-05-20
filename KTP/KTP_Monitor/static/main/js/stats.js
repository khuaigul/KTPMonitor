function show()
{
    var str = '{"divisions":[{"name":"A","contests":[{"id":"1","name":"Дерево отрезков"},{"id":"2","name":"Динамика"},{"id":"3","name":"Графы"}],"pupils":[{"nickname":"aaa","name":"Никита","surname":"Анисимов","secondname":"Николаевич"},{"nickname":"ccc","name":"Дан","surname":"Ройтбурд","secondname":"Дмитриевич"}]},{"name":"B","contests":[{"id":"1","name":"Дерево отрезков"},{"id":"2","name":"Динамика"}],"pupils":[{"nickname":"aaa","name":"Никита","surname":"Анисимов","secondname":"Николаевич"},{"nickname":"bbb","name":"Наталья","surname":"Собянина","secondname":"Николаевна"},{"nickname":"ccc","name":"Дан","surname":"Ройтбурд","secondname":"Дмитриевич"}]}]}';
    showInfo(str);
    // var xhr_d = new XMLHttpRequest();

	// xhr_d.onload = function(){
	// 	if (xhr_d.status != 200){
	// 		alert('Ошибка ${xhr.status} : ${xhr.statusText}');
	// 	}
	// 	else 
	// 	{
	// 		get_Json = xhr_d.responseText;
	// 		showInfo(get_Json);
	// 	}
	// }
	// xhr_d.open("POST", 'http://127.0.0.1:8000/divs_full?', true);
	// xhr_d.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	// xhr_d.send(null);   
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
                var check = document.createElement("input");
                check.setAttribute("type", "checkbox");
                check.setAttribute("class", "checkbox");
                check.addEventListener('click', function(){
                    checkBt(this);
                });
                var a = document.createElement("a");
                a.innerHTML = divs[i]["pupils"][j]["surname"] + " " + divs[i]["pupils"][j]["name"] + " " + divs[i]["pupils"][j]["secondname"];

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
                var check1 = document.createElement("input");
                check1.setAttribute("class", "checkbox");
                check1.setAttribute("type", "checkbox");
                var a1 = document.createElement("a");
                check1.addEventListener('click', function(){
                    checkBt(this);
                });
                a1.innerHTML = divs[i]["contests"][j]["name"];
    
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
    alert(bt.checked);
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