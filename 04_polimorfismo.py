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


if __name__ == '__main__':
    mi_gato = Gato("Mamifero", 1)
    mi_perro = Perro("Mamifero", 4, "lasecta")

    def pasearAnimal(animal):
        animal.moverse()

    pasearAnimal(mi_gato)
    pasearAnimal(mi_perro)