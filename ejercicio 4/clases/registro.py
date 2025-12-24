# Clase Registro para gestionar sensores y fallos
class Registro:
    def __init__(self):
        self.__sensores = [] # Lista de sensores registrados
        self.__fallos = [] # Lista de sensores con fallos

    # Método para registrar un sensor
    def registrar(self, sensor):
        if not sensor.leer_sensor():
            self.__fallos.append(sensor)
        self.__sensores.append(sensor)
    
    # Método para generar un reporte de sensores y fallos
    def reporte(self):
        print("- - - R E P O R T E - - -")
        for s in self.__sensores:
            print(s.descripcion())
        if self.__fallos == None:
            print(" - Fallos:")
            for f in self.__fallos:
                print(f.descripcion())