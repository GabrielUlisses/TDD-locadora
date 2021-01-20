from datetime import timedelta
from datetime import date

class Locacao(object):
    def __init__(self, usuario, valor, filmes, data_locacao=None, data_retorno=None, *args, **kwargs):
        self.data_locacao = data_locacao or self.get_data_locacao()
        self.data_retorno = data_retorno or self.set_data_devolucao()
        self.valor = valor
        self.filmes = filmes
        self.usuario = usuario

    def get_data_locacao(self):
        return date.today()

    def set_data_devolucao(self):
        devolucao = date.today() + timedelta(days=7)
        if devolucao.weekday == 6:
            devolucao += timedelta(days=1)
        return devolucao