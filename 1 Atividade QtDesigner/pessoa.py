class Pessoa:

    __slots__ = ['_nome', '_cpf', '_nascimento', '_endereco']

    def __init__(self, nome, cpf, nascimento, endereco):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
        self._endereco = endereco


    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def endereco(self):
        return self._endereco

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco


