import sympy as sp

# Definimos la variable simbólica y la función
x = sp.symbols('x')
funcion = sp.sin(x)

# Calculamos la derivada de la función con respecto a x
derivada = sp.diff(funcion, x)

# Evaluamos la derivada en el punto x = 1
valor_derivada_en_1 = derivada.evalf(subs={x: 1})

print(f"La derivada de sin(x) es: {derivada}")
print(f"El valor de la derivada en x = 1 es: {valor_derivada_en_1}")