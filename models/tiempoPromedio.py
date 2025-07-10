from pydantic import BaseModel

class TiempoPromedio(BaseModel):
    departamento:int
    fecha_inicio:str
    fecha_fin:str