from abc import ABC, abstractmethod

# Clase abstracta Sensor
class Sensor(ABC):
    def __init__(self, id_sensor=1):
        self.__id_sensor = id_sensor # Identificador del sensor

    # Métodos abstractos que deben implementarse en las subclases
    @abstractmethod
    def leer_sensor(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    # Método para obtener el ID del sensor
    def get_id(self):
        return self.__id_sensor