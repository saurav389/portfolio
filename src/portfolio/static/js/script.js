const tempload = () => {
	let logo  = document.getElementById('lgo');
	logo.innerHTML  = "&#xf110";
	logo.style.color = "white";
	var path = window.location.pathname;
	console.log(path);
	if(path == '/'){
		var nav = document.getElementById('services');
		nav.style.display = 'block';

	}

}
tempload();

