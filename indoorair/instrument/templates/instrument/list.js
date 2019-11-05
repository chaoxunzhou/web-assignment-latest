function onPageLoadGetInstrumentsListApi(){
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
         const dataString = this.responseText;
         const dataObj = JSON.parse(dataString);

         const instrumentArray = dataObj.instruments;
         text = "";
         for(instrumentObj of instrumentArray){
          text += "<li>" + instrumentObj.name + "</li>"
         }

         var element = document.getElementById("instrument_list")
         element.innerHTML = text;

   }
   xhttp.open("POST", "api/instruments", true);
   // xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
   xhttp.send();
 }

 onPageLoadGetInstrumentsListApi();
