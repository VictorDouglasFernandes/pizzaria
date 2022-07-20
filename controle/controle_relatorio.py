from controle.controle_pedido import ControlePedido
from tela.tela_relatorio import TelaRelatorio
from entidade.relatorio import Relatorio


class ControleRelatorio:
    def __init__(self, controle_pedido: ControlePedido):
        self.__tela_relatorio = TelaRelatorio()
        self.__controle_pedido = None
        if isinstance(controle_pedido, ControlePedido):
            self.__controle_pedido = controle_pedido

    def menu(self):
        retorno = self.__tela_relatorio.menu()
        if retorno == 0:
            return
        funcao_opcoes = {1: self.gerar_relatorio}
        funcao_opcoes[retorno]()
        self.menu()

    def gerar_relatorio(self):
        try:
            data = self.__tela_relatorio.gerar_relatorio()
        except:
            return self.__tela_relatorio.mensagem("Valor de data inválido")

        relatorio = Relatorio(data)
        for pedido in self.__controle_pedido.pedidos:
            if pedido.data.year == data.year and pedido.data.month and data.month and pedido.data.day == data.day:
                relatorio.incluir_pedido(pedido)
        if relatorio.pedidos:
            self.__tela_relatorio.mostrar_relatorio(relatorio)
        else:
            self.__tela_relatorio.mensagem("Pedidos não encontrados")
