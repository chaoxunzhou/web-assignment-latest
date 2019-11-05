function onLoginClick() {
    window.location.href = "/login";
}

function onRegisterClick() {
    window.location.href = "/register";
}


function onContactClick() {
    window.location.href = "/contact";
}

function onVersionClick(){
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
         const dataString = this.responseText;
         const dataDict = JSON.parse(dataString);

         var element = document.getElementById("version");
         element.innerHTML = dataDict.version;
   }
   xhttp.open("GET", "api/version", true);
   // xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
   xhttp.send();
 }
}
