import math

def babylonian_squareroot(n):
    if n < 0:
        raise ValueError("Input must be non-negative.")
    guess = n / 2.0
    while True:
        better_guess = (guess + n / guess) / 2.0
        if math.isclose(guess, better_guess):
            return better_guess
        guess = better_guess

print(babylonian_squareroot(25))
print(babylonian_squareroot(9))
print(babylonian_squareroot(10))

