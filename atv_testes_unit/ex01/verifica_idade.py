import unittest

#função testada:
def pode_dirigir(idade):
    if idade >= 18:
        return True
    else:
        return False


#classe de teste:
class TestPodeDirigir(unittest.TestCase):

    #se positivo:
    def test_maior_idade(self):
        self.assertEqual(pode_dirigir(20), True)

    #se negativo:
    def test_menor_idade(self):
        self.assertEqual(pode_dirigir(16), False)


#executa testes:
if __name__ == "__main__":
    unittest.main()   


'''Como rodar: python nome_do_arquivo.py'''





