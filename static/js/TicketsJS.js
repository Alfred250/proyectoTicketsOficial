$(document).ready(function(){

consultarDepartamentos();
obtenerTicketsGenerados();
})

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
  const id_empleado = parseInt(localStorage.getItem("idEmpleadoGlobal"));
  console.log("ID empleado:", id_empleado);

  try {
    console.log("si entro")
    console.log(id_empleado)
    const response = await fetch(`/mostrarMisTickets?id_empleado=${id_empleado}`, {
      method: "GET"
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Tickets recibidos:", data);
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
