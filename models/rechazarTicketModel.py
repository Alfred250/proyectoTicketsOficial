from pydantic import BaseModel

class RechazarTicket(BaseModel):
    ticket:int
    motivo:str