import sqlite3 as sql

class DataBaseUser:

    def selectUsuarios(self):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT empleado_id, password FROM usuarios")
                resultado = cursor.fetchall()

                diiccionarioUsuarios = {id_: pwd for id_, pwd in resultado}
                return diiccionarioUsuarios
        except sql.OperationalError as e:
            print("Error SQLite:", e)
            return {}

    def insertarUsuario(self, empleado_id, password):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO usuarios(empleado_id, password) VALUES (?, ?)", (empleado_id, password))
                conexion.commit()
                return {"Exito": "Se registró correctamente"}
        except sql.OperationalError as e:
            print("Error SQLite:", e)
            return {"Error": str(e)}
