from models.Filme import Filme

class FilmeSemEstoqueException(Exception):
    serialVersionUid = 3864394934824610211

    def __init__(self, msg, filme=None, *args, **kwargs):
        super(FilmeSemEstoqueException, self).__init__(msg, *args, **kwargs)
        self.msg = msg
        self.filme = filme

    def __str__(self, *args, **kwargs):
        if self.filme:
            return "Não há estoque disponível para o filme: %s"%(self.filme)
        return self.msg

    @property
    def filme(self):
        return self._filme

    @filme.setter
    def filme(self, filme):
        if isinstance(filme, Filme) or filme == None:
            self._filme = filme
        else:
            error = "É necessário um objeto do tipo %s, não %s"%(Filme, type(filme))
            raise TypeError(error)