from clases.sensor import Sensor

# Clase Sensor_Humedad que hereda de Sensor
class Sensor_Humedad(Sensor):
    def __init__(self, id_sensor, humedad):
        super().__init__(id_sensor)
        self.__humedad = humedad # Humedad en porcentaje

    # Método para leer el sensor y validar la humedad
    def leer_sensor(self):
        if 0 <= self.__humedad <= 100:
            return True
    
    # Método para obtener la descripción del sensor
    def descripcion(self):
        if not self.leer_sensor():
            return f"Sensor de Humedad -> Humedad: Fuera de rango ({self.__humedad})."
        return f"N°{self.get_id()} Sensor de Humedad -> Humedad: {self.__humedad}"

    # Método para obtener la humedad
    def get_humedad(self):
        return self.__humedad
