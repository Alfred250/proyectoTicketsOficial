import sqlite3 as sql
import datetime
from datetime import datetime
import pandas as pd
import json

class Base:
    def crearBD():
        #Instanciar objeto con las caracteristicas de una base de datos
        conexion = sql.connect("BD_MesadeAyuda.db")
        #(Realiza Cambios en la base de datos)
        conexion.commit()
        conexion.close()

    def crearTabla_Asuntos():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE asuntos (
                        id_asunto INTEGER PRIMARY KEY AUTOINCREMENT,
                        departamento INTEGER NOT NULL,
                        titulo TEXT NOT NULL,
                        FOREIGN KEY (departamento) REFERENCES departamentos(id_departamento)

                    )
                """
            )
            conexion.commit()
            conexion.close()

    def crearTabla_TicketsAceptados():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE ticketaceptado (
                        ticket INTEGER NOT NULL , 
                        empleado INTEGER NOT NULL,
                        situacion TEXT NOT NULL,
                        fecha_respuesta TEXT NOT NULL,
                        fecha_solucion TEXT NOT NULL,
                        fecha_caducidad TEXT NOT NULL,
                        FOREIGN KEY (ticket) REFERENCES tickets(id_ticket)
                        FOREIGN KEY (empleado) REFERENCES empleados(id_empleado)

                    )
                """
            )

    def crearTabla_TicketsRechazados():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE tickets_rechazados (
                        id_ticket INTEGER NOT NULL,
                        motivo INTEGER NOT NULL , 
                        fecha_respuesta TEXT NOT NULL,
                        FOREIGN KEY (id_ticket) REFERENCES tickets(id_ticket)

                    )
                """
            )
            conexion.commit()
            conexion.close()

    def borrar_Tabla(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    TRUNCATE TABLE tickets
                """
            )
            conexion.commit()
            conexion.close()
    def crearTabla_Usuarios():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE usuarios (
                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                        empleado_id INTEGER NOT NULL , 
                        password TEXT NOT NULL,
                        FOREIGN KEY (empleado_id) REFERENCES empleados(id_empleado)
 
                    )
                """
            )
            conexion.commit()
            conexion.close()

    def crearTabla_Empleados(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE empleados (
                        id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        puesto INTEGER NOT NULL,
                        direccion TEXT NOT NULL,
                        telefono TEXT UNIQUE NOT NULL,
                        correo text UNIQUE NOT NULL,
                        FOREIGN KEY (puesto) REFERENCES puestos(id_puesto)
                    )
                """
            )
            conexion.commit()
            conexion.close()

    def crearTabla_Departamentos():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE departamentos (
                        id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL
                    )
                """
            )
            conexion.commit()
            conexion.close()

    def crearTabla_Puestos(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE puestos (
                        id_puesto INTEGER PRIMARY KEY AUTOINCREMENT,
                        descripcion TEXT NOT NULL,
                        departamento_id INTEGER NOT NULL,
                        FOREIGN KEY (departamento_id) REFERENCES departamentos(id_departamento)
                    )
                """
            )
            conexion.commit()
            conexion.close()
    
    def renombrarTabla(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            instruccion= ("ALTER TABLE tickets RENAME TO old_tickets")
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()

    def crearTabla_Tickets(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    CREATE TABLE tickets (
                        id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_empleado INTEGER NOT NULL,
                        asunto INTEGER NOT NULL,
                        descripcion TEXT NOT NULL,
                        status INTEGER NOT NULL,
                        fecha_creacion TEXT NOT NULL,
                        FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
                        FOREIGN KEY (asunto) REFERENCES asuntos(id_asunto)
                    )
                """
            )
            cursor.execute("INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion) SELECT id_empleado, asunto, descripcion, status, fecha_creacion FROM old_tickets")
            conexion.commit()
            conexion.close()
        
        
    def crearRegistros(self):
            departamentos = [("Recursos Humanos",), ("Finanzas",), ("Marketing",),
                            ("Ventas",),("Tecnología",),("Logística",),
                            ("Producción",),("Calidad",),("Investigación y Desarrollo",),
                            ("Atención al Cliente",),("Compras",),("Legal",),
                            ("Sistemas",),("Comunicación",),("Administración",),]

            puestos= [('Gerente de RRHH', 1),('Especialista en Reclutamiento', 1),('Analista de Nóminas', 1),
                      ('Contador General', 2),('Analista Financiero', 2),('Tesorero', 2),
                      ('Gerente de Marketing', 3),('Especialista en Marketing Digital', 3),('Diseñador Gráfico', 3),
                      ('Gerente de Ventas', 4),('Ejecutivo de Cuentas', 4),('Representante de Ventas Internas', 4),
                      ('Desarrollador de Software', 5),('Ingeniero de Soporte Técnico', 5),('Administrador de Bases de Datos', 5),
                      ('Gerente de Logística', 6),('Coordinador de Almacén', 6),('Planificador de Rutas', 6),
                      ('Gerente de Producción', 7),('Supervisor de Línea', 7),('Operador de Maquinaria', 7),
                      ('Gerente de Calidad', 8),('Inspector de Control de Calidad', 8),('Analista de Procesos', 8),
                      ('Científico de I+D', 9),('Ingeniero de Producto', 9),('Técnico de Laboratorio', 9),
                      ('Gerente de Atención al Cliente', 10),('Agente de Soporte', 10),('Especialista en Experiencia del Cliente', 10),
                      ('Gerente de Compras', 11),('Analista de Abastecimiento', 11),('Comprador Junior', 11),
                      ('Asesor Jurídico', 12),('Paralegal', 12),('Especialista en Cumplimiento Normativo', 12),
                      ('Administrador de Sistemas', 13),('Ingeniero de Redes', 13),('Analista de Seguridad Informática', 13),
                      ('Gerente de Comunicaciones', 14),('Especialista en Relaciones Públicas', 14),('Redactor de Contenidos', 14),
                    ('Gerente Administrativo', 15),('Asistente Administrativo', 15),('Recepcionista', 15)]
            
            asuntos= [(13, "Actualización de Software"), (13, "Solicitud de Acceso a Servidor"), (13, "Incidente de Seguridad"), (13, "Backup de Datos"), (13, "Configuración de Red"), (13, "Error en Aplicación Interna"), (13, "Mantenimiento Programado"), (13, "Solicitud de Nueva Cuenta"), (13, "Problemas con VPN"), (13, "Reporte de Caída del Sistema"), (13, "Configuración de Correo Electrónico"), (13, "Instalación de Antivirus"), (13, "Solicitud de Hardware"), (13, "Optimización de Base de Datos"),]
            tickets= [(1,2,'Laptop No Enciende, Ni Carga',0,'28/05/25', '29/05/25')]

            tickets_rechazados= [(3,'Ticket Repetido')]

            tickets_aceptados=[(1,11,"Resuelto","29/05/25","30/05/2025")]

            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            #cursor.executemany("INSERT INTO departamentos (nombre) VALUES (?)", departamentos)
            #cursor.executemany("INSERT INTO puestos (descripcion, departamento_id) VALUES (?, ?)", puestos)
            #cursor.executemany("INSERT INTO empleados (nombre, puesto, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?)", empleados)
            #cursor.executemany("INSERT INTO asuntos (departamento, titulo) VALUES (?, ?)", asuntos)
            #cursor.execute("SELECT id_ticket, fecha_creacion FROM tickets WHERE status=2")
            cursor.execute("SELECT * FROM ticketaceptado")
            #cursor.execute("SELECT asuntos.id_asunto, departamentos.nombre, asuntos.titulo FROM asuntos INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento")
            #cursor.execute("SELECT asuntos.titulo, departamentos.nombre FROM asuntos INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento")
            datos=cursor.fetchall()
            for i in datos:
                   print(i)
            #cursor.executemany("INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion, fecha_respuesta) VALUES (?, ?, ?, ?, ?, ?)", tickets)
            #cursor.executemany("INSERT INTO empleados (nombre, puesto, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?)", empleado)
            #cursor.executemany("INSERT INTO ticketaceptado (ticket, empleado, situacion, fecha_resolucion, fecha_caducidad) VALUES (?, ?, ?, ?, ?)", tickets_aceptados)
            #cursor.executemany("INSERT INTO tickets_rechazados (id_ticket, motivo) VALUES (?, ?)", tickets_rechazados)
            #conexion.commit()
            conexion.close()

    def consultar_empleados(self):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT empleados.id_empleado, empleados.nombre , puestos.descripcion, empleados.direccion, empleados.telefono, empleados.correo FROM empleados INNER JOIN puestos ON puestos.id_puesto = empleados.puesto")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
            print(i)

    def revisar_tickets_enviados(self,empleado):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute(f"SELECT tickets.id_ticket, asuntos.titulo, tickets.descripcion, tickets.status, tickets.fecha_creacion FROM tickets INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto WHERE tickets.id_empleado='{empleado}'")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)
           
    def consultar_tickets_all(self):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT tickets.id_ticket, empleados.nombre, asuntos.titulo, tickets.descripcion, tickets.status, tickets.fecha_creacion FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def consultar_tickets_pendientes(self):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT tickets.id_ticket, empleados.nombre, asuntos.titulo, tickets.descripcion, tickets.status, tickets.fecha_creacion FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto WHERE status=2")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def consultar_tickets_rechazados(self):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT tickets.id_ticket, tickets.descripcion, tickets_rechazados.motivo, tickets.fecha_creacion, tickets_rechazados.fecha_respuesta FROM tickets_rechazados INNER JOIN tickets ON tickets.id_ticket = tickets_rechazados.id_ticket")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def consultar_tickets_aceptados(self):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        #cursor.execute("SELECT * FROM ticketaceptado")
        cursor.execute("SELECT tickets.id_ticket, tickets.descripcion, empleados.nombre, ticketaceptado.situacion,ticketaceptado.fecha_solucion ,tickets.fecha_creacion, ticketaceptado.fecha_respuesta, ticketaceptado.fecha_caducidad FROM ticketaceptado INNER JOIN empleados ON empleados.id_empleado= ticketaceptado.empleado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def insertar_ticket(self,id_empleado,asunto,descripcion,status,fecha_creacion):
            ticket=[(id_empleado,asunto,descripcion,status,fecha_creacion)]
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.executemany(f"INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion) VALUES (?, ?, ?, ?, ?)", ticket)
            conexion.commit()
            conexion.close()

    def aceptar_ticket(self,ticket,empleado,stiuacion,fecha_respuesta,fecha_resolucion,fecha_caducidad):
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute(f"INSERT INTO ticketaceptado (ticket, empleado, situacion,fecha_respuesta ,fecha_solucion, fecha_caducidad) VALUES ('{ticket}', '{empleado}', '{stiuacion}', '{fecha_respuesta}','{fecha_resolucion}', '{fecha_caducidad}')")
            conexion.commit()
            conexion.close()

    def rechazar_ticket(self,ticket,motivo,fecha_respuesta):
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute(f"INSERT INTO tickets_rechazados (id_ticket, motivo,fecha_respuesta) VALUES ('{ticket}', '{motivo}','{fecha_respuesta}')")
            conexion.commit()
            conexion.close()

    def consultar_empleado_depto(self,departamento):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           cursor.execute(f"SELECT empleados.id_empleado, empleados.nombre,puestos.descripcion, empleados.direccion, empleados.telefono, empleados.correo FROM empleados INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id WHERE departamentos.nombre= '{departamento}'")
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
            print(i[0],i[1],i[2])

    def modificar(self):
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute(f"UPDATE tickets_rechazados SET fecha_respuesta='2023-10-31' WHERE id_ticket=43")
            conexion.commit()
            conexion.close()

    def registrar_empleado(self,nombre, puesto, direccion, telefono, correo):
           empleado= [(nombre, puesto, direccion, telefono, correo)]
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           cursor.executemany("INSERT INTO empleados (nombre, puesto, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?)", empleado)
           conexion.commit()
           conexion.close()

    def filtrar_situacion(self,situacion):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           #instruccion=  f"SELECT departamentos.nombre FROM ticketaceptado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id WHERE ticketaceptado.situacion= '{situacion}'"
           instruccion=  f"SELECT ticketaceptado.fecha_respuesta, departamentos.nombre, asuntos.titulo, tickets.descripcion FROM ticketaceptado INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto WHERE ticketaceptado.situacion= '{situacion}'"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def filtrar_departamentoorigen(self,depto_origen):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT departamentos.nombre, asuntos.titulo, tickets.descripcion, ticketaceptado.fecha_respuesta, tickets.id_empleado, ticketaceptado.empleado, ticketaceptado.situacion FROM ticketaceptado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  if (i[0]==depto_origen):
                    print(i)

    def filtrar_departamentoorigen_rechazado(self,depto_origen):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT departamentos.nombre, asuntos.titulo, tickets.descripcion, tickets_rechazados.fecha_respuesta, tickets_rechazados.motivo FROM tickets_rechazados INNER JOIN tickets ON tickets.id_ticket = tickets_rechazados.id_ticket INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  if (i[0]==depto_origen):
                    print(i)

    def filtrar_departamentodestinado_rechazado(self,depto_destino):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT departamentos.nombre, asuntos.titulo, tickets.descripcion, tickets_rechazados.fecha_respuesta, tickets_rechazados.motivo FROM tickets_rechazados INNER JOIN tickets ON tickets.id_ticket = tickets_rechazados.id_ticket INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           print(datos)
           conexion.close()
           for i in datos:
                  conexion= sql.connect("BD_MesadeAyuda.db")
                  cursor= conexion.cursor()
                  instruccion= f"SELECT departamentos.nombre FROM asuntos INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento WHERE asuntos.titulo='{i[1]}'"
                  cursor.execute(instruccion)
                  datos= cursor.fetchall()
                  conexion.close()
                  for e in datos:
                         if(e[0]==depto_destino):
                                print(i)

        
    def filtrar_departamentodestinado(self,depto_destino):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT departamentos.nombre, asuntos.titulo, tickets.descripcion, ticketaceptado.fecha_respuesta, tickets.id_empleado, ticketaceptado.empleado, ticketaceptado.situacion FROM ticketaceptado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  conexion= sql.connect("BD_MesadeAyuda.db")
                  cursor= conexion.cursor()
                  instruccion= f"SELECT departamentos.nombre FROM asuntos INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento WHERE asuntos.titulo='{i[1]}'"
                  cursor.execute(instruccion)
                  datos= cursor.fetchall()
                  conexion.close()
                  for e in datos:
                         if(e[0]==depto_destino):
                                print(i)

    def tickets_diarios(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT fecha_creacion, departamentos.nombre, COUNT(*) as total FROM tickets INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento GROUP BY fecha_creacion, departamentos.nombre ORDER BY fecha_creacion;"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def filtro_tickets_diarios_deptos_origen(self,mes,year):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT fecha_creacion,departamentos.nombre, COUNT(*) as total FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id WHERE strftime('%m', fecha_creacion) = '{mes}' AND strftime('%Y', fecha_creacion) = '{year}' GROUP BY fecha_creacion, departamentos.nombre ORDER BY fecha_creacion,departamentos.nombre;"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def tickets_diarios_deptos_destinados(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT fecha_creacion,departamentos.nombre , COUNT(*) as total FROM tickets INNER JOIN asuntos ON asuntos.id_asunto=tickets.asunto INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento GROUP BY fecha_creacion, departamentos.nombre ORDER BY fecha_creacion,departamentos.nombre;"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def filtro_tickets_diarios_deptos_destinados(self,mes,year):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT fecha_creacion,departamentos.nombre , COUNT(*) as total FROM tickets INNER JOIN asuntos ON asuntos.id_asunto=tickets.asunto INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento WHERE strftime('%m', fecha_creacion) = '{mes}' AND strftime('%Y', fecha_creacion) = '{year}' GROUP BY fecha_creacion, departamentos.nombre ORDER BY fecha_creacion,departamentos.nombre;"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def tickets_mesuales_origen(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT CASE strftime('%m', fecha_creacion) WHEN '01' THEN 'Enero' WHEN '02' THEN 'Febrero' WHEN '03' THEN 'Marzo' WHEN '04' THEN 'Abril' WHEN '05' THEN 'Mayo' WHEN '06' THEN 'Junio' WHEN '07' THEN 'Julio' WHEN '08' THEN 'Agosto' WHEN '09' THEN 'Septiembre' WHEN '10' THEN 'Octubre' WHEN '11' THEN 'Noviembre' WHEN '12' THEN 'Diciembre' END,strftime('%Y', fecha_creacion) ,departamentos.nombre, COUNT(*) as total FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN puestos ON puestos.id_puesto = empleados.puesto INNER JOIN departamentos ON departamentos.id_departamento = puestos.departamento_id GROUP BY strftime('%m', fecha_creacion), strftime('%Y', fecha_creacion), departamentos.nombre ORDER BY fecha_creacion,departamentos.nombre;"
           cursor.execute(instruccion)
           conexion.commit()
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)
    
    def tickets_mensuales_destino(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT CASE strftime('%m',fecha_creacion) WHEN '01' THEN 'Enero' WHEN '02' THEN 'Febrero' WHEN '03' THEN 'Marzo' WHEN '04' THEN 'Abril' WHEN '05' THEN 'Mayo' WHEN '06' THEN 'Junio' WHEN '07' THEN 'Julio' WHEN '08' THEN 'Agosto' WHEN '09' THEN 'Septiembre' WHEN '10' THEN 'Octubre' WHEN '11' THEN 'Noviembre' WHEN '12' THEN 'Diciembre' END, strftime('%Y',fecha_creacion),departamentos.nombre , COUNT(*) as total FROM tickets INNER JOIN asuntos ON asuntos.id_asunto=tickets.asunto INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento GROUP BY strftime('%m',fecha_creacion), departamentos.nombre ORDER BY fecha_creacion,departamentos.nombre;"
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  print(i)

    def borrar_datos(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           cursor.execute("DELETE FROM tickets")
           cursor.execute("DELETE FROM sqlite_sequence WHERE name='tickets'")
           conexion.commit()
           conexion.close()

    def tickets_cad(self, fecha_inicio, fecha_final):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           cursor.execute("SELECT tickets.id_ticket, tickets.descripcion, empleados.nombre, ticketaceptado.situacion,ticketaceptado.fecha_solucion ,tickets.fecha_creacion, ticketaceptado.fecha_respuesta, ticketaceptado.fecha_caducidad FROM ticketaceptado INNER JOIN empleados ON empleados.id_empleado= ticketaceptado.empleado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket")
           datos= cursor.fetchall()
           conexion.close()
           for i in datos:
                  solucion= i[4]
                  caducidad= i[7]
                  if solucion!="------" and caducidad!="------":
                    solucion_date= datetime.strptime(solucion, '%Y-%m-%d')
                    caducidad_date= datetime.strptime(caducidad, '%Y-%m-%d')
                    if caducidad_date < solucion_date:
                            if caducidad_date > datetime.strptime(fecha_inicio, '%Y-%m-%d') and caducidad_date < datetime.strptime(fecha_final, '%Y-%m-%d'):
                                print(i)

    def tiempo_tickets(self,departamento, fecha_inicio, fecha_final):
           conexion= sql.connect("BD_MesadeAyuda.db")
           cursor= conexion.cursor()
           instruccion= f"SELECT departamentos.nombre, ticketaceptado.fecha_respuesta, ticketaceptado.fecha_solucion FROM ticketaceptado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket INNER JOIN asuntos ON asuntos.id_asunto=tickets.asunto INNER JOIN departamentos ON departamentos.id_departamento = asuntos.departamento WHERE departamentos.nombre= '{departamento}' "
           cursor.execute(instruccion)
           datos= cursor.fetchall()
           conexion.close()
           tiemporespuesta=0
           resueltos= 0
           for i in datos:
                  respuesta= i[1]
                  solucion= i[2]
                  if respuesta!="------" and solucion!="------":
                    respuesta= datetime.strptime(respuesta, '%Y-%m-%d')
                    solucion= datetime.strptime(solucion, '%Y-%m-%d')
                    if solucion > datetime.strptime(fecha_inicio, '%Y-%m-%d') and solucion < datetime.strptime(fecha_final, '%Y-%m-%d'):
                        tiemporespuesta+= (solucion-respuesta).total_seconds() / 60  
                        resueltos+=1
           print("Total del Tiempo de Respuesta: ", tiemporespuesta, " Minutos")  
           print("Total de Tickets Resueltos: ", resueltos)
           promedio= round(tiemporespuesta / resueltos)
           print("Promedio de Tiempo de Respuesta:")
           print(promedio, "Minutos")
                  
    def exportarTabla(self):
           conexion= sql.connect("BD_MesadeAyuda.db")
           instuccion= "SELECT tickets.id_ticket, tickets.descripcion, tickets_rechazados.motivo, tickets.fecha_creacion, tickets_rechazados.fecha_respuesta FROM tickets_rechazados INNER JOIN tickets ON tickets.id_ticket = tickets_rechazados.id_ticket"
           df= pd.read_sql_query(instuccion,conexion)
           df.to_excel('Tickets_Rechazados.xlsx',index=False)
           
    def selectTicketsAdministrar(self,id_empleado):
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT A.id_ticket, A.Descripcion, D.nombre as empleado, C.nombre, B.titulo, A.fecha_creacion
            FROM tickets A 
            INNER JOIN asuntos B ON A.asunto = B.id_asunto 
            INNER JOIN departamentos C ON B.departamento = C.id_departamento
            INNER JOIN empleados D ON A.id_empleado = D.id_empleado 
            WHERE A.Status =2 and A.id_empleado=?""",[id_empleado])
        columnas = [desc[0] for desc in cursor.description]
        resultado = cursor.fetchall()
        resultado_json = [dict(zip(columnas, fila)) for fila in resultado]
        print(resultado_json)
        return json.dumps(resultado_json, ensure_ascii=False)  
        

    #insertar_ticket(3,1,"Olvide la Contraseña de Intranet",1,"05/06/25")
    #insertar_ticket(7,1,"Las impresiones se quedan en espera",1,"2025-06-18")
    #insertar_ticket(5,2,"Cambio de Tóner",0,"05/06/25")
    #aceptar_ticket(1,11,"Resuelto","05/06/25","05/06/25","06/06/25")
    #rechazar_ticket(2,"Se llamara a proveedor","12/06/25")
    #consultar_empleados()
    #consultar_tickets_all()
    #consultar_tickets_rechazados()
    #consultar_tickets_aceptados()