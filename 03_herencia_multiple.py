
class Clase1:
    pass

class Clase2:
    pass

class Clase3(Clase2, Clase1):
    pass

print(Clase3.__mro__)
