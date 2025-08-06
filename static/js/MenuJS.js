document.addEventListener("DOMContentLoaded", function () {
    ocultar()
    $("#btnTickets").click(function(){
         window.location.href = "/mostrarTickets";
    });

});
const id_empleado_Global=parseInt(localStorage.getItem("idEmpleadoGlobal"));

console.log(id_empleado_Global)
function ocultar(){
    var oIdEmpleadoPuesto={
      id_empleado: id_empleado_Global
    }

    
    $("#btnRegUsuario").click(function(){
        window.location.href = "/mostrarUsuario";
    });

  try {
    fetch('/consultarPuesto',{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(oIdEmpleadoPuesto)
    }).then(response=>{
      if(!response.ok){
        throw new Error(`ERROR HTTP ${response.status}`)
      }
      return response.json()
    }).then(data=>{
      var puestoJson=JSON.parse(data)
      var puesto= puestoJson.puesto[0]
      console.log(puesto)
      if(puesto.includes("Gerente") || puesto.includes("Supervisor") || puesto.includes("Jefe")){
          
      }else{
      document.querySelectorAll('.ocultar').forEach(function(el) {
            el.style.display = 'none';
          });
      }
    })
  } catch (error) {
    
  }

}