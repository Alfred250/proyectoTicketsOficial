from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from routers.ticketsRouter import router
from routers.filtrosTicketsRouter import router as routerFiltrosTickets
from models.regUser import RegistrarUsuario
from data.conexionTablaUsuarios import DataBaseUser
app = FastAPI(title="Las primeras pruebas")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modelo para login
class LoginData(BaseModel):
    usuario: int
    contrasena: str
    
# Usuarios simulados
USUARIOS = {
    "admin": "1234",
    "user": "abcd"
}
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", tags=["pruebas"])
def regresar_inicio():
    return FileResponse("templates/home/InicioSesion.html")

@app.post("/login", tags=["pruebas"])
def validar_login(datos: LoginData):
    dataUser= DataBaseUser()
    Usuarios= dataUser.selectUsuarios()
    usuario= int(datos.usuario)
    if usuario in Usuarios and Usuarios[usuario] == datos.contrasena:
        idUsuario = datos.usuario
        return{"idLog": idUsuario}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
@app.get("/menu", tags=["pruebas"])
def mostrar_menu():
    return FileResponse("templates/home/menuP.html")

@app.post('/regUsuario', tags=["reg"])
def registrar_usuario(datos: RegistrarUsuario):
    print(">>> Llegó solicitud de registro:", datos)
    dataUser = DataBaseUser()
    Usuarios = dataUser.selectUsuarios()
    try:
        IdEmpleado = int(datos.nIdEmpleado)
    except ValueError:
        raise HTTPException(status_code=400, detail="El ID de empleado debe ser un número entero")

    usuario_existe_antes = IdEmpleado in Usuarios
    usuario_existe_despues = False 
    if not usuario_existe_antes:
        dataUser.insertarUsuario(IdEmpleado, datos.cPassword)
        Usuarios = dataUser.selectUsuarios()
        usuario_existe_despues = IdEmpleado in Usuarios
    else:
        raise HTTPException(status_code=409, detail="El usuario ya existe") 
    if usuario_existe_despues:
        return {"mensaje": "Registro exitoso"}
    else:
        raise HTTPException(status_code=500, detail="No se pudo registrar por un error interno")


  
    
@app.get("/mostrarUsuario", tags=["reg"])
def mostrar_registro_usuario():
    return FileResponse("templates/users/usuarios.html")

@app.get("/api/usuarios", tags=["reg"])
def get_usuarios():
    dataUser= DataBaseUser()
    Usuarios= dataUser.selectUsuarios()
    return JSONResponse(content=Usuarios)
    

app.include_router(router)
app.include_router(routerFiltrosTickets)
