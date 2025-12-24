from clases.vehiculo import Vehiculo
import math 

TARIFA_MOTO = 700 # Tarifa por hora para motos

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, patente, tipo = "Moto"):
        super().__init__(patente, tipo)

    # Método para calcular el cobro de la estadía
    def calcular_cobro(self, entrada, salida):
        minutos = (salida - entrada).total_seconds() / 60 # Calcular minutos de estadía
        # Aplicar tarifa media hora si es menos de 30 minutos
        if minutos <= 30:
            horas = 0.5
        else:
            horas = math.ceil(minutos / 60) # Redondear hacia arriba a la hora más cerca
        return horas * TARIFA_MOTO # Calcular cobro sin recargo