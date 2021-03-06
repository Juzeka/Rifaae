from datetime import datetime
import random, string


class BilheteService:

    def __init__(self, **kwargs):
        ...

    def gerar_numero(self, init, stop):
        return random.randint(init, stop)

    def gerar_parte_numerica(self):
        first = self.gerar_numero(1, 9)
        last = datetime.now().microsecond

        if self.gerar_numero(0, 1):
            return '{}{}'.format(first, last)

        return '{}{}'.format(last, first)

    def gerar_parte_alfabetica(self):
        return ''.join(random.choices(population=string.ascii_uppercase, k=3))

    def gerar_numero_bilhete(self):
        return '{}{}'.format(
            self.gerar_parte_alfabetica(),
            self.gerar_parte_numerica()
        )