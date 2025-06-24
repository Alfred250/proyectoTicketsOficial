$(document).ready(function(){

consultarDepartamentos()
})

async function consultarDepartamentos() {
  fetch('/filtroDepartamento')
    .then(response => response.json())
    .then(data => {
      console.log("departamento",data)
      
      });
}

async function consultarProblematicas(params) {
  fetch('/filtroProblematicas').then(response=> response.json()).then(data=>{
    console.log("problematicas",data)
  })
}
