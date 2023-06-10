function rotateNeedle(angle, duration) {
	var needleElement = document.querySelector("#needleResponse .needle");
	needleElement.style.transition = "transform " + duration + "s ease-in-out";
	needleElement.style.transform = "rotate(" + angle + "deg)";
  }
  
  function gelenDegeriGuncelle() {
	var gelenDegerInput = document.querySelector("#gelenDegerInput");
	var gelenDeger = parseFloat(gelenDegerInput.value);
  
	if (!isNaN(gelenDeger)) {
	  rotateNeedle(gelenDeger, 5); // 5 saniyede dönme animasyonu
	}
  }
  



  var xValues = ["Olumlu", "Nötr", "Olumsuz"];
  var yValues = [33,33,33];
  var barColors = [
	"#4EB302",
	"#F9B305",
	"#EE5827",
  ];
  new Chart("myChart", {
	type: "pie",
	data: {
	  labels: xValues,
	  datasets: [{
		backgroundColor: barColors,
		data: yValues
	  }]
	},
	options: {
	  title: {
		display: true,
		text: "Pie Chart"
	  }
	}
  });