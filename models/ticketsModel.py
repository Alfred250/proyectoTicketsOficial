from datetime import date
from pydantic import BaseModel

class Ticket(BaseModel):
    iIdEmpleadoSolicita: int
    sAsunto: str
    sDescripcion: str
    sSituacion:str
    sDepartamento: str
    iIdResponsable:int
    iIdEmpleadoAsignado: int
    dFechaCreacion:date
    dFechaAutorizacion:date
    iStatus: int
    dFechaSolucion:date
    dFechaCaducidad:date
    
