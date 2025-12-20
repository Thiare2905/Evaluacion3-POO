from clases.notificacion import Notificacion
import re

MAX_LARGO_TELF = 160 # Máximo largo del mensaje para teléfono
COSTO_CHAR = 25     # Costo por cada caracter

# Clase para notificaciones por teléfono
class Notif_Telefono(Notificacion):
    # Método para validar el formato del número de teléfono
    def validar_destino(self, destino):
        patron = r'^(\+56)?9\d{8}$'
        destino = self.get_destino()
        if re.match(patron, destino):
            return True
        return False

    # Método para calcular el costo total de la notificación
    def costo_total(self):
        return len(self.get_mensaje().strip()) * COSTO_CHAR
    
    # Método para enviar el mensaje
    def enviar_mensaje(self):
        if not self.validar_destino(self.get_destino()):
            self.suma_fallo()
            return f"El número de teléfono es invalido ({self.get_destino()})."
        print(super().validar_mensaje(MAX_LARGO_TELF))
    
