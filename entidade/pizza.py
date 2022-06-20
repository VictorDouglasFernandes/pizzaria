

class Pizza:
    ultimo_id = 0
    
    def __init__(self, nome: str, sabor: str, borda: str, preco: float):
        self.__id_ingredientes = []

        Pizza.ultimo_id = Pizza.ultimo_id + 1
        self.__id = Pizza.ultimo_id

        self.__nome = None
        self.__sabor = None
        self.__borda = None
        self.__preco = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(sabor, str):
            self.__sabor = sabor
        if isinstance(borda, str):
            self.__borda = borda
        if isinstance(preco, float):
            self.__preco = preco

    @property
    def id(self):
        return self.__id
    
    @property
    def id_ingredientes(self):
        return self.__id_ingredientes
    
    def incluir_id_ingrediente(self, id: int):
        if isinstance(id, int):
            if id not in self.__id_ingredientes:
                self.__id_ingredientes.append(id)

    def excluir_id_ingrediente(self, id: int):
        if isinstance(id, int):
            if id in self.__id_ingredientes:
                self.__id_ingredientes.remove(id)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def sabor(self):
        return self.__sabor

    @sabor.setter
    def sabor(self, sabor: str):
        if isinstance(sabor, str):
            self.__sabor = sabor

    @property
    def borda(self):
        return self.__borda

    @borda.setter
    def borda(self, borda: str):
        if isinstance(borda, str):
            self.__borda = borda

    @property
    def preco(self):
        return  self.__preco

    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__preco = preco
