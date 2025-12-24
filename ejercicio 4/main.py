from clases.registro import Registro
from clases.sensor_humedad import Sensor_Humedad
from clases.sensor_movimiento import Sensor_Movimiento
from clases.sensor_temperatura import Sensor_Temperatura

registro = Registro()   # Crear instancia de Registro
id_actual = 1           # ID inicial para sensores

while True:
    # Menú de opciones
    print("\n- - - MENÚ SENSORES - - -")
    print("1. Registrar sensor de temperatura")
    print("2. Registrar sensor de humedad")
    print("3. Registrar sensor de movimiento")
    print("4. Ver reporte")
    print("5. Salir")

    opcion = input("Seleccione una opción: ") # Leer opción del usuario

    match opcion:
        # Registrar sensor de temperatura
        case "1":
            valor = input("Ingrese temperatura (ej: 25C, 77F): ")
            sensor = Sensor_Temperatura(id_actual, valor)   # Crear sensor de temperatura
            registro.registrar(sensor)              # Registrar sensor
            id_actual += 1
            print("Sensor de temperatura registrado.")

        case "2":
            # Registrar sensor de humedad
            valor = int(input("Ingrese humedad (%) (0 a 100): "))
            sensor = Sensor_Humedad(id_actual, valor) # Crear sensor de humedad
            registro.registrar(sensor)        # Registrar sensor
            id_actual += 1
            print("Sensor de humedad registrado.")

        case "3":
            # Registrar sensor de movimiento
            valor = float(input("Ingrese valor de movimiento (mayor a 0.7): "))
            sensor = Sensor_Movimiento(id_actual, valor)    # Crear sensor de movimiento
            registro.registrar(sensor)      # Registrar sensor
            id_actual += 1
            print("Sensor de movimiento registrado.")

        case "4":
            # Ver reporte de sensores
            registro.reporte()

        case "5":
            # Salir del programa
            print("Saliendo...")
            break

        case _:
            print("Opción inválida.")