from clases.vehiculo import Vehiculo
import math

RECARGO_FIJO = 0.20  # Recargo fijo del 20% para camiones
TARIFA_CAMION = 2500 # Tarifa por hora para camiones

# Clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, patente, tipo = "Camion"):
        super().__init__(patente, tipo)

    # Método para calcular el cobro de la estadía
    def calcular_cobro(self, entrada, salida):
        minutos = (salida - entrada).total_seconds() / 60 # Calcular minutos de estadía
        horas = math.ceil(minutos / 60) # Redondear hacia arriba a la hora más cerca
        return (horas * TARIFA_CAMION) * RECARGO_FIJO # Aplicar recargo fijo