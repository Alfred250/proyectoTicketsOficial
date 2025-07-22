import sqlite3 as sql
from MdeAyuda import Base
from datetime import date
import json


class ConexionTablaTickets:
    def __init__(self):
        self.baseDatos= Base()
        self.conexionBase=Base()
        
    def selectTicketsPropios(self, id_empleado):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT A.id_ticket, C.nombre AS departamento, B.titulo, A.status 
                    FROM tickets A 
                    INNER JOIN asuntos B ON A.asunto = B.id_asunto 
                    INNER JOIN departamentos C ON B.departamento = C.id_departamento 
                    WHERE id_empleado = ?""", [id_empleado])
                columnas = [desc[0] for desc in cursor.description]
                resultado = cursor.fetchall()
                resultado_json = [dict(zip(columnas, fila)) for fila in resultado]
                return json.dumps(resultado_json, ensure_ascii=False)  # Para que no escape acentos
        except sql.OperationalError as e:
            print("Error base de datos: ", e)
            return str(e)

        
    def insertarTicket(self,id_empleado,asunto,descripcion):
        fecha_hoy = date.today()
        fecha_formateada = fecha_hoy.strftime("%Y-%m-%d")
        self.conexionBase.insertar_ticket(id_empleado,asunto,descripcion,1,fecha_formateada)
        

    def ticketsAdministrar(self,id_empleado):
        ejecucion= self.conexionBase.consultar_tickets_pendientes(id_empleado)
        return ejecucion
       
    def ticketsAceptados(self,id_empleado):
        ejecucion= self.conexionBase.consultar_tickets_aceptados(id_empleado)
        return ejecucion
        
    def ticketsAsignados(self,id_ticket):
        ejecucion= self.conexionBase.consultar_empleado_depto(id_ticket)
        return ejecucion
    
    def asignarTickets(self,id_ticket,empleado,situacio,fecha_respuesta,fecha_solucion,fecha_caducidad):
        ejecucion= self.conexionBase.aceptar_ticket(id_ticket,empleado,situacio,fecha_respuesta,fecha_solucion,fecha_caducidad)
        return ejecucion
    
    def rechazarTicket(self,ticket,motivo):
        ejecucion= self.conexionBase.rechazar_ticket(ticket,motivo)
        return ejecucion