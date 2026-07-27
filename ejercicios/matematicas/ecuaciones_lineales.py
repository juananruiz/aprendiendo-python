import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve, sympify

def plot_linear_equation(equation_str):
    # Crear un símbolo para la variable
    x, y = symbols('x y')
    
    try:
        # Separar el lado izquierdo y derecho de la ecuación
        left_side, right_side = equation_str.split('=')
        
        # Convertir ambos lados en expresiones sympy y restar el lado derecho
        equation = Eq(sympify(left_side) - sympify(right_side), 0)
        
        # Resolver la ecuación para y
        y_expr = solve(equation, y)[0]
        
        # Crear una función lambda para evaluar y
        f = lambda x_val: float(y_expr.subs(x, x_val))
        
        # Generar puntos para el gráfico
        x_vals = np.linspace(-10, 10, 100)
        y_vals = [f(xi) for xi in x_vals]
        
        # Crear el gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=equation_str)
        plt.axhline(y=0, color='k', linestyle='--')
        plt.axvline(x=0, color='k', linestyle='--')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Gráfica de la ecuación: {equation_str}')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    except Exception as e:
        print(f"Error al procesar la ecuación: {e}")
        print("Asegúrate de ingresar una ecuación lineal válida en el formato 'ax + by = c'.")

# Ejemplo de uso
equation = input("Ingresa una ecuación lineal (por ejemplo, '2*x + y = 3'): ")
plot_linear_equation(equation)