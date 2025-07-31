import sqlite3 as sql
import json

class ConexionTablaProblematicas:
    
    def selectProblematicas(self,departamento):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor= conexion.cursor()
                cursor.execute('SELECT id_asunto,titulo FROM asuntos WHERE departamento=?',[departamento])  # Asegúrate que estos campos existen
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

    def selectProblematicasSinDepartamento(self,id_empleado):
        try:
            with sql.connect("BD_MesadeAyuda.db") as conexion:
                cursor = conexion.cursor()
                cursor.execute(f"SELECT departamentos.id_departamento FROM empleados "
                            f"INNER JOIN puestos ON puestos.id_puesto = empleados.puesto "
                            f"INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id "
                            f"WHERE empleados.id_empleado = ?", (id_empleado,))
                departamento = cursor.fetchone()
                print(departamento[0])
                if departamento:
                    departamento_nombre = departamento[0]
                    cursor.execute(f"SELECT id_asunto, titulo FROM asuntos WHERE departamento = ?", (departamento_nombre,))
                    columnas = [desc[0] for desc in cursor.description]
                    resultado = cursor.fetchall()
                    resultado_json = [dict(zip(columnas, fila)) for fila in resultado]
                    return json.dumps(resultado_json, ensure_ascii=False)
                else:
                    return json.dumps({"Error": f"No se encontró departamento para el empleado con ID {id_empleado}"})
        except sql.OperationalError as e:
            print(f"No se pudo crear la conexión: {e}")
            return json.dumps({"Error": str(e)})