from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/mostrarTickets", tags=["tickets"])
def mostrar_pagina_creacion_ticket():
    return FileResponse("templates/tickets/home.html")
