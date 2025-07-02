from fastapi import APIRouter,HTTPException
from fastapi.responses import FileResponse,JSONResponse
from data.ConexionTablaTickets import  ConexionTablaTickets
from pydantic import BaseModel
from models.ticketsModel import Ticket
from datetime import datetime

router = APIRouter()


@router.get("/mostrarTickets", tags=["tickets"])
def mostrar_pagina_creacion_ticket():
    return FileResponse("templates/tickets/home.html")

@router.post("/registrarTicket",tags=["tickets"])
def insertar_tickets(datos:Ticket):
    conexionTablaTickets= ConexionTablaTickets()
    fecha_hoy=datetime.now().strftime("%Y-%m/-%d")
    conexionTablaTickets.insertarTicket(datos.id_empleado,datos.asunto, datos.descripcion,1,fecha_hoy)



@router.get("/mostrarMisTickets", tags=["tickets"])
def mostrarTicketsEnviados(id_empleado:int):
    print(id_empleado)
    conexionTablaTickets= ConexionTablaTickets()
    datos=conexionTablaTickets.selectTicketsPropios(id_empleado)
    if datos:
        return JSONResponse(content=datos)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron registro")

@router.get("/administrarTickets", tags=["tickets"])
def mostrarAdministrarTicket():
    conexionTablaTickets= ConexionTablaTickets()
    datos=conexionTablaTickets.selectTicketsAdministrar()
    return JSONResponse(content=datos)

@router.get("/asignarTicket", tags=["tickets"])
def asignarTicket():
    conexionTablaTickets= ConexionTablaTickets()
    datos=conexionTablaTickets.selectTicketsAdministrar()
    return JSONResponse(content=datos)