# Main de ejercicio 2
from clases.estadia import Estadia
from clases.estacionamiento import Estacionamiento
from clases.auto import Auto
from clases.moto import Moto
from clases.camion import Camion
from datos_prueba.carga_datos import cargar_datos

estacionamiento = Estacionamiento() # Crear instancia de Estacionamiento
cargar_datos(estacionamiento) # Cargar datos de prueba

while True:
    print("\n- - - MENÚ ESTACIONAMIENTO - - -")
    print("1. Registrar estadía.")
    print("2. Ver reporte.")
    print("3. Salir.")

    opcion = input("Seleccione una opción: ")

    match opcion:
        # Registrar estadía
        case "1":
            patente = input("Ingrese patente: ")
            print("Tipo de vehículo:")
            print("1. Auto")
            print("2. Moto")
            print("3. Camión")
            tipo = input("Seleccione tipo: ")

            match tipo:
                case "1":
                    vehiculo = Auto(patente) # Crear instancia de Auto
                case "2":
                    vehiculo = Moto(patente) # Crear instancia de Moto
                case "3":
                    vehiculo = Camion(patente) # Crear instancia de Camion
                case _:
                    print("Tipo de vehículo inválido")
                    continue

            entrada = input("Hora entrada (HH:MM): ") # Ingresar hora de entrada
            salida = input("Hora salida (HH:MM): ") # Ingresar hora de salida
            estadia = Estadia(vehiculo, entrada, salida) # Crear instancia de Estadia
            print(estacionamiento.registrar_estadia(estadia)) # Registrar estadía en el estacionamiento 

        case "2":
            # Ver reporte
            estacionamiento.reporte()

        case "3":
            # Salir
            print("Saliendo...")
            break

        case _:
            # Opción inválidas
            print("Opción inválida.")