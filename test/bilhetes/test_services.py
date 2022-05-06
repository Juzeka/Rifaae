import string
from django.test import TestCase
from parameterized import parameterized
from bilhetes.services import BilheteService
from bilhetes.models import Bilhete


INIT_AND = [
    (1, 9), (10, 99), (100, 999)
]


class BilheteServiceTestCase(TestCase):
    class_service = BilheteService
    class_model = Bilhete

    def setUp(self):
        ...

    def format_replace_variavel(self, variavel, iterador):
        for iter in iterador:
            variavel = variavel.replace(iter, '')

        return variavel

    @parameterized.expand(INIT_AND)
    def test_gerar_numero(self, inicio, fim):
        result = self.class_service().gerar_numero(inicio, fim)
        is_range = result >= inicio or result <= fim
        
        self.assertTrue(is_range)

    def test_gerar_parte_numerica(self):
        result = self.class_service().gerar_parte_numerica()

        self.assertTrue(self.format_replace_variavel(
            result, string.ascii_uppercase).isdigit()
        )

    def test_gerar_parte_alfabetica(self):
        result = self.class_service().gerar_parte_alfabetica()

        self.assertTrue(self.format_replace_variavel(
            result, string.digits).isascii()
        )

    def test_gerar_numero_bilhete(self):
        result = self.class_service().gerar_numero_bilhete()

        letras = result
        numeros = letras

        self.assertTrue(self.format_replace_variavel(
            letras, string.digits).isascii()
        )
        self.assertTrue(self.format_replace_variavel(
            numeros, string.ascii_uppercase).isdigit()
        )