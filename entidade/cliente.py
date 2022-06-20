from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str):
        super().__init__(nome, cpf)
        self.__endereco = None
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco
