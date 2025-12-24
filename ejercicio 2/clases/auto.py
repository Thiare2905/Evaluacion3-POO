from clases.vehiculo import Vehiculo
import math 

TARIFA_AUTO = 1500 # Tarifa por hora para autos

# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, patente, tipo = "Auto"):
        super().__init__(patente, tipo)

    # Método para calcular el cobro de la estadía
    def calcular_cobro(self, entrada, salida):
        minutos = (salida - entrada).total_seconds() / 60 # Calcular minutos de estadía
        horas = math.ceil(minutos / 60) # Redondear hacia arriba a la hora más cerca
        return horas * TARIFA_AUTO # Calcular cobro sin recargo
