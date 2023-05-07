function show()
{
	var paramValue = window.location.href.split("?")[1].split("&")[1].split("=")[1];
	document.querySelectorAll(".usual_header")[0].innerHTML = paramValue;

	
}