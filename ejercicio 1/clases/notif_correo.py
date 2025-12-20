from clases.notificacion import Notificacion
import re

MAX_LARGO_CORREO = 500  # Máximo largo del mensaje para correo
COSTO_CHARS = 100       # Costo por cada 15 caracteres

# Clase para notificaciones por correo electrónico
class Notif_Correo(Notificacion):
    # Método para validar el formato del correo electrónico
    def validar_destino(self, destino):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        destino = self.get_destino()
        if re.match(patron, destino):
            return True
        return False

    # Método para calcular el costo total de la notificación
    def costo_total(self):
        mensaje = self.get_mensaje().strip()
        return len(mensaje)/15 * COSTO_CHARS # Costo por cada 15 caracteres

    # Método para enviar el mensaje
    def enviar_mensaje(self):
        if  not self.validar_destino(self.get_destino()): 
            self.suma_fallo()
            return f"EL correo es invalido ({self.get_destino()})."
        print(self.validar_mensaje(MAX_LARGO_CORREO))