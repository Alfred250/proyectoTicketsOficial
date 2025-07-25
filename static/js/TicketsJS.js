$(document).ready(function(){

consultarDepartamentos();
obtenerTicketsGenerados();
obtenerTicketsAsignados()
})
const id_empleado = parseInt(localStorage.getItem("idEmpleadoGlobal"));
const id_empleado_Global=parseInt(localStorage.getItem("idEmpleadoGlobal"));

async function consultarDepartamentos() {
  
  var selectDepartamentos=document.getElementById("selectDepartamento");
  var selectDepartamentosPromedio=document.getElementById("selectDepartamentoPromedio");
  fetch('/filtroDepartamento').then(response => response.json()).then(data => {
    for(var i in data){
      console.log(data[i])
      var opcionDepas= document.createElement("option");
        opcionDepas.value=i;
        opcionDepas.text=data[i];
        selectDepartamentos.append(opcionDepas);
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
        body: JSON.stringify({ id_departamento:departamento })
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
    "Rechazados",
    "reporteTickets",
    "reporteTicketsOperativo"
  ];

  secciones.forEach(seccion => {
    const elemento = document.getElementById(seccion);
    if (elemento) elemento.style.display = 'none';
  });
  const vistaActiva = document.getElementById(idVista);
  if (vistaActiva) vistaActiva.style.display = 'block';
  if(idVista='Administrar'){
    obtenerAdministrarTicket()
  }
  if(idVista='Aceptados'){
    obtenerTicketsAceptados()
  }
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

function obtenerEmpleadoAsignar(id_ticket, selectElement) {
  const id_ticketParse = parseInt(id_ticket);
  const datosAsignados = { id_ticket: id_ticketParse };

  fetch('/ticketsAsignados', {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(datosAsignados)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ERROR: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    const empleadoJson = JSON.parse(data);
    selectElement.innerHTML = '<option value="">Seleccione</option>'; // Limpiar antes de llenar

    empleadoJson.forEach(dato => {
      const opt = document.createElement("option");
      opt.value = dato.id_empleado;
      opt.text = dato.nombre;
      selectElement.append(opt);
    });
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
}

 function obtenerAdministrarTicket(){
  try{
    fetch(`/administrarTickets?id_empleado=${id_empleado}`).then(response=>{
      if (!response.ok){
        throw new Error(`HTTP ERROR! status ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      var administrarJson= JSON.parse(data) 
      var bodyAdministrar= document.getElementById("divAdministrador");
      for(var i=0; i<administrarJson.length;i++){
        bodyAdministrar.innerHTML+=
        `
        <div class="row t-2">
                      <div class="container-fluid">
                          <div class="card ticket-card mb-3 p-3 shadow-sm">
                            <label for="fecha" style="text-align:center; ">Fecha de caducidad</label>
                            <input type="date" name="fecha" id="fechaAsignacion">
                            <div class="row align-items-center mb-2">
                              <div class="col-4">
                                <small class="text-muted">Fecha:</small>
                                <div id="fecha">${administrarJson[i].fecha_creacion}</div>
                              </div>
                              <div class="col-4">
                                <small class="text-muted">Emisor:</small>
                                <div id="emisor">${administrarJson[i].nombre}</div>
                              </div>
                              <div class="col-4">
                                <label for="EmpleadoDisponible" class="form-label mb-1">Asignar a:</label>
                                <select class="form-select form-select-sm select-empleado" data-id-ticket="${administrarJson[i].id_ticket}" id="selectEmpleadoAsig">
                                <option value="">Seleccione</option>
                              </select>
                              </div>
                            </div>

                            <div class="row small">
                              <div class="col-5">
                                <strong>Problemática:</strong><br>
                                ${administrarJson[i].descripcion}
                              </div>
                              <div class="col-7">
                                <strong>Descripción:</strong><br>
                                ${administrarJson[i].descripcion}
                              </div>
                            </div>
                            <div class="mt-3 text-end">
                              <button class="btn btn-outline-danger btn-sm me-2" onclick="rechazarTicket(${administrarJson[i].id_ticket})">Rechazar</button>
                              <button class="btn btn-primary btn-sm" onclick="asignarTicket('${administrarJson[i].id_ticket}','${administrarJson[i].fecha_creacion}')">Asignar</button>
                            </div>
                          </div>
                      </div>
                    </div>
        `
      }
      document.querySelectorAll('.select-empleado').forEach(select => {
    const id_ticket = select.getAttribute("data-id-ticket");
    obtenerEmpleadoAsignar(id_ticket, select); 
  });
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

function asignarTicket(ticket,fecha_creacion){
  var id_empleadoAsignado= parseInt(document.getElementById("selectEmpleadoAsig").value);
  var fecha_caducidad= document.getElementById("fechaAsignacion").value;
  var id_ticket= parseInt(ticket)
  console.log(Date.parse(fecha_caducidad))
  console.log(Date.parse(fecha_creacion))
  if(Date.parse(fecha_creacion)>Date.parse(fecha_caducidad)){
    Swal.fire({
    icon: "error",
    title: "Oops...",
    text: "No puedes asignar una fecha menor a la de creacion!"
  });
    throw new Error("NO SE PUEDE ASIGNAR UNA FECHA MENOR A LA DE CREACION")

  }
  data={
    id_ticket:id_ticket,
    empleado:id_empleadoAsignado,
    situacion:"En observacion",
    fecha_respuesta:"na",
    fecha_solucion:"na",
    fecha_caducidad:fecha_caducidad
  }
  try {
    if(validarNoVacios(data)){
      fetch('/asignarTicket',{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(data)
    }).then(response=>{
      if(!response.ok){
        throw new Error(`HTTP ERROR: ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      console.log(data)
      if(data.mensaje=="Sí se aceptó"){
        Swal.fire({
        title: "Se asigno al empleado!",
        icon: "success",
        draggable: true
      });
      obtenerAdministrarTicket()
      
      }
    })
    }
    else{
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Campos vacios!"  
      });
    }
  } catch (error) {
    
  }
}

function rechazarTicket(ticket){
  var id_ticket= parseInt(ticket)
  var modalRechazar = $('#modalRechazar');
  modalRechazar.modal('show');
  $("#txtMotivo").val('')
  $("#btnRechazar").on("click",function(){
    var motivo= document.getElementById("txtMotivo").value;
    if(motivo==''){
      throw new Error
      (Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Agregue el motivo!"
      }))
    }else{
      var datosRechazar={
        ticket:id_ticket,
        motivo:motivo
      }
      try {
      fetch('/rechazarTicket',{
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify(datosRechazar)
      }).then(response=>{
        if(!response.ok){
          throw new Error(`ERROR HTTP: ${response.status}`)
        }
        return response.json()
      }).then(data=>{
        console.log(data.mensaje)
        if(data.mensaje=="Sí se rechazo"){
          Swal.fire({
            title: "Rechazado correctamente!",
            icon: "success",
            draggable: true
          });
          obtenerAdministrarTicket()
           modalRechazar.modal('hide');
        }
      })
    } catch (error) {
      
    }
  }
  });
}

async function obtenerTicketsAceptados() {
  try{
    console.log("entro al js de aceptados")
    await fetch(`/ticketsAceptados?id_empleado=${id_empleado}`).then(response=>{
      if(!response.ok){
        throw new Error(`HTTP ERROR ${response.status}`)
      }
      return response.json() 
    }).then(data=>{
      var bodyAceptados = document.getElementById("bodyAceptados");
      var aceptadosJson= JSON.parse(data)
      for(var i =0; i<aceptadosJson.length;i++){
        var contenido=`
          <tr>
            <td>${aceptadosJson[i].titulo}</td>
            <td>${aceptadosJson[i].descripcion}</td>
            <td>${aceptadosJson[i].fecha_creacion}</td>
            <td>${aceptadosJson[i].nombre}</td>
            <td>${aceptadosJson[i].situacion}</td>
            <td>${aceptadosJson[i].fecha_solucion}</td>
            <td>${aceptadosJson[i].fecha_caducidad}</td>
          </tr>
        `
        bodyAceptados.innerHTML += contenido
      }

    })
  }catch{
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Algo salio mal, no se pudo obtener los tickets Aceptados!",
      footer: '<a href="#">Why do I have this issue?</a>'
    });
  }
}

async function obtenerOperativoTicketsDiario(fecha) {
  try {
    fetch(`/operativoDiarioTickets?fecha=${fecha}`).then(response=>{
      if(!response.ok){
        throw new Error(`HTTP ERROR: ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      var bodyTicketsDiarios= document.getElementById("bodyTicketsDiarios");
      var jsonTicketsDiarios=JSON.parse(data)    
      bodyTicketsDiarios.innerHTML=''  
      jsonTicketsDiarios.forEach((ticketsDiario)=>{
        bodyTicketsDiarios.innerHTML+=`
          <tr>
            <td>${ticketsDiario.fecha_creacion}</td>
            <td>${ticketsDiario.nombre}</td>
            <td>${ticketsDiario.total}</td>
          </tr>
        `
      })

    })
  } catch (error) {
    
  }
}

$("#btnConsultarDiario").click(function(){
  var fecha= document.getElementById("datePicker");
  fechaSele= fecha.value
  console.log(fechaSele)
  if(!fechaSele){
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Selecciona una fecha!"
    });
  }
  obtenerOperativoTicketsDiario(fechaSele)
});

function obtenerOperativoMensualDepartamento(mes,anio){
  data={
    mes:mes,
    anio:anio
  }
  try {
    fetch(`/operativoMensualTicketsDepa`,{
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body: JSON.stringify(data)
    }).then(response=>{
      if(!response.ok){
        throw new Error(`HTTP ERROR: ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      var bodyTicketsMensualDepa= document.getElementById("bodyTicketsMensualDepa")
      bodyTicketsMensualDepa.innerHTML=''
      var jsonTicketsMensuales= JSON.parse(data)

      jsonTicketsMensuales.forEach((ticket)=>{
        bodyTicketsMensualDepa.innerHTML+=`
          <tr>
            <td>${ticket.fecha_creacion}</td>
            <td>${ticket.nombre}</td>
            <td>${ticket.total}</td>
          </tr>
        `
      })
    })
  } catch (error) {
    
  }
}

$("#btnConsultarMensualDepa").click(function(){
  var datepicker1= document.getElementById("datepicker1")
  datepicker1= datepicker1.value
  if(!datepicker1){
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Escoge un mes y año"
    });
  }else{
    var aFecha=datepicker1.split("-")
    obtenerOperativoMensualDepartamento(aFecha[1],aFecha[0])
  }
});

function obtenerOperativoTicketsCaducados(fecha_inicio, fecha_fin){
  var data={
    fecha_inicio:fecha_inicio,
    fecha_fin:fecha_fin
  }
  try {
    fetch('/operativoTicketsCaducados',{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify(data)
    }).then(response=>{
      if(!response.ok){
        throw new Error(`ERROR HTTP ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      jsonTicketsCaducados= JSON.parse(data)
      var bodyTicketsCaducados = document.getElementById("bodyTicketsCaducados");
      bodyTicketsCaducados.innerHTML=''
      jsonTicketsCaducados.forEach((ticketCaducado)=>{
        bodyTicketsCaducados.innerHTML+=`
          <tr>
            <td>${ticketCaducado.id_ticket}</td>
            <td>${ticketCaducado.descripcion}</td>
            <td>${ticketCaducado.nombre}</td>
            <td>${ticketCaducado.situacion}</td>
            <td>${ticketCaducado.fecha_solucion}</td>
            <td>${ticketCaducado.fecha_creacion}</td>
            <td>${ticketCaducado.fecha_respuesta}</td>
            <td>${ticketCaducado.fecha_caducidad}</td>
          </tr>
        `
      })
    })
  } catch (error) {
    
  }
}


$(function () {
    $('#rangoFechas').daterangepicker({
      locale: {
        format: 'YYYY-MM-DD',
        applyLabel: 'Aplicar',
        cancelLabel: 'Cancelar',
        fromLabel: 'Desde',
        toLabel: 'Hasta',
        customRangeLabel: 'Personalizado',
        weekLabel: 'S',
        daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
          'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        firstDay: 1
      },
      opens: 'right'
    });
     $('#rangoFechasPromedio').daterangepicker({
      locale: {
        format: 'YYYY-MM-DD',
        applyLabel: 'Aplicar',
        cancelLabel: 'Cancelar',
        fromLabel: 'Desde',
        toLabel: 'Hasta',
        customRangeLabel: 'Personalizado',
        weekLabel: 'S',
        daysOfWeek: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
          'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        firstDay: 1
      },
      opens: 'right'
    });
});

$("#btnConsultarCaducados").click(function(){
  var rangoFechas= document.getElementById("rangoFechas");
  rangoFechas= rangoFechas.value
  var nuevasFechas= rangoFechas.split(' - ')
  obtenerOperativoTicketsCaducados(nuevasFechas[0], nuevasFechas[1])
})

function obtenerOperativoTiempoRespuesta(departamentore, fecha_inicio, fecha_fin){
 
  console.log(departamentore)
  var data={
    departamento:departamentore, 
    fecha_inicio:fecha_inicio,
    fecha_fin:fecha_fin
  }
  try {
    fetch('/operativoTiempoRespuesta',{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify(data)
    }).then(response=>{
      if(!response.ok){
        throw new Error(`HTTP ERROR ${response.status}`)
      }
      return response.json()
    }).then(respuesta=>{
      var bodyPromedioRespuesta= document.getElementById("bodyPromedioRespuesta")
      bodyPromedioRespuesta.innerHTML=`
        <tr>
          <td>${respuesta.timepo_respuesta}</td>
          <td>${respuesta.resueltos}</td>
          <td>${respuesta.promedio}</td>
        </tr>
      `
      
    })
  } catch (error) {
    
  }
}

$("#btnConsultarPromedio").click(function(){
  var rangoFechasPromedio= document.getElementById("rangoFechasPromedio");
  rangoFechasPromedio= rangoFechasPromedio.value;
  var nuevasFechas= rangoFechasPromedio.split(' - ')
  var selectDepartamentosPromedio= document.getElementById("selectDepartamentoPromedio").value
  var valorSeleccionado = parseInt(selectDepartamentosPromedio);
  console.log(valorSeleccionado)
  if(valorSeleccionado>0){
    obtenerOperativoTiempoRespuesta(valorSeleccionado,nuevasFechas[0],nuevasFechas[1])
  }else{

  }
})


function obtenerTicketsAsignados() {
  console.log(id_empleado_Global);
  var datosAsignados = {
    "id_ticket": parseInt(id_empleado_Global)
  };

  fetch('/ticketsAsignados', {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(datosAsignados)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ERROR: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    var divAsignados = document.getElementById("divAsignados");
    var aAsignados= JSON.parse(data)
    aAsignados.forEach(asignado=>{
      var fechaAs=asignado.fecha_creacion 
      fechaAsig=fechaAs.substring(0,10)
      divAsignados.innerHTML+=`
        <div class="card ticket-card mb-3 p-3 shadow-sm">
          <div class="row align-items-center mb-2">
            <div class="col-4">
              <small class="text-muted">Fecha Asignaciòn:</small>
              <div id="fecha">${fechaAsig}</div>
            </div>
            <div class="col-4">
              <small class="text-muted">Fecha Caducidad:</small>
              <div id="fecha_caducidad">${asignado.fecha_caducidad}</div>
            </div>
            <div class="col-4">
              <label for="EmpleadoDisponible" class="form-label mb-1">Situacion:</label>
              <select class="form-select form-select-sm" id="EmpleadoDisponible">
                <option value="">Seleccione una opcion</option>
                <option value="1">En revision</option>
                <option value="2">En proceso</option>
                <option value="3">Cancelado</option>
                <option value="4">Completo</option>
              </select>
            </div>
          </div>

          <div class="row small">
            <div class="col-4">
              <strong>Problematica:</strong><br>
              ${asignado.titulo}
            </div>
            <div class="col-4">
              <strong>Detalle:</strong><br>
              ${asignado.descripcion}
            </div>
          </div>
        </div>
      `
    })
  })
  .catch(error => {
    console.error('Error en la solicitud:', error);
  });
}

