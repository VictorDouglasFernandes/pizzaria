from entidade.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, senha: str):
        pass

    @property
    def senha(self):
        pass

    @senha.setter
    def senha(self, senha: str):
        pass
