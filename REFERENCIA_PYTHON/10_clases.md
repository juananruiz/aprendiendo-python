# Clases (POO básica)

## Qué es una clase

Una clase es una plantilla para crear objetos. Un objeto tiene **atributos** (datos) y **métodos** (funciones).

```python
class Perro:
    # __init__ se ejecuta al crear un objeto
    def __init__(self, nombre, raza):
        self.nombre = nombre   # atributo de instancia
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

    def __str__(self):
        return f"Perro({self.nombre}, {self.raza})"

# Crear objetos (instanciar)
rex = Perro("Rex", "Pastor Alemán")
coco = Perro("Coco", "Labrador")

rex.ladrar()    # "Rex dice: ¡Guau!"
rex.nombre      # "Rex"
print(rex)      # "Perro(Rex, Pastor Alemán)"  — usa __str__
```

## Métodos especiales (dunder methods)

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"       # para print()

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"  # representación técnica

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

a = Punto(1, 2)
b = Punto(3, 4)
a + b        # Punto(4, 6)
a == Punto(1, 2)   # True
```

## Atributos de clase vs de instancia

```python
class Contador:
    total = 0          # atributo de clase — compartido por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre     # atributo de instancia — propio de cada objeto
        Contador.total += 1

c1 = Contador("uno")
c2 = Contador("dos")
Contador.total   # 2
```

## Herencia

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Las subclases deben implementar este método")

    def __str__(self):
        return f"{self.__class__.__name__}({self.nombre})"


class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


animales = [Perro("Rex"), Gato("Misi"), Perro("Toby")]
for animal in animales:
    print(animal.hablar())   # polimorfismo: cada uno responde según su clase
```

## super()

```python
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

class Coche(Vehiculo):
    def __init__(self, marca, velocidad_max, puertas):
        super().__init__(marca, velocidad_max)  # llama al __init__ del padre
        self.puertas = puertas

c = Coche("Toyota", 200, 4)
```

## @property — getters y setters

```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio          # convención: _ indica "no acceder directamente"

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def area(self):
        import math
        return math.pi * self._radio ** 2   # calculada, sin almacenar

c = Circulo(5)
c.radio        # 5         — llama al getter
c.radio = 10   # 10        — llama al setter (valida)
c.area         # 314.15... — calculada al vuelo
```

## Cuándo NO usar clases

Las clases no siempre son la respuesta. Usa funciones simples si:

- La funcionalidad no necesita estado interno.
- No vas a crear múltiples instancias.
- El código es más claro sin ellas.

```python
# Innecesariamente complicado:
class Sumador:
    def sumar(self, a, b):
        return a + b

# Mejor así:
def sumar(a, b):
    return a + b
```
