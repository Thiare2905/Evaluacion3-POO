# Clase para representar una venta en la tienda
class Venta:
    def __init__(self, id_venta, monto, medio_pago):
        self.__id_venta = id_venta 
        self.__monto = monto        # monto base de la venta
        self.__medio_pago = medio_pago # medio de pago utilizado
        self.__total = 0            # monto total pagado (con recargo)
        self.__recargo = 0          # recargo aplicado

    # Método para procesar el pago de la venta
    def procesar_pago(self):
        # Calcular el pago usando el medio de pago
        resultado = self.__medio_pago.calcular_pago(self.__monto)
        # Verificar si el pago fue exitoso
        if resultado is False:
            return False
        self.__total = resultado
        self.__recargo = resultado - self.__monto
        return True

    # Método para generar un comprobante de la venta
    def comprobante(self):
        return (
            " -- COMPROBANTE --\n"
            f"VENTA: {self.__id_venta}\n"
            f"Medio de pago: {self.__medio_pago.get_tipo()}\n"
            f"Monto base: ${self.__monto}\n"
            f"Recargo: ${self.__recargo}\n"
            f"Total pagado: ${self.__total}\n"
        )

    # Getters
    def get_total(self):
        return self.__total

    def get_recargo(self):
        return self.__recargo

    def get_id_venta(self):
        return self.__id_venta

    def get_monto(self):
        return self.__monto

    def get_medio_pago(self):
        return self.__medio_pago
