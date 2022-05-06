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

    @parameterized.expand(INIT_AND)
    def test_gerar_numero(self, inicio, fim):
        result = self.class_service().gerar_numero(inicio, fim)
        is_range = result >= inicio or result <= fim
        
        self.assertTrue(is_range)

    def test_gerar_numero_bilhete(self):
        result = self.class_service().gerar_numero_bilhete()

        letras = result
        numeros = letras

        for digit in string.digits:
            letras = letras.replace(digit, '')

        for number in string.ascii_uppercase:
            numeros = numeros.replace(number, '')


        self.assertEqual(len(result), 10)
        self.assertTrue(letras.isascii())
        self.assertTrue(numeros.isdigit())