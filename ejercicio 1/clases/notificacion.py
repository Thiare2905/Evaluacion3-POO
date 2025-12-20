from abc import ABC, abstractmethod

# Clase abstracta para notificaciones base
class Notificacion(ABC):
    def __init__(self, destino, mensaje):
        self.__destino = destino
        self.__mensaje = mensaje
        self.__exitos = 0
        self.__fallos = 0

    # Método abstracto para calcular el costo total de la notificación
    @abstractmethod
    def costo_total(self):
        pass

    # Método abstracto para enviar el mensaje
    @abstractmethod
    def enviar_mensaje(self):
        pass

    # Método abstracto para validar el destino
    @abstractmethod
    def validar_destino(self, destino):
        pass

    # Método para validar el mensaje
    def validar_mensaje(self, MAX_LARGO):
        if self.__mensaje.strip() == "":
            self.__fallos += 1
            return "El mensaje no puede estar vacio."
        if len(self.__mensaje.strip()) > MAX_LARGO:
            self.__fallos += 1
            return "El mensaje excede el largo maximo."
        self.__exitos += 1
        return f"Se envio con exito la notificación a {self.__destino}."

    # Método para incrementar el contador de fallos
    def suma_fallo(self):
        self.__fallos += 1
    
    # Getters
    def get_destino(self):
        return self.__destino
    
    def get_mensaje(self):
        return self.__mensaje
    
    def get_fallos(self):
        return self.__fallos
    
    def get_exitos(self):
        return self.__exitos