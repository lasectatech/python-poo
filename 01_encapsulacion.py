class Clase:
    atributo_publico = "Hola"
    __atributo_privado = "Soy privado, no podes accederme desde fuera de la clase"

    def metodo_publico(self):
        print("Hola soy un metodo publico")
        print("Yo que soy parte de la clase, puedo acceder a los metodos privados")
        self.__metodo_privado()
        print("Tambien a los atributos privados")
        print(self.__atributo_privado)

    def __metodo_privado(self):
        print("Hola soy un metodo privado")


mi_clase = Clase()

print(dir(mi_clase)) # muestra las propiedaes y metodos de nuestra clase

print(mi_clase.atributo_publico)
print(Clase.atributo_publico)
mi_clase.metodo_publico()

print(mi_clase.__atributo_privado)
print(Clase.__atributo_privado)
mi_clase.__metodo_privado()
