import sqlite3 as sql


class ConexionTablaProblematicas:
    
    def selectProblematicas(self,departamento):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("SELECT id_asunto,titulo FROM asuntos WHERE departamento= ?",[departamento])  # Asegúrate que estos campos existen
                resultado = cursor.fetchall()

                diccionario_resultado = {str(fila[0]): fila[1] for fila in resultado}

                return diccionario_resultado
        except sql.OperationalError as e:
            print("No se puedo crear la conexion")
            return {"Error":e}
    
    def insertarProblematicas(self,departamento,titulo):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor=conexion.cursor()
                cursor.execute("INSERT INTO asuntos(departamento,titulo) VALUES(?,?)",[departamento,titulo])
        except sql.OperationalError as e:
            return{"Error":e}
            