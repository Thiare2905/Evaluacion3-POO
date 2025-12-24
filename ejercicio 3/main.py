from clases.tienda import Tienda
from clases.venta import Venta
from clases.tarjeta import Tarjeta
from clases.transferencia import Transferencia
from clases.billetera_digital import Billetera_Digital
import random

mi_tienda = Tienda() # Instancia de la tienda
id_venta = 0 # Contador de ID de ventas

while True:
    # Menú principal
    print("\n--- MENÚ TIENDA ---")
    print("1. Registrar venta")
    print("2. Ver reporte")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        # Registrar venta
        case "1":
            monto = int(input("Monto de la venta: "))
            # Selección del medio de pago
            print("\nMedio de pago:")
            print("1. Tarjeta")
            print("2. Transferencia")
            print("3. Billetera Digital")
            medio = input("Seleccione medio: ")
                
            match medio:
                case "1":
                    numero = random.randint(1000000, 2000000) # Número de tarjeta 
                    cupo = random.randint(monto-100, monto+100000) # Cupo disponible
                    medio_pago = Tarjeta(numero, cupo) # Instancia de Tarjeta
                case "2":
                    saldo = random.randint(monto-100, monto+100000) # Saldo disponible
                    cuenta = random.randint(100000, 200000) # Número de cuenta
                    medio_pago = Transferencia(cuenta, saldo) # Instancia de Transferencia

                case "3":
                    cuenta = random.randint(10000000, 20000000) # Número de cuenta
                    saldo = random.randint(monto-100, monto+100000) # Saldo disponible
                    medio_pago = Billetera_Digital(cuenta, saldo) # Instancia de Billetera Digital

                case _:
                    # Opción inválida
                    print("opción inválida.")
                    continue
                
            id_venta += 1
            venta = Venta(id_venta, monto, medio_pago) # Instancia de Venta
            print(mi_tienda.registrar_venta(venta)) # Registrar la venta en la tienda

        case "2":
            # Ver reporte de ventas
            mi_tienda.reporte()

        case "3":
            # Salir del programa
            print("Saliendo...")
            break

        case _:
            print("Opción inválida.")
