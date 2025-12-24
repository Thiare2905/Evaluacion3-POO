from abc import ABC, abstractmethod

# Clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, patente, tipo):
        self.__patente = patente
        self.__tipo = tipo

    # Método abstracto para calcular el cobro de la estadía
    @abstractmethod
    def calcular_cobro(self):
        pass
    
    # Getters
    def get_patente(self):
        return self.__patente
    
    def get_tipo(self):
        return self.__tipo