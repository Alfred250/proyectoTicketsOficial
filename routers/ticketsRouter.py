from fastapi import APIRouter,HTTPException
from fastapi.responses import FileResponse,JSONResponse
from data.ConexionTablaTickets import  ConexionTablaTickets
from models.ticketsModel import Ticket
from datetime import datetime
from models.id_ticketsModel import IdTicket
from models.asignarTicketModel import Asignacion
from models.rechazarTicketModel import RechazarTicket
from models.usuarioReg import IdUsuario
from models.modificarSituacionModel import SitucionModificar

router = APIRouter()


conexionTablaTickets= ConexionTablaTickets()

@router.get("/mostrarTickets", tags=["tickets"])
def mostrar_pagina_creacion_ticket():
    return FileResponse("templates/tickets/home.html")

@router.post("/registrarTicket",tags=["tickets"])
def insertar_tickets(datos:Ticket):
    fecha_hoy=datetime.now().strftime("%Y-%m/-%d")
    conexionTablaTickets.insertarTicket(datos.id_empleado,datos.asunto, datos.descripcion,1,fecha_hoy)



@router.get("/mostrarMisTickets", tags=["tickets"])
def mostrarTicketsEnviados(id_empleado:int):
    datos=conexionTablaTickets.selectTicketsPropios(id_empleado)
    if datos:
        return JSONResponse(content=datos)
    else:
        raise HTTPException(status_code=404, detail="No se encontraron registro")

@router.get("/administrarTickets", tags=["tickets"])
def mostrarAdministrarTicket(id_empleado:int):
    datos=conexionTablaTickets.ticketsAdministrar(id_empleado)
    return JSONResponse(content=datos)


@router.get("/ticketsAceptados", tags=["tickets"])
def mostrarTicketsAceptados(id_empleado:int):
    datos=conexionTablaTickets.ticketsAceptados(id_empleado)
    return JSONResponse(content=datos)

@router.post("/ticketsAsignados", tags=["tickets"])
def mostrarTicketsAsignados(datos: IdTicket):
    resultado= conexionTablaTickets.ticketsAsignados(datos.id_ticket)
    return JSONResponse(resultado)


@router.post("/asignarTicket", tags=["tickets"])
def asignarTicket(datos:Asignacion):
    resultado= conexionTablaTickets.asignarTickets(datos.id_ticket,datos.empleado,datos.situacion,datos.fecha_respuesta,datos.fecha_solucion,datos.fecha_caducidad)
    return resultado
    
@router.post('/rechazarTicket',tags=["tickets"])
def rechazarTicket(datos:RechazarTicket):
    resultado= conexionTablaTickets.rechazarTicket(datos.ticket,datos.motivo)
    return resultado

@router.post('/ticketsAsignados', tags=["tickets"])
def ticketsAsignados(datos: IdUsuario):
    print("Se recibió la solicitud para obtener tickets asignados.")
    resultado = conexionTablaTickets.ticketsAsignados(datos.id_empleado)
    return resultado

@router.get('/ticketsRechazados',tags=["tickets"])
def ticketsRechazados(id_empleado:int):
    datos=conexionTablaTickets.ticketsRechazados(id_empleado)
    return JSONResponse(content=datos)

@router.post('/modificarSituacion',tags=["tickets"])
def modificarSituacion(datos:SitucionModificar):
    resultado=conexionTablaTickets.modificarSituacion(datos.id_ticket,datos.situacion)
    return resultado

