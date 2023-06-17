# Realice un programa en python que defina números complejos en sus repre-
# sentación binómica y sus operaciones básicas de:
# • Imprimir
# • Multiplicación por escalar
# • Módulo
# • Fase
# • Conjugación
# • Conversión a polar

import math

# Clase que representa un número complejo en su forma binómica.
class NumeroComplejo:
    def __init__(self, real, imaginario):
        
        self.real = real
        self.imaginario = imaginario

    #Imprime el número complejo en su forma binómica.
    def imprimir(self):
        
        print(f"{self.real} + {self.imaginario}i")

    #Multiplica el número complejo por un escalar.
    def multiplicacionEscalar(self, escalar):
        
        real_resultante = self.real * escalar
        imaginarioResultante = self.imaginario * escalar
        return NumeroComplejo(real_resultante, imaginarioResultante)

    #Calcula el módulo del número complejo.
    def modulo(self):
        
        return math.sqrt(self.real ** 2 + self.imaginario ** 2)

    #Calcula la fase del número complejo en radianes.
    def fase(self):
       
        return math.atan2(self.imaginario, self.real)

    #Calcula el conjugado del número complejo.
    def conjugacion(self):
        
        return NumeroComplejo(self.real, -self.imaginario)

    #Convierte el número complejo a su forma polar.
    def convertirapolar(self):
        
        modulo = self.modulo()
        fase = self.fase()
        return modulo, fase


# Ejemplo de uso
# Crear un número complejo
numero = NumeroComplejo(3, 4)

# Imprimir el número complejo
numero.imprimir()

# Multiplicar el número complejo por un escalar
escalar = 2
resultado_multiplicacion = numero.multiplicacionEscalar(escalar)
resultado_multiplicacion.imprimir()

# Calcular el módulo del número complejo
modulo = numero.modulo()
print("Módulo:", modulo)

# Calcular la fase del número complejo
fase = numero.fase()
print("Fase:", fase)

# Calcular el conjugado del número complejo
conjugado = numero.conjugacion()
conjugado.imprimir()

# Convertir el número complejo a su forma polar
polar = numero.convertirapolar()
print("Forma polar:", polar)
