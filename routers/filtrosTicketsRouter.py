
from fastapi import APIRouter
from fastapi.responses import FileResponse
from data.conexionTablaDepartamento import ConexionTablaDepartamento
from data.conexionTablaProblematicas import ConexionTablaProblematicas
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
router = APIRouter()



@router.get('/filtroDepartamento',tags=['filtros'])
def consultarDepartamentos():
    tDepartamentos= ConexionTablaDepartamento()
    datosDepartamentos=tDepartamentos.selectDepartamento()
    print(datosDepartamentos)
    if datosDepartamentos:
        return JSONResponse(content=datosDepartamentos)
    else:
        raise HTTPException(status_code=404, detail="No se pudo registrar")
    

@router.get('/filtroProblematicas',  tags=["filtros"])
def consultarProblematicas():
    tProblematicas= ConexionTablaProblematicas()
    resultado= tProblematicas.selectProblematicas()
    print(resultado)
    if resultado:
        return JSONResponse(content=resultado)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron registro")