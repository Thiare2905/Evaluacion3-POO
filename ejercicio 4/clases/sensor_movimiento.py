from clases.sensor import Sensor

UMBRAL_DETECCION = 0.7 # Umbral para detectar movimiento

# Clase Sensor_Movimiento que hereda de Sensor
class Sensor_Movimiento(Sensor):
    def __init__(self, id_sensor, movimiento):
        super().__init__(id_sensor)
        self.__movimiento = movimiento # Valor de movimiento

    # Método para leer el sensor y validar el movimiento
    def leer_sensor(self):
        if self.__movimiento >= UMBRAL_DETECCION:
            return True
    
    # Método para obtener la descripción del sensor
    def descripcion(self):
        if not self.leer_sensor():
            return f"Sensor de Movimiento -> Movimiento: No detectado ({self.__movimiento})."
        return f"N°{self.get_id()} Sensor de Movimiento -> Movimiento: Detectado ({self.__movimiento})"
    
    # Método para obtener el movimiento
    def get_movimiento(self):
        return self.__movimiento