function oncreateClick(){
    const create = document.getElementById("create").value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
      if (this.readyState == 4 && this.status == 200){
        const resultString = this.responseText;
        var resultObject = JSON.parse(resultString);
        //  was_successful is key that we set in dictionary from wiews.py
        if(resultObject.was_successful === false){
          console.log(resultObject.reason);
        }else{
          window.location.href = "/register_success";
        }
      }
    }
    xhttp.open("POST","api/register", true);
    xhttp.setRequestHeader("content-type","application/x-www-form-urlencoded");
    xhttp.send("first_name="+first_name+"&last_name="+last_name+"&username="+username+"&password="+password+"&email="+email);
}
