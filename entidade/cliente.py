from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str):
        pass

    @property
    def endereco(self):
        pass

    @endereco.setter
    def endereco(self, endereco: str):
        pass
