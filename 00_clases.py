class Car:

    velocidad_actual = 0

    def __init__(self, marca, color):
        self.marca = marca # Atributos de instancia
        self.color = color # Atributos de instancia

    def tocar_bocina(self): # Metodos de la instancia
        print("Beep Beep")

    def cambiar_velocidad(self, velocidad):
        print(f"Cambiando la velocidad a {velocidad}") # Metodos de la instancia con parametros
        self.velocidad_actual = velocidad

if __name__ == '__main__':
    car = Car("Lamborghini", "Verde")
    car2 = Car("Ferrari", "Rojo")
    car3 = Car("Fiat", "Blanco")
    car2.cambiar_velocidad(10)

print(f"El {car.marca} es de color {car.color} y su velocidad es de {car.velocidad_actual} km/h")
print(f"El {car2.marca} es de color {car2.color} y su velocidad es de {car2.velocidad_actual} km/h")
print(f"El {car3.marca} es de color {car3.color}")

print(Car.velocidad_actual)
car2.tocar_bocina()