from pydantic import BaseModel

class TicketsCaducados(BaseModel):
    fecha_inicio:str
    fecha_fin:str