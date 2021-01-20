
"""


>>> LOCACAO SEM FILME: MUST FAIL -> LocacaoServiceException

>>> LOCACAO SEM USUÁRIO: MUST FAIL -> LocacaoServiceException

>>> LOCACAO COM FILME SEM ESTOQUE: MUST FAIL -> FilmeSemEstoqueException

>>> LOCACAO DE UM FILME: MUST PASS
    --> DEVOLUCÃO NAO DEVE CAIR NUM DOMINGO

>>> LOCACAO DE DOIS FILMES: MUST PASS 

>>> LOCACAO DE TRÊS FILMES: MUST PASS 
    --> APLICAR 25% DESCONTO NO TERCEIRO FILME

>>> LOCACAO DE QUATRO FILMES: MUST PASS 
    --> APLICAR 50% DESCONTO NO QUARTO FILME

>>> LOCACAO DE QUATRO FILMES: MUST PASS 
    --> APLICAR 75% DESCONTO NO QUINTO FILME

>>> LOCACAO DE QUATRO FILMES: MUST PASS 
    --> APLICAR 100% DESCONTO NO SEXTO FILME

"""

from models.Filme import Filme
from models.Locacao import Locacao
from models.Usuario import Usuario

from exceptions.FilmeSemEstoque import FilmeSemEstoqueException
from exceptions.LocacaoServiceException import LocacaoServiceException

from services.LocacaoService import LocacaoService

from datetime import timedelta
from datetime import date

import unittest

class TestLocacaoService(unittest.TestCase):
    service = LocacaoService()
    usuario = Usuario('André Garcia Alves', 32)

    def test_alugar_filme_sem_filme(self):
        with self.assertRaises(LocacaoServiceException):
            self.service.alugar_filme(self.usuario, None)
    
    def test_alugar_filme_sem_usuario(self):
        filmes = [ Filme("Crocodilo Dunde", 3, 12.50 ) ]
        with self.assertRaises(LocacaoServiceException):
            self.service.alugar_filme(None, filmes)

    def test_alugar_filme_sem_estoque(self):
        filmes = [ Filme("Matrix I", 0, 14.25) ]
        with self.assertRaises(FilmeSemEstoqueException):
            locacao = self.service.alugar_filme(self.usuario, filmes)

    def test_alugar_filme(self):
        filmes = [ Filme("Um vampiro no brooklyn", 2, 12.50) ]
        hoje = date.today()
        devolucao = hoje + timedelta(days=7)
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertTrue(locacao != None)
        self.assertIsInstance(locacao, Locacao)
        self.assertEqual(locacao.data_locacao, hoje)
        self.assertEqual(locacao.valor, 12.50)
        if devolucao.weekday == 6:
            self.assertEqual(locacao.data_retorno, devolucao + timedelta(days=1))
        else:
            self.assertEqual(locacao.data_retorno, devolucao)

    def test_alugar_um_filme(self):
        filmes = [ Filme("Matrix I", 2, 14.25) ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(filmes[0].preco_locacao, locacao.valor )

    def test_alugar_dois_filmes(self):
        filmes = [
            Filme("Matrix II", 1, 12.90),
            Filme("Cegos surdos e Loucos", 1, 8.50),
        ]

        locacao = self.service.alugar_filme(self.usuario, filmes)

        self.assertEqual( len(locacao.filmes), 2 )
        self.assertEqual( locacao.valor, 21.40 )

    def test_alugar_tres_filmes(self):
        filmes = [
            Filme("Matrix III", 2, 12.00),
            Filme("Madagascar", 2, 9.50),
            Filme("Piratas do CAribe I", 2, 9.50),
        ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(locacao.valor, 28.625 )

    def test_alugar_quatro_filmes(self):
        filmes = [
            Filme("O poderoso chefão II", 2, 14.00),
            Filme("Anjos da Lei II", 2, 9.50),
            Filme("A pequena sereia", 1, 10.00),
            Filme("Alice no pais da maravilhas", 3, 13.30),
        ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(locacao.valor, 37.65 )

    def test_alugar_cinco_filmes(self):
        filmes = [
            Filme("O segredo dos animais", 2, 10.00),
            Filme("Anjos da Lei", 2, 11.20),
            Filme("O poderoso chefão", 1, 15.00),
            Filme("Piratas do Caribe II", 3, 9.75),
            Filme("MadMax", 2, 12.40),
        ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(locacao.valor, 40.425000000000004 )

    def test_alugar_seis_filmes(self):
        filmes = [
            Filme("Matrix III", 2, 12.00),
            Filme("Madagascar", 2, 9.50),
            Filme("Piratas do CAribe I", 2, 9.50),
            Filme("Anjos da Noite", 2, 12.00),
            Filme("Os estranhos", 2, 9.00),
            Filme("Piratas do Caribe III", 2, 11.00),
        ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(locacao.valor, 36.875 )

    def test_alugar_sete_filmes(self):
        filmes = [
            Filme("Matrix III", 2, 12.00),
            Filme("Madagascar", 2, 9.50),
            Filme("Piratas do CAribe I", 2, 9.50),
            Filme("Anjos da Noite", 2, 12.00),
            Filme("Os estranhos", 2, 9.00),
            Filme("Piratas do Caribe III", 2, 11.00),
            Filme("Os estranhos", 2, 9.00)
        ]
        locacao = self.service.alugar_filme(self.usuario, filmes)
        self.assertEqual(locacao.valor, 45.875 )

unittest.main(verbosity=2)