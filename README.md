# python-poo
Repo del curso de POO con python

[Enlace a pdf externo explicado a detalle de POO](https://repositorio.grial.eu/bitstream/grial/353/1/DClase.pdf)

[Enalce a pdf externo explicado mas breve de POO](http://elvex.ugr.es/decsai/java/pdf/3c-relaciones.pdf)

[Enlace al curso completo de python en youtube](https://www.youtube.com/playlist?list=PLl8w4biTYzaUc0p1eURaJlaLEcbs1s38a)


# Curso POO con Python

## Introduccion

La POO o programacion orientada a objetos es un paradigma de programacion que nace en los anos 70 y que busca modelar los objetos de la vida real dentro del software.

La programación orientada a objetos se diferencia de la programación de procedimiento porque
ésta hace hincapié en la secuencia de los pasos de codificación necesarios para solucionar un
problema, mientras que la programación orientada a objetos lo hace en la creación e interacción
de los objetos.

Basicamente lo que hacemos cuando intentamos resolver un problema aplicando POO es, identificar que elementos participan o interactuan entre si en nuestro problema y los modelamos con codigo. Esto quiere decir que debemos identificar sus atriubutos y sus comportamientos para poder llevarlos al lenguaje de programacion que elijamos.

Existen varios lenguajes de programacion que soportan POO, aunque tambien los hay que no soportan este paradigma.

La mayoria de los lengujes populares a dia de hoy lo soportan, siendo algunos ejemplos Python, C++, Kotlin o Java.

Para ilustrar este concepto con un ejemplo sencillo podriamos pensar por ejemplo en un auto. Un auto tiene determinadas caracteristicas o atributos, como pueden ser su marca, su color, su modelo, su numero de puertas, el tamano y tipo de su motor. Por otro lado, un auto tiene determinados comportamientos, como acelerar, frenar, tocar bocina, encender las luces, etc.

Una ultima cosa a destacar es que el modelado de un objeto depende tambien del contexto del problema. El ejemplo anterior del auto podria corresponder al modelado de algun software de un auto, mientras que si lo que necesitamos es modelar un auto en el contexto de un software para la administracion de un estacionamiento, el modelado sera totalmente diferente ya que los atributos a observar y los comportamientos que nos interesa modelar del auto en esos ambientes no son los mismos. En el caso del estacionamiento los atributos podrian ser marrca, modelo, color y patente. Sus comportamientos podrian ser ingresar al estacionamiento y salir del estacionamiento.

## Clases y objetos

Para hacer el modelado de los objetos de la vida real a codigo, lo hacemos mediante el uso de clases y objetos. Podemos pensar a las clases como una plantilla o modelo a partir de la cual vamos ir creando diferentes objetos. Estos objetos pueden diferir en sus caracteristicas. Un ejemplo de esto podria ser una remera, donde nosotros creariamos la clase remera y luego a partir de ella creariamos diferentes objetos remera, una roja talle l, otra azul talle m y asi diferentes variantes. A estas caracteristicas de los objetos en la vida real los llamamos atributos en los objetos de nuestro codigo.

Los atributos de una clase los representamos en codigo mediante variables y los comportamientos los representamos mediante funciones. Cuando una funcion pertenece a una clase recibe el nombre de metodo de dicha clase y cuando una variable pertenece a una clase se convierte en un atributo de dicha clase.

De esta forma uno de los desafios mas importante de la POO es ser capaz de modelar de la mejor manera posible estos objetos ya que hacerlo de la forma incorrecta puede llevar a soluciones ineficientes y problemas para escalar mas adelante.

## Aplicacion en python

Para crear una clase en python utilizamos la palabra reservada **************class.************** Por ejemplo para crear una clase vacia lo hariamos de la siguiente manera:

```python
class Car:
	pass
```

Debemos notar una cosa, los nombres de las clases en python empiezan con mayusculas por convencion y usan camel case, lo que quiere decir que si el nombre tiene mas de una palabra, todas ellas empiezan con mayusculas.

Esta clase esta vacia y no hace nada, sin embargo python no nos permite hacer esto, por lo que se hace necesario en este caso usar la palabra clave **********pass********** para evitar el error.

Como dijimos anteriormente una clase es una plantilla que contiene la estructura para crear objetos con diferentes atributos y comportamientos o metodos.

Al no tener atributos nuestra clase, podemos crear una instancia de la siguiente forma:

```python
my_car = Car()
```

Notese que usamos el nombre de la clase y los parenteisis a continuacion para indicar que vamos a crear un objeto llamado my_car a partir de la clase Car. El hecho de usar parentesis, al igual que cuando se llama a una funcion te puede haber parecido curioso. Te quedara mucho mas claro el porque en unos segundos.

Ahora bien, recordemos que nuestras clases pueden tener atributos y metodos. Como los definimos, para poder hacer uso de esa clase si tuviera atributos, debemos indicarle a python que valores deben tomar sus atributos al momento de crearse y esto lo hacemos con la ayuda de algo que se llama constructor.

Un constructor es un metodo que toma la plantilla o clase que creamos y genera objetos a partir de ella, tantos objetos como queramos.

A un objeto generado a partir de una clase lo llamamos por lo general instancia de esa clase.

Por lo que diriamos que un constructor instancia objetos de una clase.

Como el constructor no es un metodo cualquiera de una clase, sino que es un metodo especial que ademas debe ser llamado directamente de la clase y no desde una instancia, debemos indicarle este metodo a python de una forma especial:

```python
class Car:
	
	# El metodo __init__ es el constructor de nuestra clase 
	# y es el encargado de generar objetos o instancias a partir de ella
	def __init__(self, marca, color):
		self.marca = marca
		self.color = color
```

El uso de `__init__` y el doble `__` no es una coincidencia. Cuando veas un método con esa forma, significa que está reservado para un uso especial del lenguaje.

Si observamos el constructor del ejemplo anterior veremos que el primer parametro es self, esto siempre es asi y self hace referencia a la propia instancia de la clase que se esta creando. El segundo parametro es marca, cuyo valor se almacenara en la instancia creada dentro del atributo marca.

```python
my_car = Car('Lamborghini', 'naranja')
```

Segun en snippet anterior estariamos creando una instancia de la clase Car que dentro posee un atributo ‘marca’ que tiene el valor de ‘Volkswagen’ y otro atributo color que tiene el valor de ‘naranja’.

Cabe remarcar que a este tipo de atributos (los que se definen en el constructor) se les llama atributos de instancia, ya que son propios para cada instancia y se definen en el constructor, durante la instanciacion del objeto.

Una vez que tenemos instanciada la clase podemos acceder a sus atributos a partir de la notacion de punto de la siguiente manera:

```python
print(my_car.marca)
print(my_car.color)
```

Asi como tenemos los atributos de instancia, tambien tenemos los atributos de clase, estos los definimos a nivel de clase y por lo tanto seran comunes a todas las instancias que generemos a partir de la clase.

```python
class Car:
	
	velocidad_actual = 0
	
	# El metodo __init__ es el constructor de nuestra clase 
	# y es el encargado de generar objetos o instancias a partir de ella
	def __init__(self, marca, color):
		self.marca = marca #Atributos de instancia
		self.color = color 
```

Al ser un atributo de clase (Similar a los atributos estaticos en java) podemos accederlo tanto sin instanciar la clase, como habiendola instanciado

```python
print(Car.velocidad_actual)
my_car = Car('Volkswagen', 'Rojo')
my_car.numero_ruedas
```

## Metodos

Ademas de atributos, podemos agregarle funcionalidad a nuestra clase, esto lo hacemos asociandole funciones, las cuales por ser funciones relacionadas a una clase reciben el nombre de metodos.

```python
class Car:
	
	velociadad_actual = 0
	
	# El metodo __init__ es el constructor de nuestra clase 
	# y es el encargado de generar objetos o instancias a partir de ella
	def __init__(self, marca, color):
		self.marca = marca #Atributos de instancia
		self.color = color
	
	def tocar_bocina (self):
		print('Tocando bocina')

	def cambiar_velocidad (self, velocidad) :
		print(f'Acelerando hasta velocidad {velocidad}')
		self.velocidad_actual = velocidad
```

Para definir metodos en una clase solo es necesario declarar funciones dentro del cuerpo de la clase.

De nuevo podemos acceder a los metodos de la instancia mediante la notacion de punto.

```python
my_car = Car('Volkswagen', 'Rojo')
my_car.tocar_bocina()
my_car.cambiar_velocidad(10)
```

## UML

[https://repositorio.grial.eu/bitstream/grial/353/1/DClase.pdf](https://repositorio.grial.eu/bitstream/grial/353/1/DClase.pdf)

[http://elvex.ugr.es/decsai/java/pdf/3c-relaciones.pdf](http://elvex.ugr.es/decsai/java/pdf/3c-relaciones.pdf)

## Principios de la POO

La POO se funamenta en 4 pilares o conceptos fundamentales:

- Abstraccion
- Polimorfismo
- Encapsulacion
- Herencia

### Abstraccion

Como mencionamos anteriormente, la POO busca modelar en codigo objetos de la vida real. Sin embargo, los objetos del programa no representan a los originales de manera exacta. En su lugar, los objetos que creamos solo copian atributos y comportamientos especificos que son utiles en el contexto en el que estamos trabajando.

Asi, citando un ejemplo del libro de patrones de diseno de refactoring guru, podemos tener una clase Avion. Dicha clase tendra representaciones completamente distintas segun el contexto en el que se este trabajando. Por ejemplo, si intentamos modelar un avion en el contexto de un simulador de vuelo y por otro lado en una aplicacion de reserva de pasajes aereos los resultados son totalmente diferentes.

En el caso del simulador, la clase Avion contendria informacion relacionada con el propio vuelo,

![Untitled](Curso%20POO%20con%20Python%203961ba94cda2486791311e452fcf4c3c/Untitled.png)

Mientras que en el caso de la aplicacion de reservas habria que preocuparse del mapa de asientos y de los asientos que estan disponibles.

Entonces la ************************abstraccion************************ es el modelado de un objeto o fenomeno del mundo real, limitado a un determinado contexto, que representa todos los datos relevantes a este contexto con gran precision, omitiendo el resto.

### Encapsulamiento

La encapsulacion es la capacidad que tiene un objeto de esconder partes de su estado y comportamiento de otros objetos, exponiendo unicamente una interfaz limitada al resto del programa.

Esto podemos verlo mejor con algunos ejemplos de la vida real. Por ejemplo para encender un auto, solo debemos girar la llave, es decir, para nosotros la interfaz es la llave. Luego por dentro y de forma oculta a nosotros el auto realiza una serie de acciones que terminan en que el auto finalmente enciende. Pero todo eso que sucede bajo el capo luego que nosotros giramos la llave, es invisible para nosotros. Eso es la encapsulacion, ocultar determinados detalles de la implementacion y solo exponer una interfaz sencilla y acotada.

Encapsular algo significa hacerlo privado, y por ello, accesible solo desde dentro de los metodos de su propia clase. Existe un modelo menos restrictivo llamado protegido que hace que un miembro de una clase tambien este disponible para las subclases. 

El control de acceso a los metodos y atributos de una clase se lleva a cabo mediante lo que definimos como modificadores de acceso. En java por ejemplo tenemos 3 modificadores de acceso: private, protected y public. En private los atributos o metodos solo son accesibles desde la propia clase, con protected ademas hacemos que sean accesibles desde subclases, por utlimo con public exponemos estos metodos o variables al resto de nuestro programa, haciendolos accesibles desde cualquir fragmento de codigo.

Cuando creamos una nueva clase en python, el modificador de acceso por defecto es el publico. Lo que quiere decir que el 100% de nuestra clase es acecsible desde el exterior y esto no es bueno. De hecho te recomiendo solo hacer publico lo minimo indispensable para el funcionamiento correcto del app.

```python
class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase("Que tal")
mi_clase.atributo_clase
mi_clase.atributo_instancia

# 'Hola'
# 'Que tal'
```

![Untitled](Curso%20POO%20con%20Python%203961ba94cda2486791311e452fcf4c3c/Untitled%201.png)

Vemos que todos los atributos de la clase son por defecto publicos en python.

```python
class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
mi_clase.atributo_clase     # Ok!
mi_clase.metodo_normal()    # Ok!
```

Sin embargo al definir a las variables con sus nombre comenzando con __ lo que hacemos es indicarle a python que estas seran accesibles unicamente desde la propia clase.

Como curiosidad extra, tenemos un metodo que nos muestra todas las propiedades y metodos de una clase, este metodo es el metodo dir. Como era de esperarse, al ser nuestras propiedades privadas, el metodo dir tampoco las mostrara.

```python
print(dir(mi_clase))
#['_Clase__atributo_clase', '_Clase__mi_metodo', '_Clase__variable',
#'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#'__str__', '__subclasshook__', '__weakref__', 'atributo_clase', 'metodo_normal']
```

En realidad hay una forma de saltarse esta restriccion pero no es buena idea hacerlo asi que no lo vamos a ver aqui.

```python
mi_clase._Clase__atributo_clase
# 'Hola'
mi_clase._Clase__mi_metodo()
# 'Haz algo'
```

### Herencia

En conjunto con el concepto de herencia debemos definir otros dos conceptos que son el de superclase o clase padre y subclase o clase hija.

La herencia es la capacidad de crear nuevas clases a partir de clases ya existentes. 

Una clase usada como base para crear otra clase (extender) se llama superclase o clase padre.

Una clase creada a partir de otra clase (heredando de ella) se llama subclase o clase hija.

La principal ventaja de la herencia es la reutilizacion de codigo. Si queres crear una clase ligeramente diferente de una clase ya existente, no hay necesidad de duplicar el codigo. Extendemos de la clase original y colocamos la funcionalidad adicional dentro de una subclase resultante que hereda los campos y metodos de la superclase.

La consecuencia de la herencia es que las subclases tienen la misma interfaz que su clase padre. No es posible esconder un metodo en una subclase si este se declaro en la superclase. Tambien se debe implementar todos los metodos abstractos aunque estos no tengan sentido en la subclase.

En la mayoria de los lenguajes solo es posbile que una clase herede de una unica superclase, en cambio con las interfaces esto no es asi, nuestra clase puede implementar tantas interfaces como se nos ocurra. Sin embargo, como se menciono recien, si una superclase implementa una interfaz, entonces todas las subclases deben implementar dicha interfaz.

```python
# Definimos una clase padre
class Animal:
    pass

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    pass
```

Luego para saber si realmente una clase es hija o hereda de otra clase, podemos hacerlo con __bases__

```
print(Perro.__bases__)
# (<class '__main__.Animal'>,)
```

De la misma manera que podemos ver que clases heredan de una cierta clase con __subclasses__

```python
print(Animal.__subclasses__())
# [<class '__main__.Perro'>]
```

La herencia esta muy asociada con un principio muy importante llamado DRY (Don’t Repeat Yourself)

Ahora para ver un ejemplo en codigo, utilizaremos la clase Animal.

```python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

Ahora que ya tenemos definida una clase generica Animal que condensa todos los metodos y propiedades que tienen en comun los animales, podemos extender de ella clases particulares para cada animal.

Primero vamos a crear una clase vacia para ver como se estan heredando las propiedades y comportamientos de la clase padre.

```python
# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro
```

Podemos incluso crear nuevos metodos, como en el caso de abeja, por ejemplo, que tiene el metodo picar:

```python
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")
```

Del ejemplo anterior notamos 3 clases diferentes de metodos:

- Heredados directamente: describeme
- Heredados de la clase padre, pero modificados: hablar(), moverse()
- Creados en la clase hija unicamente: picar()

Una de las preguntas que tal vez te surgio es si podemos desde una clase hija referenciar a esa clase padre de la cual heredamos. Para esto tenemos el metodo super(). Uno de los usos mas comunes de super() es el de extender el comportamiento del constructor para adaptarlo a nuestra clase hija. Un caso de esto podria ser si nuestra clase hija tiene algun parametro que la clase padre no. Veamos como seria con nuestro ejemplo de Animal y Perro.

```python
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño
```

## Herencia multiple

En python a diferencia de otros lenguajes, tenemos herencia multiple, es decir que una clase puede heredar de varias clases al mismo tiempo.

```python
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass
```

Tambien es posible obviamente que una clase herede de otra clase, la cual a su vez hereda de otra clase.

En este punto puede surgir otra duda y es que si bien las clases hijas heredan los metodos de las clases padres, tambien pueden sobreescribirlos teniendo sus propias implementaciones. Entonces, si llamo a un metodo que las clases tienen en comun. A cual estoy llamando?

Bueno, siempre se va desde la clase actual hacia arriba en el esquema de herencia, de modo que se empieza buscando en la clase actual, si en ella no esta implementado se continua con su clase padre y sino con la clase padre de su clase padre.

Algo a destacar es que en python todo es un objeto, de modo que si consultas el MRO o mehtod resolution order de cualquier elemento en python veremos que al final todo en python hereda de object.

```python
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass

print(Clase3.__mro__)
# (<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.Clase2'>, <class 'object'>)
```

### Polimorfismo

El polimorfismo es la capacidad que tiene un programa de detectar la verdadera clase de un objeto e invocar su implementacion, incluso aunque su tipo real sea desconocido en el contexto actual.

Otra forma de pensar el polimorfismo seria entendiendolo como la capacidad de un objeto de fingir ser otra cosa, normalmente una clase que extiende o una interfaz que implementa.

Veamos un ejemplo con animales. La mayoria de los animales es capaz de emitir algun sonido, por lo que nuestra clase Animal podria implementar un metodo emitirSonido. Sin embargo, todos los animales emiten sonidos diferentes, por lo que podriamos pensar que cada una de las clases hijas deberan hacer su propia implementacion de este comportamiento. De esta forma es que declaramos al metodo emitirSonido() como un metodo abstracto. Esto nos permite evitar cualquier implementacion de este metodo en la clase Animal, pero obliga a todas las clases hijas a hacer su propia implementacion.

![Untitled](Curso%20POO%20con%20Python%203961ba94cda2486791311e452fcf4c3c/Untitled%202.png)

De esta forma el programa no conoce realmente cual es la clase del objeto, solo sabe que es un Animal y por lo tanto implementa si o si el metodo emitirSonido, de forma que se puede llamar a este metodo independientemente de que tipo de animal sea. Esto nos permite que lo mismo podamos utilizar la clase Gato, Perro o cualquier otra que herede de Animal sin tener problemas.
