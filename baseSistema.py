import sqlite3 as sql

class BaseDatos:
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

    def borrar_Tabla():
            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            cursor.execute(
                #docString
                """ 
                    DROP TABLE tickets
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

    def crearTabla_Empleados():
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

    def crearTabla_Puestos():
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

    def crearTabla_Tickets():
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
                        FOREIGN KEY (id_empleado) REFERENCES departamentos(id_departamento)
                        FOREIGN KEY (asunto) REFERENCES asuntos(id_asunto)

                    )
                """
            )
            conexion.commit()
            conexion.close()
        
        
    def crearRegistros():
            departamentos = [("Recursos Humanos",), ("Finanzas",), ("Marketing",),
                            ("Ventas",),("Tecnología",),("Logística",),
                            ("Producción",),("Calidad",),("Investigación y Desarrollo",),
                            ("Atención al Cliente",),("Compras",),("Legal",),
                            ("Sistemas",),("Comunicación",),("Administración",),]

            puestos= [("Gerente de RR.HH",1),
                    ("Asistente de RR.HH",1),

                    ("Contador Senior",2),
                    ("Analista Financiero",2),

                    ("Especialista en Publicidad",3),
                    ("Diseñador Gráfico",3),

                    ("Ejecutivo de Ventas",4),
                    ("Representante Comercial",4),

                    ("Desarrollador Backend",5),
                    ("Administrador de Bases de Datos",5),

                    ("Coordinador de Logística",6),
                    ("Operador de Inventario",6),

                    ("Supervisor de Producción",7),
                    ("Técnico de Mantenimiento",7),

                    ("Insepector de Calidad",8),
                    ("Analista de Calidad",8),

                    ("Investigador de Mercado",9),
                    ("Científico de Datos",9),

                    ("Representante de Atención",10),
                    ("Supervisor de Call Center",10),

                    ("Encargado de Compras",11),

                    ("Asesor Legal",12),

                    ("Administrador de Sistemas",13),

                    ("Especialista en Comunicación",14),

                    ("Administrador General",15),
                    ]
            
            empleados= [('Carlos Ramírez', 3, 'Av. Reforma 123, CDMX', '5551234567', 'carlos.ramirez@email.com'),
                        ('Laura González', 7, 'Calle 8 #45, Guadalajara', '3339876543', 'laura.gonzalez@email.com'),
                        ('Jorge Martínez', 1, 'Blvd. Atlixco 567, Puebla', '2225556677', 'jorge.martinez@email.com'),
                        ('Ana Torres', 5, 'Carr. Nacional 900, Monterrey', '8181122334', 'ana.torres@email.com'),
                        ('Roberto Díaz', 12, 'Av. Las Torres 150, Toluca', '7224432111', 'roberto.diaz@email.com'),
                        ('María López', 8, 'Calle Hidalgo 234, León', '4777766554', 'maria.lopez@email.com'),
                        ('Daniela Herrera', 4, 'Paseo del Norte 321, Tijuana', '6643342211', 'daniela.herrera@email.com'),
                        ('Luis Fernández', 10, 'Calzada del Sol 98, Mérida', '9994455667', 'luis.fernandez@email.com'),
                        ('Elena Vargas', 15, 'Camino Real 456, Querétaro', '4427788990', 'elena.vargas@email.com'),
                        ('Fernando Ríos', 2, 'Av. Universidad 1010, Aguascalientes', '4493322110', 'fernando.rios@email.com')]
            
            asuntos= [(13,"Reestablecer Contraseña"), (13,"Problema con Equipo"), (11,"Cotización"), (5,"Consulta") ]
            tickets= [(1,2,'Laptop No Enciende, Ni Carga',0,'28/05/25', '29/05/25')]

            tickets_rechazados= [(3,'Ticket Repetido')]

            empleado= [('Ulises Guerrero', 13, 'Blvd. Saturno 1010, León', '4779097173', 'Uligu@gmail.com')]
            tickets_aceptados=[(1,11,"Resuelto","29/05/25","30/05/2025")]

            conexion= sql.connect("BD_MesadeAyuda.db")
            #Manipular una Tabla
            cursor= conexion.cursor()
            #cursor.executemany("INSERT INTO departamentos (nombre) VALUES (?)", departamentos)
            #cursor.executemany("INSERT INTO puestos (descripcion, departamento_id) VALUES (?, ?)", puestos)
            #cursor.executemany("INSERT INTO empleados (nombre, puesto, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?)", empleados)
            #cursor.executemany("INSERT INTO asuntos (departamento, titulo) VALUES (?, ?)", asuntos)
            #cursor.executemany("INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion, fecha_respuesta) VALUES (?, ?, ?, ?, ?, ?)", tickets)
            #cursor.executemany("INSERT INTO empleados (nombre, puesto, direccion, telefono, correo) VALUES (?, ?, ?, ?, ?)", empleado)
            cursor.executemany("INSERT INTO ticketaceptado (ticket, empleado, situacion, fecha_solucion, fecha_caducidad) VALUES (?, ?, ?, ?, ?)", tickets_aceptados)
            #cursor.executemany("INSERT INTO tickets_rechazados (id_ticket, motivo) VALUES (?, ?)", tickets_rechazados)
            conexion.commit()
            conexion.close()

    def leer():
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute("SELECT * FROM tickets_rechazados")
            #cursor.execute("SELECT tickets.id_ticket, empleados.nombre, asuntos.titulo, tickets.descripcion, tickets.status, tickets.fecha_creacion, fecha_respuesta FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto")
            #cursor.execute("SELECT asuntos.id_asunto, departamentos.nombre, asuntos.titulo FROM asuntos INNER JOIN departamentos ON id_departamento = asuntos.departamento")
            #cursor.execute("SELECT empleados.id_empleado, empleados.nombre , puestos.descripcion, empleados.direccion, empleados.telefono, empleados.correo FROM empleados INNER JOIN puestos ON puestos.id_puesto = empleados.puesto")
            datos= cursor.fetchall()
            conexion.close()
            for i in datos:
                print(i)

    def consultar_empleados():
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT empleados.id_empleado, empleados.nombre , puestos.descripcion, empleados.direccion, empleados.telefono, empleados.correo FROM empleados INNER JOIN puestos ON puestos.id_puesto = empleados.puesto")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
            print(i)

    def consultar_tickets_all():
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT tickets.id_ticket, empleados.nombre, asuntos.titulo, tickets.descripcion, tickets.status, tickets.fecha_creacion FROM tickets INNER JOIN empleados ON empleados.id_empleado = tickets.id_empleado INNER JOIN asuntos ON asuntos.id_asunto = tickets.asunto")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def consultar_tickets_rechazados():
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        cursor.execute("SELECT tickets.id_ticket, tickets.descripcion, tickets_rechazados.motivo, tickets.fecha_creacion, tickets_rechazados.fecha_respuesta FROM tickets_rechazados INNER JOIN tickets ON tickets.id_ticket = tickets_rechazados.id_ticket")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)

    def consultar_tickets_aceptados():
        conexion= sql.connect("BD_MesadeAyuda.db")
        cursor= conexion.cursor()
        #cursor.execute("SELECT * FROM ticketaceptado")
        cursor.execute("SELECT tickets.id_ticket, tickets.descripcion, empleados.nombre, ticketaceptado.situacion,ticketaceptado.fecha_solucion ,tickets.fecha_creacion, ticketaceptado.fecha_respuesta, ticketaceptado.fecha_caducidad FROM ticketaceptado INNER JOIN empleados ON empleados.id_empleado= ticketaceptado.empleado INNER JOIN tickets ON tickets.id_ticket = ticketaceptado.ticket")
        datos= cursor.fetchall()
        conexion.close()
        for i in datos:
                print(i)
        print(datos)

    def insertar_ticket(id_empleado,asunto,descripcion,status,fecha_creacion):
            ticket=[(id_empleado,asunto,descripcion,status,fecha_creacion)]
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.executemany(f"INSERT INTO tickets (id_empleado, asunto, descripcion, status, fecha_creacion) VALUES (?, ?, ?, ?, ?)", ticket)
            conexion.commit()
            conexion.close()

    def aceptar_ticket(ticket,empleado,stiuacion,fecha_respuesta,fecha_resolucion,fecha_caducidad):
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute(f"INSERT INTO ticketaceptado (ticket, empleado, situacion,fecha_respuesta ,fecha_solucion, fecha_caducidad) VALUES ('{ticket}', '{empleado}', '{stiuacion}', '{fecha_respuesta}','{fecha_resolucion}', '{fecha_caducidad}')")
            conexion.commit()
            conexion.close()

    def rechazar_ticket(ticket,motivo,fecha_respuesta):
            conexion= sql.connect("BD_MesadeAyuda.db")
            cursor= conexion.cursor()
            cursor.execute(f"INSERT INTO tickets_rechazados (id_ticket, motivo,fecha_respuesta) VALUES ('{ticket}', '{motivo}','{fecha_respuesta}')")
            conexion.commit()
            conexion.close()

    #insertar_ticket(3,1,"Olvide la Contraseña de Intranet",1,"05/06/25")
    #insertar_ticket(5,2,"Cambio de Tóner",0,"05/06/25")
    #aceptar_ticket(1,13,"Resuelto","05/06/25","05/06/25","06/06/25")
    #rechazar_ticket(2,"Se llamara a proveedor","12/06/25")
    #consultar_empleados()
    #consultar_tickets_all()
    #consultar_tickets_rechazados()
    #consultar_tickets_aceptados()
    #crearBD()
    #crearTabla_Asuntos()
    #crearTabla_TicketsAceptados()
    #crearTabla_Departamentos()
    #crearTabla_Empleados()
    #crearTabla_Usuarios()
    #crearTabla_Tickets()
    #crearTabla_Puestos()
    #crearTabla_TicketsRechazados()
    
    
base= BaseDatos()
BaseDatos.insertar_ticket(1,3,"no carga el sistema",2,"21-06-2025")
