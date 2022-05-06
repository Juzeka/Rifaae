from django.test import TestCase
from rifas.factory import RifaFactory
from rifas.services import RifaService


class RifaServiceTestCase(TestCase):
    class_service = RifaService

    def setUp(self):
        self.rifa1 = RifaFactory(cotas=2)

    def test_associar_cotas(self):
        self.class_service(rifa=self.rifa1).associar_cotas()

        self.assertEqual(self.rifa1.pk, self.rifa1.cota.first().rifa.pk)