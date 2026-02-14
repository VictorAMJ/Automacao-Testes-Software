import unittest

def validar_formato_cpf(cpf):
    if not isinstance(cpf, str):
        return False
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():
        return False
    return True


class TestValidadorFormatoCPF(unittest.TestCase):

    def test_cpf_valido(self):
        self.assertTrue(validar_formato_cpf("12345678901"))

    def test_cpf_com_letra(self):
        self.assertFalse(validar_formato_cpf("1234567890A"))

    def test_cpf_tamanho_curto(self):
        self.assertFalse(validar_formato_cpf("1234567890"))

    def test_cpf_tamanho_longo(self):
        self.assertFalse(validar_formato_cpf("123456789012"))

    def test_cpf_tipo_incorreto(self):
        self.assertFalse(validar_formato_cpf(12345678901))


if __name__ == "__main__":
    unittest.main()
