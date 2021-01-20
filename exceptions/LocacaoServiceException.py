
from models.Filme import Filme

class LocacaoServiceException(Exception):
    serialVersionUid = 8954623558516512822

    def __init__(self, msg, *args, **kwargs):
        # INVOCA O CONSTRUTOR DA CLASSE PAI
        super(LocacaoServiceException, self).__init__(msg, *args, **kwargs)
        
        self.mensagem = msg
        

    # def __str__(self, *args, **kwargs):
    #     return "Não é possível realizar a locação para o filme: %s"%(self.filme.nome)

    # @property
    # def filme(self):
    #     return self._filme

    # @filme.setter
    # def filme(self, filme):
    #     if isinstance(filme, Filme):
    #         self.filme = filme
    #     else:
    #         error = "É necessário um objeto do tipo %s, não %s"%(Filme, type(filme))
    #         raise TypeError(error)