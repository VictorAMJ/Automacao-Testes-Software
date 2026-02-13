import unittest

def calcular_desconto(valor, percentual):
    if percentual > 50:
        percentual = 50

    desconto = valor * percentual / 100
    return valor - desconto


class TestDescontos(unittest.TestCase):
    def test_desconto_comum(self):
        resultado = calcular_desconto(100,10)
        self.assertEqual(resultado, 90)

    def test_limite_segurança(self):
        resultado = calcular_desconto(100,70)
        self.assertEqual(resultado, 50)

    def test_valor_zero(self):
        resultado = calcular_desconto(0, 10)
        self.assertEqual(resultado, 0)
        
if __name__ == "__main__":
    unittest.main()



