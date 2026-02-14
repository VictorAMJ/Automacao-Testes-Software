import unittest

def validar_senha_avancada(senha):
    if len(senha) < 8:
        return False

    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)

    return tem_numero and tem_maiuscula


class TestValidadorSenhaAvancada(unittest.TestCase):

    def test_senha_valida(self):
        self.assertTrue(validar_senha_avancada("Senha123"))

    def test_senha_curta(self):
        self.assertFalse(validar_senha_avancada("Curta1"))

    def test_sem_numero(self):
        self.assertFalse(validar_senha_avancada("SemNumero"))

    def test_sem_maiuscula(self):
        self.assertFalse(validar_senha_avancada("semliteramaiuscula1"))


if __name__ == "__main__":
    unittest.main()
