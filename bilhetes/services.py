from datetime import datetime
import random, string


class BilheteService:

    def __init__(self, **kwargs):
        ...

    def gerar_numero(self, initial, stop):
        return random.randint(initial, stop)

    def gerar_parte_numerica(self):
        first = self.gerar_numero(1, 9)
        last = datetime.now().microsecond

        if self.gerar_numero(0, 1):
            return '{}{}'.format(first, last)

        return '{}{}'.format(last, first)

    def gerar_parte_letras(self):
        return ''.join(random.choices(population=string.ascii_uppercase, k=3))

    def gerar_numero_bilhete(self):
        return '{}{}'.format(
            self.gerar_parte_letras(),
            self.gerar_parte_numerica()
        )