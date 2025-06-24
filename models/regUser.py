from pydantic import BaseModel

class RegistrarUsuario(BaseModel):
    nIdEmpleado: str
    cPassword: str