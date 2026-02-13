import unittest

def cadastrar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha muito curta")
    return "Senha cadastrada com sucesso"

class TestCadastroSenha(unittest.TestCase):
    def test_sucesso(self):
        resultado = cadastrar_senha("1234567890")
        self.assertEqual(resultado, "Senha cadastrada com sucesso")
        
    def test_senha_curta(self):
        with self.assertRaises(ValueError):
            cadastrar_senha("123")

if __name__ == "__main__":
    unittest.main()

















