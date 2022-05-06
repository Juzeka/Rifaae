from .models import Cota


class CotaService:

    def __init__(self, **kwargs):
        self.cotas = kwargs.get('cotas', 0)
        self.rifa = kwargs.get('rifa')

    def listar_cotas(self):
        self.cotas += 1
        return [c for c in range(1, self.cotas) if self.cotas > 0]

    def criar_cotas(self):
        self.cotas = self.rifa.cotas

        for cota in self.listar_cotas():
            Cota(valor=cota, rifa=self.rifa).save()