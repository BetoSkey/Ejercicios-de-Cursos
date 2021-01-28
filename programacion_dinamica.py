import sys
import unittest

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

class prueba_caja_cristal(unittest.TestCase):
  #Test fibonacci reursivo con memoizacion
  def test_fibonacci_memoizacion_grande(self):
    numero = 3000
    objetivo = 664390460366960072280217847866028384244163512452783259405579765542621214161219257396449810982999820391132226802809465132446349331994409434926019045342723749188530316994678473551320635101099619382973181622585687336939784373527897555489486841726131733814340129175622450421605101025897173235990662770203756438786517530547101123748849140252686120104032647025145598956675902135010566909783124959436469825558314289701354227151784602865710780624675107056569822820542846660321813838896275819753281371491809004412219124856375121694811728724213667814577326618521478357661859018967313354840178403197559969056510791709859144173304364898001

    resultado = fibonacci_dinamico(numero)

    self.assertEqual(resultado, objetivo)


if __name__ == '__main__':
    # Set recursion limit nos ayuda a que python pueda hacer recursivamente mas de 998 veces
    sys.setrecursionlimit(10002)
    unittest.main()
