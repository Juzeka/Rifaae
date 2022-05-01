from cotas.services import CotaService


class RifaService:

    def __init__(self, **kwargs):
        self.rifa = kwargs.get('rifa')

    def associar_cotas(self):
        CotaService(rifa=self.rifa).criar_cotas()