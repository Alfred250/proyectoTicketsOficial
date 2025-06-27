from fastapi import APIRouter
from fastapi.responses import FileResponse
from data.ConexionTablaTickets import  ConexionTablaTickets
from pydantic import BaseModel
from models.ticketsModel import Ticket
from models.usuarioReg import IdUsuario

router = APIRouter()


@router.get("/mostrarTickets", tags=["tickets"])
def mostrar_pagina_creacion_ticket():
    return FileResponse("templates/tickets/home.html")

@router.post("/registrarTicket",tags=["tickets"])
def insertar_tickets(datos:Ticket):
    conexionTablaTickets= ConexionTablaTickets()
    conexionTablaTickets.insertarTicket(datos.id_empleado,datos.asunto, datos.descripcion)

'''
mostrar tickets enviados 
@router.get("/mostrarMisTickets", tags=["tickets"])
def mostrarTicketsEnviados(id_empleado:IdUsuario):
    conexionTablaTickets= ConexionTablaTickets()
    conexionTablaTickets.(id_empleado)
'''