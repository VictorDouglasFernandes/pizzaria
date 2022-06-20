

class Ingrediente:
    def __init__(self, id: int, nome: str):
        self.__id = None
        self.__nome = None
        if isinstance(id, int):
            self.__id = id
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
