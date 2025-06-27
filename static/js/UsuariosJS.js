
$( document ).ready(function() {
    console.log("hola si entro")
    fetch('/api/usuarios')
      .then(response => response.json())
      .then(data => {
        console.log("data",data)
        const tbody = document.querySelector('#bodyUsuario');
        Object.entries(data).forEach(([usuario, contrasena]) => {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td>${usuario}</td>
            <td>${contrasena}</td>
          `;
          tbody.appendChild(row);
        });
      })
      .catch(error => console.error('Error cargando usuarios:', error));
});

$("#btnReg").click(async function(){
    var nIdEmpleado=  document.getElementById("txtUsuario");
    var sPassword = document.getElementById("txtPassword");
    try {
      const response = await fetch("/regUsuario", {
          method: "POST",
          headers: {
          "Content-Type": "application/json"
          },
          body: JSON.stringify({ nIdEmpleado: nIdEmpleado.value, cPassword: sPassword.value })
      });

      if (response.ok) {
          console.log("Usuario registrado correctamente");
          const data = await response.json();
          alert(data.mensaje);
      } else {
          console.error("Error al registrar el usuario");
          const error = await response.json();
          console.log(error);
          alert("Error: " + error.detail);
      }
    } catch (err) {
    alert("Error al conectarse con el servidor.");
    console.log(err);
    }
});

$("#btnRegresar").click(function(){
    console.log("regrsar")
    window.location.replace("/menu")  
})