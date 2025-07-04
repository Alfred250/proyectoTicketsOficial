import sqlite3 as sql
from MdeAyuda import Base
from datetime import date
import json


class ConexionTablaTickets:
    def __init__(self):
        self.baseDatos= Base()
        
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
        conexionBaseDatos= Base()
        fecha_hoy = date.today()
        fecha_formateada = fecha_hoy.strftime("%Y-%m-%d")
        conexionBaseDatos.insertar_ticket(id_empleado,asunto,descripcion,1,fecha_formateada)
        

    def ticketsAdministrar(self,id_empleado):
        conexionBaseDatos= Base()
        return conexionBaseDatos.selectTicketsAdministrar(id_empleado)
        
        """
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute(
                    SELECT A.id_ticket, A.Descripcion, D.nombre, C.nombre, B.titulo, A.fecha_creacion
                    FROM tickets A 
                    INNER JOIN asuntos B ON A.asunto = B.id_asunto 
                    INNER JOIN departamentos C ON B.departamento = C.id_departamento 
                    INNER JOIN empleados D ON A.id_empleado = D.id_empleado
                    WHERE A.Status =0)
                columnas = [desc[0] for desc in cursor.description]
                resultado = cursor.fetchall()
                resultado_json = [dict(zip(columnas, fila)) for fila in resultado]
                return json.dumps(resultado_json, ensure_ascii=False)  
        except sql.OperationalError as e:
            print("Error base de datos: ", e)
            return str(e)
        """
        
    