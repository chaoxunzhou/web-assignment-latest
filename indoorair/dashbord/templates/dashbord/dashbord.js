function onPageLoadGetDashbordApi(){
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
         const dataString = this.responseText;
         const dataObj = JSON.parse(dataString);
         document.getElementById("avg_temperature").innerHTML= dataObj.avg_temperature;
         document.getElementById("avg_humidity").innerHTML= dataObj.avg_humidity;
         document.getElementById("avg_co2").innerHTML= dataObj.avg_co2;
         document.getElementById("avg_pressure").innerHTML= dataObj.avg_pressure;
         document.getElementById("avg_avg_TVOC").innerHTML= dataObj.avg_avg_TVOC;
   }
   xhttp.open("GET", "api/dashboard", true);
   // xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
   xhttp.send();
 }

 onPageLoadGetDashbordApi();
