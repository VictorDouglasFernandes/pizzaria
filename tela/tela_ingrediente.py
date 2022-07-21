from tela.tela import Tela
from excecao.valor_invalido_excecao import ValorInvalidoExcecao
import PySimpleGUI as sg


class TelaIngrediente(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela Ingrediente', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar', "RD1", key='1')],
            [sg.Radio('Adicionar', "RD1", key='2')],
            [sg.Radio('Alterar', "RD1", key='3')],
            [sg.Radio('Excluir', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        if button in (None, 'Cancelar'):
            opcao = 0
        self.__window.Close()
        return opcao

    def adicionar(self):
        layout = [
            [sg.Text('Adicionar Ingrediente', font=("Helvica", 25))],
            [sg.Text('ID: '), sg.In(key='id')],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        try:
            id = int(values['id'])
        except:
            raise ValorInvalidoExcecao()
        return {"id": id, "nome": values['nome']}

    def pegar_id(self):
        layout = [
            [sg.Text('Buscar Ingrediente', font=("Helvica", 25))],
            [sg.Text('ID: '), sg.In(key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        try:
            return int(values['id'])
        except:
            raise ValorInvalidoExcecao()

    def alterar(self):
        layout = [
            [sg.Text('Alterar Ingrediente', font=("Helvica", 25))],
            [sg.Text('ID: '), sg.In(key='id')],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        try:
            id = int(values['id'])
        except:
            raise ValorInvalidoExcecao()
        return {"id": id, "nome": values['nome']}

    def mostrar_ingredientes(self, ingredientes):
        column = [[sg.Text('Detalhes', font=("Helvica", 15))]]
        for ingrediente in ingredientes:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('ID:' + str(ingrediente.id))],
                [sg.Text('Nome:' + ingrediente.nome)],
            ])
        column.append([sg.Button('Voltar')])
        layout = [[sg.Column(column, scrollable=True, vertical_scroll_only=True)]]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()

    def mensagem(self, mensagem: str):
        sg.popup('', mensagem)
