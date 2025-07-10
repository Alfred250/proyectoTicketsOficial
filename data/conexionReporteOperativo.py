from MdeAyuda import Base


class ReporteOperativo:
    
    def filtroTicketsDiarios(self,fecha):
        baseDatos= Base()
        resultado=baseDatos.tickets_diarios(fecha)
        print("resultado de los diario",resultado)
        return resultado

    def filtroTicketsMensualDepartamento(self,mes,anio):
        baseDatos= Base()
        return baseDatos.filtro_tickets_diarios_deptos_origen(mes,anio)
    
    def filtroTicketsCaducados(self,fecha_inicio,fecha_fin):
        baseDatos=Base()
        return baseDatos.tickets_cad(fecha_inicio,fecha_fin)
    
    def filtroTiempoRespuesta(self,departamento,fecha_inicio,fecha_fin):
        baseDatos= Base()
        return baseDatos.tiempo_tickets(departamento,fecha_inicio,fecha_fin)