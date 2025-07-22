from pydantic import BaseModel

class Asignacion(BaseModel):
    id_ticket: int
    empleado:int
    situacion:str
    fecha_respuesta:str
    fecha_solucion:str
    fecha_caducidad:str