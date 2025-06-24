import sqlite3 as sql
from MdeAyuda import Base

class ConexionTablaTickets:
    def __init__(self):
        self.baseDatos= Base()
        
    def crearConexion(self):
        self.conexion = sql.connect("BD_MesadeAyuda.db")
        self.cursor= self.conexion.cursor()
        
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()
        
    def selectTickets(self):
        self.crearConexion()
        
        self.cursor.execute("SELECT * FROM tickets")
        self.resultado = self.cursor.fetchall()

        self.cursor.execute("PRAGMA table_info('tickets')")
        columnas_info = self.cursor.fetchall()
        nombres_columnas = [col[1] for col in columnas_info]  

        self.lista_tickets = []
        for fila in self.resultado:
            diccionario_fila = dict(zip(nombres_columnas, fila))
            self.lista_tickets.append(diccionario_fila)

        print(self.lista_tickets)
        self.conexion.commit()
        self.conexion.close()

        
    def insertarTicket(self,id_empleado,asunto,descripcion,status,fecha_creacion):
        self.ticket=[(id_empleado,asunto,descripcion,status,fecha_creacion)]
        self.crearConexion()
        self.cursor.executemany(f"INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion) VALUES (?, ?, ?, ?, ?)", self.ticket)
        self.cerrarConexion() 

