import sqlite3 as sql
from MdeAyuda import Base
from datetime import date

class ConexionTablaTickets:
    def __init__(self):
        self.baseDatos= Base()
        
    def selectTicketsPropios(self, id_empleado):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("SELECT * FROM tickets WHERE id_empleado=?",id_empleado)
                resultado= cursor.fetchall()
                diccionario_tickets={{fila[0]:fila[1] for fila in resultado}}
                return diccionario_tickets
        except sql.OperationalError as e:
            print("Error base de datos: ",e)
            return e
        
    def insertarTicket(self,id_empleado,asunto,descripcion):
        conexionBaseDatos= Base()
        fecha_hoy = date.today()
        fecha_formateada = fecha_hoy.strftime("%Y-%m-%d")
        conexionBaseDatos.insertar_ticket(id_empleado,asunto,descripcion,1,fecha_formateada)
        
'''
    def selectTicketsGenerados(self,id_empleado):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("SELECT * FROM tickets WHERE id_empleado=?",[id_empleado])
                resultado= cursor.fetchall()
                diccionario_tickets={{fila[0]:fila[1] for fila in resultado}}
                return diccionario_tickets
        except sql.OperationalError as e:
            print("Error base de datos: ",e)
            return e
    '''