import sqlite3 as sql


class ConexionTablaDepartamento:
    
    def selectDepartamento(self):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("SELECT * FROM departamentos")
                resultado= cursor.fetchall()
                diccionario= {id_departamento:nombre  for id_departamento, nombre in resultado}
                return diccionario
        except sql.OperationalError as e:
            print("nO SE PUDO")
            return {}
        
    def ingresarDepartamento(self, nombreDepa):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute("INSERT INTO departamentos(nombre) VALUES(?)",[nombreDepa])
        except sql.OperationalError as e:
            print("ERROR EN LA BASE: ",e)
    
            
            
