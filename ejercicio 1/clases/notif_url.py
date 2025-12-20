from clases.notificacion import Notificacion
import re

MAX_LARGO_URL = 300 # Máximo largo del mensaje para URL
COSTO_MENSAJE = 150 # Costo base del mensaje
COSTO_EXTRA = 50    # Costo extra si el mensaje excede los 200 caracteres

# Clase para notificaciones por URL
class Notif_Url(Notificacion):
    # Método para validar el formato de la URL
    def validar_destino(self, destino):
        patron = r'^(https?:\/\/)([\w-]+\.)+[\w-]+(\/[\w\-\.~]*)*$'
        destino = self.get_destino()
        if re.match(patron, destino):
            return True
        return False
    # Método para calcular el costo total de la notificación
    def costo_total(self):
        mensaje = self.get_mensaje().strip()
        if len(mensaje) > 200: 
            return COSTO_MENSAJE + COSTO_EXTRA
        return COSTO_MENSAJE
    
    # Método para enviar el mensaje
    def enviar_mensaje(self):
        if not self.validar_destino(self.get_destino()):
            self.suma_fallo()
            return f"La URL no es valida ({self.get_destino()})."
        print(super().validar_mensaje(MAX_LARGO_URL))