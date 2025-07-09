from pydantic import BaseModel

class TicketMensual(BaseModel):
    mes:str
    anio:str