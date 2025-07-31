from pydantic import BaseModel

class SitucionModificar(BaseModel):
    id_ticket:int
    situacion:str