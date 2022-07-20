from tela.tela import Tela
from datetime import datetime
import PySimpleGUI as sg


class TelaRelatorio(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela Relatório', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Gerar relatório', "RD1", key='1')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao

    def gerar_relatorio(self):
        layout = [
            [sg.Text('Gerar relatório', font=("Helvica", 15))],
            [sg.Text('Data (DD/MM/AAAA): '), sg.In(key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return datetime.strptime(values['data'], "%d/%m/%Y")

    def mostrar_relatorio(self, relatorio):
        column = []
        for pedido in relatorio.pedidos:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('ID: ' + str(pedido.id))],
                [sg.Text('CPF cliente: ' + pedido.cliente.cpf)],
                [sg.Text('Endereco: ' + pedido.endereco)],
                [sg.Text('Pagamento: ' + pedido.pagamento)],
                [sg.Text('Pizzas: ')],
            ])
            for pizza in pedido.pizzas:
                column.append([sg.Text(' - ' + pizza.nome)])

        layout = [
            [sg.Text('Detalhes' + relatorio.data.strftime("%d/%m/%Y"), font=("Helvica", 15))],
            [sg.Column(column, scrollable=True, vertical_scroll_only=True)],
            [sg.Button('Voltar')],
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()

    def mensagem(self, mensagem: str):
        sg.popup('', mensagem)
