class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describe_clase(self):
        print("Soy un animal de la clase: ", type(self).__name__)

class Perro(Animal):

    def __init__(self, especie, edad, dueno):
        super().__init__(especie, edad)
        self.dueno = dueno
    
    def moverse(self):
        print("Soy un perro caminando.")

    def hablar(self):
        print("Guau!")


class Gato(Animal):
    
    def moverse(self):
        print("Soy un gato caminando!")

    def ronronear(self):
        print("estoy ronroneando")

    def hablar(self):
        print("Miau!")

# print(Perro.__bases__)
# print(Animal.__bases__)

# print(Perro.__subclasses__())
# print(Animal.__subclasses__())

mi_perro = Perro("Mamifero", "4", "lasecta")
mi_gato = Gato("Mamifero", "2")

mi_perro.describe_clase()
mi_gato.describe_clase()

mi_perro.moverse()
mi_gato.hablar()
mi_gato.ronronear()
print(mi_perro.dueno)
