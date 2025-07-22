from data.conexionReporteOperativo import ReporteOperativo
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.ticketMensual import TicketMensual
from models.ticketsCaducados import TicketsCaducados
from models.tiempoPromedio import TiempoPromedio

router= APIRouter()
reporteOperativo=ReporteOperativo()

@router.get("/operativoDiarioTickets", tags=["reporteOperativo"])
def consultarReporteDiarioTickets(fecha:str):
    resultado= reporteOperativo.filtroTicketsDiarios(fecha)
    if resultado:
        return JSONResponse(content=resultado)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron registro")

@router.post("/operativoMensualTicketsDepa", tags=["reporteOperativo"])
def consultarReporteMensualTicketsDepa(datos:TicketMensual):
    resultado= reporteOperativo.filtroTicketsMensualDepartamento(datos.mes,datos.anio)
    if(resultado):
        return JSONResponse(content=resultado)
    else:
        raise HTTPException(status_code=404,detail="No se encontro registro")

@router.post("/operativoTicketsCaducados",tags=["operativo"])
def consultarTicketsCaducados(datos:TicketsCaducados):
    resultado=reporteOperativo.filtroTicketsCaducados(datos.fecha_inicio, datos.fecha_fin)
    if(resultado):
        return JSONResponse(content=resultado)
    else:
        return HTTPException(status_code=400, detail="No se encontraron caducados")
    
@router.post("/operativoTiempoRespuesta",tags=["reporteOperativo"])
def consultarTiempoRespuesta(datos:TiempoPromedio):
    print("si entro al respuesta")
    resultado= reporteOperativo.filtroTiempoRespuesta(datos.departamento,datos.fecha_inicio, datos.fecha_fin)
    if(resultado):
        return JSONResponse(content=resultado)
    else:
        return HTTPException(status_code=400, detail="No se encontaron registros")