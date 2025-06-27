 window.idEmpleadoGlobal=null;
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("loginForm");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const usuario = parseInt(document.getElementById("loginName").value);
    const contrasena = document.getElementById("loginPassword").value;

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ usuario, contrasena })
      }); 
      if (response.ok) {
        const data = await response.json();
        console.log("Login successful:", data);
        localStorage.setItem("idEmpleadoGlobal", data.idLog);
        alert(data.idLog);
        window.location.href = "/menu";
      } else {
        const error = await response.json();
        alert("Error: " + error.detail);
      }
    } catch (err) {
      alert("Error al conectarse con el servidor.");
      console.error(err);
    }
  });
    $('.datepicker').datepicker({
      format: 'yyyy-mm-dd',
      autoclose: true,
      todayHighlight: true
    });
});
