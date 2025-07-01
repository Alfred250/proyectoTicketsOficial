
from fastapi import APIRouter
from fastapi.responses import FileResponse
from data.conexionTablaDepartamento import ConexionTablaDepartamento
from data.conexionTablaProblematicas import ConexionTablaProblematicas
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
router = APIRouter()

class Problematica(BaseModel):
    id_departamento:int

@router.get('/filtroDepartamento',tags=['filtros'])
def consultarDepartamentos():
    tDepartamentos= ConexionTablaDepartamento()
    datosDepartamentos=tDepartamentos.selectDepartamento()
    if datosDepartamentos:
        return JSONResponse(content=datosDepartamentos)
    else:
        raise HTTPException(status_code=404, detail="No se pudo registrar")
    

@router.post('/filtroProblematicas',  tags=["filtros"])
def consultarProblematicas(datos:Problematica):
    print("si entro al filtro prroble")
    tProblematicas= ConexionTablaProblematicas()
    resultado= tProblematicas.selectProblematicas(datos.id_departamento)
    print("this result",resultado)
    if resultado:
        return JSONResponse(content=resultado)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron registro")