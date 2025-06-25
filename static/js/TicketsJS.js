$(document).ready(function(){

consultarDepartamentos();
})

async function consultarDepartamentos() {
  
  selectDepartamentos=document.getElementById("selectDepartamento");
  fetch('/filtroDepartamento').then(response => response.json()).then(data => {
      var departamentosValues= Object.values(data);
      departamentosValues.forEach(depa => {
        var opcionDepas= document.createElement("option");
        opcionDepas.value=Object.keys(data);
        opcionDepas.text=depa;
        selectDepartamentos.add(opcionDepas);
      });
    });
}

$("#selectDepartamento").on("change",function(){
  var depaSeleccionado=this.value;
  consultarProblematicas(depaSeleccionado)
})

async function consultarProblematicas(departamento) {
  var resultado=await fetch("/filtroProblematicas", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ departamento })
      });

      if (resultado.ok){
        console.log(resultado)
      }

}

