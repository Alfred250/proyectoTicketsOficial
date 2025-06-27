from fastapi import APIRouter
from fastapi.responses import FileResponse
from data.ConexionTablaTickets import  ConexionTablaTickets
from pydantic import BaseModel
from models.ticketsModel import Ticket

router = APIRouter()


@router.get("/mostrarTickets", tags=["tickets"])
def mostrar_pagina_creacion_ticket():
    return FileResponse("templates/tickets/home.html")

@router.post("/registrarTicket",tags=["tickets"])
def insertar_tickets(data:Ticket):
    conexionTablaTickets= ConexionTablaTickets()
    conexionTablaTickets.insertarTicket(data)