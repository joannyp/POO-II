class Cadastro:

    __slots__ = ['_listapessoas']

    def __init__(self):
        self._listapessoas = [] #vai inicializar com uma lista de pessoas vazia

    def cadastra(self, pessoa):
        existe = self.busca(pessoa.cpf) #vai verificar se a pessoa que esta tentando cadastrar ja existe na base de dados
        if(existe == None):
            self._listapessoas.append(pessoa)
            return True #retorna true quando consegue fazer o cadastro
        else:
            return False #retorna false caso contrario

    def busca(self, cpf):
        for lp in self._listapessoas: #faz um loop na lista de pessoas buscando se o cpf ja existe na base de dados e retorna a pessoa dona do cpf
            if lp.cpf == cpf:
                return lp

        return None
