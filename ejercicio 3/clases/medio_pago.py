from abc import ABC, abstractmethod

# Clase abstracta para representar un medio de pago
class Medio_Pago(ABC):
    def __init__(self, identificador, tipo):
        self.__identificador = identificador
        self.__tipo = tipo

    # Métodos abstractos que deben ser implementados por las subclases
    @abstractmethod
    def calcular_pago(self, monto):
        pass
    
    @abstractmethod
    def validar(self):
        pass

    # Método para obtener el tipo de medio de pago
    def get_tipo(self):
        return self.__tipo
    