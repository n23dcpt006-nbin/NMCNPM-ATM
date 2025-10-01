const form = document.getElementById("loginForm");
const errorMsg = document.getElementById("error-msg");

form.addEventListener("submit", function(e) {
  e.preventDefault(); 

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  if (username === "" || password === "") {
    errorMsg.textContent = "Please enter full your Username and Password!";
    return;
  }

  if (username === "admin" && password === "1234") {
    alert("Login successful!");
    errorMsg.textContent = "";
  } else {
    errorMsg.textContent = " The Username or Password is incorrect!";
  }
});

function cancelLogin() {
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
  document.getElementById("remember").checked = false;
  errorMsg.textContent = "";
}
