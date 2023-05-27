const form = document.getElementById("login-form");
form.addEventListener("submit", function(event) {
  event.preventDefault();
  const formData = new FormData(form);
  const usernameInput = formData.get("username");
  const passwordInput = formData.get("password");

  console.log("Kullanıcı Adı:", usernameInput);
  console.log("Şifre:", passwordInput);

  var formdata = new FormData();
  formdata.append("username", usernameInput);
  formdata.append("password", passwordInput);

  var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
  };

  fetch("http://localhost:8000/api/login_api/", requestOptions)
    .then(response => response.json())
    .then(data => {
      const redirectUrl = data.redirect_url;
      if (redirectUrl) {
        window.location.href = redirectUrl;
      }
    })
    .catch(error => console.log('error', error));
});