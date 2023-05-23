const form = document.getElementById("login-form");
if (isAuthenticated()) {
  window.location.href = "/";
}else{
}
form.addEventListener("submit", function(event) {
  event.preventDefault();
  const formData = new FormData(form);
  const usernameInput = formData.get("username");
  const passwordInput = formData.get("password");

  console.log("Kullanıcı Adı:", usernameInput);
  console.log("Şifre:", passwordInput);

  var requestOptions = {
    method: 'POST',
    body: formData,
    redirect: 'follow'
  };

  fetch("http://localhost:8000/api/login_api/", requestOptions)
    .then(response => response.text())
    .then(result => {console.log(result)
      const token = result; // Token'ı JSON yanıttan al
      localStorage.setItem("token", token);
      window.location.href = "/index/";
    })
    .catch(error => console.log('error', error));
});
function isAuthenticated() {
  if (localStorage.getItem('token') != null) {
      return true;
  }
  return false;
}