# Método babilónico para calcular la raíz cuadrada
# Si tienes un candidato para raiz de n como n/2
# (n/2)/2 es también una buena aproximación
# pero si promedias ambas obtienes una mejor aproximación
# si sigues iterando, la aproximación mejora cada vez más
# paramos cuando la diferencia entre las aproximaciones sea menor que 1e-10
# https://chatgpt.com/c/6a67878a-81e4-83eb-849b-e0626887a10b

def babylonian_squareroot(n):
    
    if n < 0:
        raise ValueError("No se puede calcular raíz de negativo")
    if n == 0:
        return 0

    # Ponemos 2.0 para forzar la división de punto flotante
    guess = n / 2.0
    while True:
        print(guess)
        better_guess = (guess + n / guess) / 2.0
        if abs(guess - better_guess) < 1e-10:
            return better_guess   # esto hace que pare de iterar
        guess = better_guess

if __name__ == "__main__":
    print(babylonian_squareroot(25))