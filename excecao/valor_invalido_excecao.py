class ValorInvalidoExcecao(Exception):
    def __init__(self):
        super().__init__('Valor Inválido')