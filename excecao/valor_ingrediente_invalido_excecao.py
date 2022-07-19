class ValorIngredienteInvalidoExcecao(Exception):
    def __init__(self):
        super().__init__('Valor do Ingrediente Inválido')
