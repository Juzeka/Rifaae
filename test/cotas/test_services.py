from django.test import TestCase
from parameterized import parameterized
from cotas.services import CotaService
from cotas.models import Cota
from rifas.factory import RifaFactory


QNTD_COTAS = [
    (0,), (5,), (60,),
]

class CotaServiceTestCase(TestCase):
    class_service = CotaService
    class_model = Cota

    def setUp(self):
        ...

    @parameterized.expand(QNTD_COTAS)
    def test_listar_cotas(self, cotas):
        response = self.class_service(cotas=cotas).listar_cotas()

        self.assertEqual(len(response), cotas)

    @parameterized.expand(QNTD_COTAS)
    def test_criar_cotas(self, cotas):
        self.class_service(rifa=RifaFactory(cotas=cotas)).criar_cotas()

        is_result = Cota.objects.all().exists()

        if cotas:
            self.assertTrue(is_result)
        else:
            self.assertFalse(is_result)

