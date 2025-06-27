from datetime import date
from pydantic import BaseModel

class Ticket(BaseModel):
    id_empleado: int
    asunto: int
    descripcion: str
    
