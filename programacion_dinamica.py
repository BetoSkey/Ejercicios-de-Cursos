import sys


def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo={}):
    # Base case
    if n == 0 or n == 1:
        return 1

    # If number (n) key is in dictionary
    try:
        return memo[n]

    # If number(n) key is not found in dictionary
    except KeyError:
        resultado = fibonacci_dinamico(
            n-1, memo) + fibonacci_dinamico(n-2, memo)
        # Adding result to dictionary with key number (n)
        memo[n] = resultado

        return resultado


if __name__ == '__main__':
    # Set recursion limit nos ayuda a que python pueda hacer recursivamente mas de 998 veces
    sys.setrecursionlimit(10000)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
