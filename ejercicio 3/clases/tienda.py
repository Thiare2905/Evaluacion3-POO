from clases.venta import Venta

# Clase para representar una tienda que gestiona ventas
class Tienda:
    def __init__(self):
        self.__ventas = [] # lista de ventas registradas

    # Método para registrar una venta
    def registrar_venta(self, venta: Venta):
        # Verificar si la venta ya está registrada
        for v in self.__ventas:
            if v.get_id_venta() == venta.get_id_venta():
                return "Ya está registrada esta venta."
        # Validar medio de pago y procesar pago
        if not venta.get_medio_pago().validar():
            return "Medio de pago invalido."
        # Procesar pago
        if not venta.procesar_pago():
            return "Pago rechazado."
        self.__ventas.append(venta)
        return "Venta registrada con éxito."

    # Método para generar un reporte de ventas
    def reporte(self):
        recaudado = 0
        recargo_total = 0
        # Imprimir detalles de cada venta
        print(" - - REPORTE - -")
        for v in self.__ventas:
            recaudado += v.get_total() # monto recaudado sin recargo
            recargo_total += v.get_recargo() # recargo total
            print(v.comprobante()) # Comprobante de la venta
        print(f"Total recaudado: ${recaudado}") # Monto sin recargos
        print(f"Total recargos: ${recargo_total}") # Total recargos aplicados


