function onLoginClick(){
  const usernameElement = document.getElementById("username")
  const username = usernameElement.value;
  console.log(username);
  const passwordElement = document.getElementById("password")
  const password = passwordElement.value;
  console.log(password);

var xhttp = new XMLHttpRequest();
xhttp.onreadstatechange = function(){
  if (this.readyState == 4 && this.status == 200){
    const resultString = this.responseText;
    var resultObject = JSON.parse(resultString);
    //  was_successful is key that we set in dictionary from wiews.py
    if(resultObject.was_logged === false){
      console.log(resultObject.reason);
    }else{
      window.location.href = "/dashbord";
    }
  }
}
xhttp.open("POST","/api/login",true)
const string = "username=" + username + "&password=" + password
xhttp.send(string)
}
