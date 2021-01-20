from models.Filme import Filme
from models.Locacao import Locacao
from models.Usuario import Usuario

from exceptions.LocacaoServiceException import LocacaoServiceException
from exceptions.FilmeSemEstoque import FilmeSemEstoqueException

from datetime import timedelta
from datetime import date

class LocacaoService:
    """
    Objeto service para realizar as operações relacionadas à locação de filmes

    Operações:
        - calcular_preco_filme
        - alugar_filme
    """

    def calcular_preco_filmes(self, filmes):
        """
        Calcula o preço total de uma locação à partir dos filmes alugados, 
        aplicando descontos de acordo com a quantidade de filmes.
        
        - 25% sobre o terceiro filme.
        - 50% sobre o quarto filme.
        - 75% sobre o quinto filme.
        - 100% sobre o sexto filme.

        Entrada:
         - Lista de filmes <class 'Filme'> 

        Saída:
         - Preço final acumulado <class 'Float'>
        """
        vl_total = 0
        for idx, filme in enumerate(filmes):
            if idx == 2:
                vl_total += filme.preco_locacao - ( filme.preco_locacao * 0.25)
            elif idx == 3:
                vl_total += filme.preco_locacao - ( filme.preco_locacao * 0.50)
            elif idx == 4:
                vl_total += filme.preco_locacao - ( filme.preco_locacao * 0.75)
            elif idx == 5:
                pass
            else:
                vl_total += filme.preco_locacao
        return vl_total

    def alugar_filme(self, usuario=None, filmes=None):
        """
        Realiza as iterações necessárias para a operação de locação

        Entrada:
         - usuário <class 'Usuario'>
         - filmes [ <class 'Filme'> ]

        Saída:
         - locacao <class 'Locacao'>
        """
        if not filmes:
            raise LocacaoServiceException("Nenhum filme foi informado")
        if not usuario:
            raise LocacaoServiceException("Nenhum usuário foi informado")
        
        for filme in filmes:
            if filme.estoque == 0:
                raise FilmeSemEstoqueException("Filme sem Estoque")
        
        locacao = Locacao(usuario, 0.0, filmes )

        locacao.valor = self.calcular_preco_filmes(filmes)

        return locacao
