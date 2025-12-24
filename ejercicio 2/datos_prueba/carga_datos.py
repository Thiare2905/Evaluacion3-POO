from clases.estadia import Estadia
from clases.auto import Auto
from clases.moto import Moto
from clases.camion import Camion

# Función para cargar datos de prueba en el estacionamiento
def cargar_datos(estacionamiento):
    datos = [
        ("Auto", "AA1111", "08:10", "09:30"),
        ("Moto", "BB2222", "10:00", "10:20"),
        ("Camion", "CC3333", "17:30", "19:00"),
        ("Auto", "DD4444", "18:00", "20:15"),
        ("Moto", "EE5555", "19:10", "20:00"),
        ("Camion", "FF6666", "16:00", "18:30"),
        ("Auto", "GG7777", "14:00", "15:10"),
        ("Moto", "HH8888", "18:30", "19:00"),
        ("Camion", "II9999", "20:00", "22:00"),
        ("Auto", "JJ1010", "09:00", "11:45"),
        ("Moto", "KK1112", "07:30", "08:30"),
        ("Camion", "LL1314", "15:00", "17:00"),
    ]

    # Iterar sobre los datos y registrar las estadías
    for tipo, patente, entrada, salida in datos:
        match tipo:
            case "Auto":
                vehiculo = Auto(patente)
            case "Moto":
                vehiculo = Moto(patente)
            case "Camion":
                vehiculo = Camion(patente)

        estacionamiento.registrar_estadia(Estadia(vehiculo, entrada, salida))
