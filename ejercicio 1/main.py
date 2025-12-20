# Main de ejercicio 1
from clases.gestion_notif import Gestion_Notif
from clases.notif_correo import Notif_Correo
from clases.notif_telefono import Notif_Telefono
from clases.notif_url import Notif_Url

# Crear instancia de Gestion_Notif
gestion_notif = Gestion_Notif()

# Menú interactivo para el usuario
while True:
    # Opciones del menú
    print("\n - - - M E N Ú - - -")
    print("1. Registrar mensaje.")
    print("2. Ingresar destino.")
    print("3. Enviar notificación a los destinos.")
    print("4. Mostrar un resumen.")
    print("5. Salir.")

    opcion = str(input("Opción: "))

    # Manejo de opciones del menú
    match opcion:
        # Registrar mensaje - se usará el ultimo mensaje registrado
        case "1":
            print("\n--- MENSAJE ---")
            mensaje = str(input("Ingrese el mensaje que enviará en la notificación: "))

        # Ingresar destino
        case "2":
            print("\n--- DESTINO ---")
            print("1. Correo electronico.")
            print("2. Telefono celular.")
            print("3. Url.")
            print("4. Salir.")

            tipo = str(input("Ingrese el destino: "))

            # Manejo de tipos de destino
            match tipo:
                case "1":   
                    print("- Agregar Correo (ejemplo: usuario@dominio.com)")
                    destino = str(input("Ingrese el correo: "))
                    n_correo = Notif_Correo(mensaje, destino)       # Crear instancia de Notif_Correo
                    print(gestion_notif.agregar_destino(n_correo))  # Agregar destino a la gestión
                case "2":
                    print("- Agregar Telefono (ejemplo: +56912345678 o 912345678)")
                    destino = str(input("Ingrese el telefono: "))
                    n_telefono = Notif_Telefono(mensaje, destino)       # Crear instancia de Notif_Telefono
                    print(gestion_notif.agregar_destino(n_telefono))    # Agregar destino a la gestión
                case "3":
                    print("- Agregar Url (ejemplo: https://www.ejemplo.com)")
                    destino = str(input("Ingrese el url: "))    
                    n_url = Notif_Url(mensaje, destino)             # Crear instancia de Notif_Url
                    print(gestion_notif.agregar_destino(n_url))     # Agregar destino a la gestión
                case "4":
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")

        case "3":
            print("\n--- ENVIAR NOTIFICACIÓN ---")
            gestion_notif.enviar()      # Enviar notificaciones a los destinos registrados

        case "4":
            print("\n--- RESUMEN ---")
            gestion_notif.resumen()    # Mostrar resumen de envíos
        case "5":
            print("Saliendo...")
            break

        case _:
            print("Opción inválida.")
