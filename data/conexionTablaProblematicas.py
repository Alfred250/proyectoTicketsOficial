import sqlite3 as sql


class ConexionTablaProblematicas:
    
    def selectProblematicas():
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("SELECT * FROM asuntos")
                resultado= cursor.fetchall() 
                cursor.execute("PRAGMA table_info('tickets')")
                columnas_info = cursor.fetchall()
                nombres_columnas = [col[1] for col in columnas_info]    #convierte directamente los datos en diccionaarios
                lista_tickets = []
                for fila in resultado:
                    diccionario_fila = dict(zip(nombres_columnas, fila))
                    lista_tickets.append(diccionario_fila)
        except sql.OperationalError as e:
            print("No se puedo crear la conexion")
            return {"Error":e}
    
    def insertarProblematicas(departamento,titulo):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO asuntos(departamento,titulo) VALUES(?,?)",[departamento,titulo])
        except sql.OperationalError as e:
            return{"Error":e}
            