from clases.medio_pago import Medio_Pago

# Clase para representar una transferencia como medio de pago
class Transferencia(Medio_Pago):
    def __init__(self, identificador, saldo):
        super().__init__(identificador, "Transferencia")
        self.__saldo = saldo # saldo disponible para la transferencia

    # Método para calcular el pago sin recargo
    def calcular_pago(self, monto):
        # Verificar si hay saldo suficiente
        if monto > self.__saldo:
            return False
        # Solicitar confirmación de la transferencia
        confirmacion = input("¿Confirmar transferencia? (s/n):")
        if confirmacion.lower() != "s":
            return False
        return monto 
    
    # Método para validar el pago
    def validar(self):
        print("Esperando confirmación...")
        return True