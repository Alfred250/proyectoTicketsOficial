$(document).ready(function(){

consultarDepartamentos();
obtenerTicketsGenerados();
obtenerAdministrarTicket();
})
const id_empleado = parseInt(localStorage.getItem("idEmpleadoGlobal"));

async function consultarDepartamentos() {
  
  selectDepartamentos=document.getElementById("selectDepartamento");
  fetch('/filtroDepartamento').then(response => response.json()).then(data => {
    for(var i in data){
      var opcionDepas= document.createElement("option");
        opcionDepas.value=i;
        opcionDepas.text=data[i];
        selectDepartamentos.add(opcionDepas);
    }
    });
}

$("#selectDepartamento").on("change",function(){
  var depaSeleccionado=parseInt(this.value);
  consultarProblematicas(depaSeleccionado)
})

async function consultarProblematicas(departamento) {
  var resultado=await fetch("/filtroProblematicas", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ "id_departamento":departamento })
      });

      if (resultado.ok){
        var selectProblematicas= document.getElementById("selectProblematicas")
        selectProblematicas.innerHTML=''
        var datos= await resultado.json()
        for(var i in datos){
          var option= document.createElement('option');
          option.value=i
          option.text=datos[i]
          selectProblematicas.add(option)
        }
      }
}

$("#btnGenerarTicket").click(async function(){
  var problematica= parseInt($("#selectProblematicas").val());
    console.log($("#selectProblematicas").val())

  var especificaciones= $("#txtEspecificaciones").val();
  const idEmpleadoGlobal = parseInt(localStorage.getItem("idEmpleadoGlobal"));

  var oRegistrarTicket={
    id_empleado:idEmpleadoGlobal,
    asunto: problematica,
    descripcion:especificaciones
  }

  var comprobar=validarNoVacios(oRegistrarTicket);
  if (comprobar){

    try{
      var response= await fetch('/registrarTicket',{
        method:"POST",
        headers: {
          "Content-Type": "application/json"
        },
        body:JSON.stringify(oRegistrarTicket)
      })
      if (response.ok){
        console.log("va si se inserto")
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Tu ticket fue insertado",
          showConfirmButton: false,
          timer: 1500
        });
      }
      else{
        Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Something went wrong!",
        footer: '<a href="#">Why do I have this issue?</a>'
      });
      }
    }catch (err){
      alert("Error al conectarse con el servidor.");
      console.log(err);
    }
  }
  else{
    Swal.fire({
    icon: "error",
    title: "Oops...",
    text: "Campos vacios!"
  });
  }
})



function validarNoVacios(datos) {
  return Object.values(datos).every(valor => {
    return valor !== null && 
           valor !== undefined && 
           !(typeof valor === 'string' && valor.trim() === '') &&
           !(Array.isArray(valor) && valor.length === 0) &&
           !(typeof valor === 'object' && Object.keys(valor).length === 0);
  });
}

function mostrarApartado(idVista) {
  const secciones = [
    "CrearTicket", 
    "Asignados", 
    "Administrar", 
    "Aceptados", 
    "Rechazados"
  ];

  secciones.forEach(seccion => {
    const elemento = document.getElementById(seccion);
    if (elemento) elemento.style.display = 'none';
  });
  const vistaActiva = document.getElementById(idVista);
  if (vistaActiva) vistaActiva.style.display = 'block';
}

async function obtenerTicketsGenerados() {
  

  try {
    const response = await fetch(`/mostrarMisTickets?id_empleado=${id_empleado}`, {
      method: "GET"
    });

    if (response.ok) {
      var bodyMisTickets= document.getElementById("tbodyMitickets");
      var misTickets = await response.json();
      var misTicketsJson=JSON.parse(misTickets)
      for (var i = 0; i < misTicketsJson.length; i++) {
      var tr = document.createElement("tr")
      for (var key in misTicketsJson[i]) {
        var td = document.createElement("td");
        td.textContent = misTicketsJson[i][key];
        tr.appendChild(td);
        bodyMisTickets.appendChild(tr)
      }
        }
    } else {
      console.error("Error al obtener tickets:", response.status);
      
    }
  } catch (err) {
    console.error("Error al conectar:", err);
    Swal.fire({
      icon: "error",
      title: "Error de red",
      text: "No se pudo conectar con el servidor."
    });
  }
}

async function obtenerAdministrarTicket(){
  try{
    await fetch(`/administrarTickets?id_empleado=${id_empleado}`).then(response=>{
      if (!response.ok){
        throw new Error(`HTTP ERROR! status ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      console.log(data)
      var administrarJson= JSON.parse(data) 
      var bodyAdministrar= document.getElementById("divAdministrador");
      for(var i=0; i<administrarJson.length;i++){
        bodyAdministrar.innerHTML+=
        `
        <div class="row t-2">
                      <div class="container-fluid">
                          <div class="card ticket-card mb-3 p-3 shadow-sm">
                            <div class="row align-items-center mb-2">
                              <div class="col-4">
                                <small class="text-muted">Fecha:</small>
                                <div id="fecha">${administrarJson[i].fecha_creacion}</div>
                              </div>
                              <div class="col-4">
                                <small class="text-muted">Emisor:</small>
                                <div id="emisor">Juan Pérez</div>
                              </div>
                              <div class="col-4">
                                <label for="EmpleadoDisponible" class="form-label mb-1">Asignar a:</label>
                                <select class="form-select form-select-sm" id="EmpleadoDisponible">
                                  <option value="">Seleccione</option>
                                  <option value="1">Empleado 1</option>
                                  <option value="2">Empleado 2</option>
                                </select>
                              </div>
                            </div>

                            <div class="row small">
                              <div class="col-4">
                                <strong>Departamento:</strong><br>
                                ${administrarJson[i].nombre}
                              </div>
                              <div class="col-4">
                                <strong>Problemática:</strong><br>
                                ${administrarJson[i].titulo}
                              </div>
                              <div class="col-4">
                                <strong>Descripción:</strong><br>
                                ${administrarJson[i].descripcion}
                              </div>
                            </div>

                            <div class="mt-3 text-end">
                              <button class="btn btn-outline-danger btn-sm me-2" onclick="rechazarTicket(${administrarJson[i].id_ticket})">Rechazar</button>
                              <button class="btn btn-primary btn-sm" onclick="asignarTicket(${administrarJson[i].id_ticket})">Asignar</button>
                            </div>
                          </div>
                      </div>
                    </div>
        `
      }
      
    })
  }catch{
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Algo salio mal, no se pudo obtener los datos!",
      footer: '<a href="#">Why do I have this issue?</a>'
    });
  }
}





