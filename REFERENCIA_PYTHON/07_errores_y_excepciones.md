# Errores y excepciones

## try / except básico

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

## Capturar el mensaje del error

```python
try:
    numero = int("abc")
except ValueError as e:
    print(f"Error: {e}")   # Error: invalid literal for int() with base 10: 'abc'
```

## Múltiples excepciones

```python
try:
    valor = lista[10]
    resultado = int(valor)
except IndexError:
    print("Índice fuera de rango")
except ValueError:
    print("El valor no es un número")
except (TypeError, KeyError):
    print("Error de tipo o clave")   # puedes agrupar en tupla
```

## else y finally

```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("División por cero")
else:
    print(f"Resultado: {resultado}")   # se ejecuta si NO hubo excepción
finally:
    print("Esto se ejecuta siempre")   # útil para limpiar recursos
```

## Lanzar excepciones con raise

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser 0")
    return a / b

# Relanzar una excepción después de loggearla
try:
    dividir(5, 0)
except ValueError as e:
    print(f"Registrado: {e}")
    raise   # vuelve a lanzar la misma excepción
```

## Excepciones comunes de la stdlib

| Excepción | Cuándo ocurre |
|-----------|---------------|
| `ValueError` | Tipo correcto pero valor inválido: `int("abc")` |
| `TypeError` | Tipo incorrecto: `"hola" + 5` |
| `IndexError` | Índice fuera de rango: `lista[99]` |
| `KeyError` | Clave que no existe en dict: `d["foo"]` |
| `AttributeError` | Atributo o método que no existe: `None.upper()` |
| `FileNotFoundError` | Fichero que no existe al abrirlo |
| `ZeroDivisionError` | División entre cero |
| `NameError` | Variable usada antes de definirse |
| `ImportError` | Módulo no encontrado |
| `StopIteration` | Iterador agotado |
| `RecursionError` | Demasiadas llamadas recursivas |

## Crear excepciones propias

```python
class SaldoInsuficienteError(Exception):
    """Se lanza cuando la cuenta no tiene fondos suficientes."""
    pass

def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError(f"Saldo: {saldo}, intento: {cantidad}")
    return saldo - cantidad

try:
    retirar(100, 200)
except SaldoInsuficienteError as e:
    print(f"Operación rechazada: {e}")
```

## Jerarquía de excepciones (simplificada)

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt       ← Ctrl+C
 └── Exception               ← la mayoría hereda de aquí
      ├── ValueError
      ├── TypeError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    └── FileNotFoundError
      └── ArithmeticError
           └── ZeroDivisionError
```

> No uses `except Exception` a secas a menos que tengas una razón. Siempre captura la excepción más específica posible.
