from entidade.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, senha: str):
        super().__init__(nome, cpf)
        self.__senha = None
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if isinstance(senha, str):
            self.__senha = senha
