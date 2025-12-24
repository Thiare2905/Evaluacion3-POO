from clases.sensor import Sensor

# Clase Sensor_Temperatura que hereda de Sensor
class Sensor_Temperatura(Sensor):
    # Inicializador de la clase con id_sensor y temperatura
    def __init__(self, id_sensor, temperatura):
        super().__init__(id_sensor)
        self.__temperatura = temperatura 
        self.__bool = False # Variable para validar lectura

    # Método para leer el sensor y convertir la temperatura a Celsius
    def leer_sensor(self):
        # Normalizar entrada
        temp = self.__temperatura.upper().strip()
        
        # Convertir a Celsius si es necesario
        if temp.endswith("F"):
            self.__temperatura = float(temp.replace("F", "")) # Convertir a float
            self.__temperatura = (self.__temperatura - 32) * 5 / 9 # Formula de Fahrenheit a Celsius
            self.__bool = True
            return True
        # Si ya está en Celsius
        elif temp.endswith("C"):
            self.__temperatura = float(temp.replace("C", "")) # Convertir a float
            self.__bool = True
            return True
        # Si el formato es incorrecto
        else:
            self.__bool = False
            return False
        
    # Método para obtener la descripción del sensor
    def descripcion(self):
        # Verificar si la lectura es válida
        if not self.__bool:
            # Formato incorrecto
            return f"Sensor de Temperatura -> Temperatura: Está mal el formato ({self.__temperatura})."
        # Formato correcto
        return f"N°{self.get_id()} Sensor de Temperatura -> Temperatura: {self.__temperatura}°C."
    
    # Método para obtener la temperatura
    def get_temperatura(self):
        return self.__temperatura