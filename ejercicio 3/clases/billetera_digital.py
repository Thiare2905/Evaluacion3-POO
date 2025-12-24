from clases.medio_pago import Medio_Pago

RECARGO_FIJO = 1000 # Recargo fijo por uso de billetera digital

class Billetera_Digital(Medio_Pago):
    def __init__(self, identificador, saldo):
        super().__init__(identificador, "Billetera digital")
        self.__saldo = saldo # saldo disponible en la billetera digital

    # Método para calcular el pago con recargo fijo
    def calcular_pago(self, monto):
        if monto + RECARGO_FIJO > self.__saldo:
            return False
        self.__saldo -= (monto + RECARGO_FIJO)
        return monto + RECARGO_FIJO
    
    # Método para validar el pago
    def validar(self):
        print("Validando saldo en la App...")
        return True