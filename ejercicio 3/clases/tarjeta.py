from clases.medio_pago import Medio_Pago

RECARGO = 0.05 # Recargo del 5% por uso de tarjeta

# Clase para representar una tarjeta como medio de pago
class Tarjeta(Medio_Pago):
    def __init__(self, identificador, cupo):
        super().__init__(identificador, "Tarjeta")
        self.__cupo = cupo # cupo disponible en la tarjeta

    # Método para calcular el pago con recargo
    def calcular_pago(self, monto):
        recargo = monto * RECARGO # calcular recargo del 5%
        total = monto + recargo # monto total a pagar
        if total > self.__cupo:
            return False
        self.__cupo -= total
        return total
    
    # Método para validar el pago
    def validar(self):
        print("Validando cupo con el banco...")
        return True