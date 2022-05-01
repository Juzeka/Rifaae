from .models import Cota


class CotaService:

    def __init__(self, **kwargs):
        self.cotas = kwargs.get('cotas', 0)
        self.rifa = kwargs.get('rifa')

    def listar_cotas(self):
        return [x for x in range(1, self.cotas) if self.cotas > 0]

    def criar_cotas(self):
        self.cotas = self.rifa.cotas

        for cota in self.listar_cotas():
            Cota.objects.create(numero=cota, rifa=self.rifa.pk)