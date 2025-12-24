from clases.estadia import Estadia
import heapq

# Clase Estacionamiento para gestionar estadías
class Estacionamiento:
    def __init__(self):
        self.__estadias = [] # Lista privada para almacenar estadías

    # Método para registrar una nueva estadía
    def registrar_estadia(self, estadia:Estadia):
        # Verificar si la estadía ya está registrada
        for e in self.__estadias:
            if e.get_vehiculo().get_patente() == estadia.get_vehiculo().get_patente() and e.get_hora_entrada() == estadia.get_hora_entrada():
                return "Ya está registrado."
        # Registrar la nueva estadía
        self.__estadias.append(estadia)
        return f"Estadia registrada."

    # Método para generar un reporte de las estadías
    def reporte(self):
        total = 0
        tipo_auto = 0
        tipo_moto = 0
        tipo_camion = 0
        cobros = []

        # Calcular totales y conteos
        for e in self.__estadias:
            tipo = e.get_vehiculo().get_tipo()
            if tipo == "Auto":
                tipo_auto += 1
            elif tipo == "Moto":
                tipo_moto += 1
            elif tipo == "Camion":
                tipo_camion += 1
            # Calcular cobro de la estadía
            cobro = e.get_vehiculo().calcular_cobro(e.get_hora_entrada(), e.get_hora_salida()) 
            total += cobro
            cobros.append(cobro)
        
        top_3 = sorted(cobros, reverse=True)[:3] # Obtener los tres cobros más altos
        print(" - - - R E P O R T E - - -")
        print(f"Total recaudado: ${total}")
        print("-- Top 3 cobros más altos:")
        # Imprimir los tres cobros más altos
        for i, monto in enumerate(top_3, start=1):
            print(f"{i}. ${monto}")
        print("-- Cantidad de vehículos por tipo:")
        print(f"Auto: {tipo_auto} - Moto: {tipo_moto} - Camion: {tipo_camion}")
