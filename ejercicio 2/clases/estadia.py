from datetime import datetime, time

RECARGO_HORA_PUNTA = 0.30       # Recargo del 30% en hora punta
HORA_PUNTA_INICIO = time(18, 0) # 18:00 horas
HORA_PUNTA_FIN = time(22, 0)    # 22:00 horas

# Clase Estadia para representar una estadía de un vehículo
class Estadia:
    def __init__(self, vehiculo, hora_entrada, hora_salida):
        self.__vehiculo = vehiculo # Vehículo asociado a la estadía
        self.__hora_entrada = datetime.strptime(hora_entrada, "%H:%M") # Hora de entrada como objeto datetime
        self.__hora_salida = datetime.strptime(hora_salida, "%H:%M") # Hora de salida como objeto datetime

    # Método para ver si la estadía fue en hora punta
    def hora_punta(self):
        if self.__hora_entrada.time() < HORA_PUNTA_FIN and self.__hora_salida.time() > HORA_PUNTA_INICIO:
            return True
    
    # Getters
    def get_vehiculo(self):
        return self.__vehiculo
    
    def get_hora_entrada(self):
        return self.__hora_entrada
    
    def get_hora_salida(self):
        return self.__hora_salida