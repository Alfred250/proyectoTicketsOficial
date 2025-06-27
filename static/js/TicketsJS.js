$(document).ready(function(){

consultarDepartamentos();
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
  var especificaciones= $("#txtEspecificaciones").val();
  const idEmpleadoGlobal = parseInt(localStorage.getItem("idEmpleadoGlobal"));

  console.log(problematica)
  var oRegistrarTicket={
    id_empleado:idEmpleadoGlobal,
    asunto: problematica,
    descripcion:especificaciones
  }
  //var result=comprobacionDatos(datos )
  //if(result){
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
      }
    }catch (err){
      alert("Error al conectarse con el servidor.");
      console.log(err);
    }
  //}
})


function comprobacionDatos(datos){
  for (var i in datos){
    if (datos[i].length === 0){
      return false;
    }
  }
  return true;
}


async function obtenerTicketsAdministrar(){
  

}