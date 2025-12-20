from clases.notificacion import Notificacion

# Clase para gestionar múltiples notificaciones
class Gestion_Notif:
    def __init__(self):
        self.__destinos = []

    # Método para agregar un destino de notificación
    def agregar_destino(self, notificacion:Notificacion):
        for d in self.__destinos:
            if d.get_destino() == notificacion.get_destino(): # validar si el destino ya existe
                return ("Este destino ya existe.")
        self.__destinos.append(notificacion) # agregar destino a la lista
        return f"Se agregó ({notificacion.get_destino()})."
            
    # Método para mostrar un resumen de envíos
    def resumen(self):
        exitos = 0
        fallos = 0
        for d in self.__destinos:
            if d.get_fallos() == 0:
                print(f"{d.get_tipo()}: {d.get_destino()} -> costo: {d.costo_total()}")
            else:
                print(f"{d.get_tipo()}: {d.get_destino()} -> costo: 0 (fallido)")
            exitos += d.get_exitos()
            fallos += d.get_fallos()
        print(f"Envíos exitosos: {exitos}\n"
             f"Total de fallos: {fallos}")
    
    # Método para enviar notificaciones a todos los destinos registrados
    def enviar(self):
        for d in self.__destinos:
            d.enviar_mensaje()