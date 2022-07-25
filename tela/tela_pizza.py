from tela.tela import Tela
from excecao.valor_ingrediente_invalido_excecao import ValorIngredienteInvalidoExcecao
from excecao.valor_invalido_excecao import ValorInvalidoExcecao
import PySimpleGUI as sg


class TelaPizza(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela Pizzas', font=("Helvica", 25))],
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
            [sg.Text('Adicionar Pizza', font=("Helvica", 25))],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Text('Sabor: '), sg.In(key='sabor')],
            [sg.Text('Borda: '), sg.In(key='borda')],
            [sg.Text('* Separados por vírgular ex.: 1,3,4,7')],
            [sg.Text('Ingredientes: '), sg.In(key='ingredientes', size=(40,1))],
            [sg.Text('Preço: '), sg.In(key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        try:
            ingredientes = [int(id) for id in values['ingredientes'].split(",")]
        except:
            raise ValorIngredienteInvalidoExcecao()
        try:
            preco = float(values['preco'])
        except:
            raise ValorInvalidoExcecao()

        return {
            "nome": values['nome'],
            "sabor": values['sabor'],
            "borda": values['borda'],
            "id_ingredientes": ingredientes,
            "preco": preco
        }

    def pegar_nome_sabor_borda(self):
        layout = [
            [sg.Text('Buscar Pizza', font=("Helvica", 25))],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Text('Sabor: '), sg.In(key='sabor')],
            [sg.Text('Borda: '), sg.In(key='borda')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        return {
            "nome": values['nome'],
            "sabor": values['sabor'],
            "borda": values['borda'],
        }

    def alterar(self):
        layout = [
            [sg.Text('Alterar Pizza', font=("Helvica", 25))],
            [sg.Text('Nome: '), sg.In(key='nome')],
            [sg.Text('Sabor: '), sg.In(key='sabor')],
            [sg.Text('Borda: '), sg.In(key='borda')],
            [sg.Text('* Separados por vírgular ex.: 1,3,4,7')],
            [sg.Text('Ingredientes: '), sg.In(key='ingredientes', size=(40, 1))],
            [sg.Text('Preço: '), sg.In(key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        button, values = self.__window.Read()
        self.__window.close()
        if button in (None, 'Cancelar'):
            return 0
        try:
            ingredientes = [int(id) for id in values['ingredientes'].split(",")]
        except:
            raise ValorIngredienteInvalidoExcecao()
        try:
            preco = float(values['preco'])
        except:
            raise ValorInvalidoExcecao()

        return {
            "nome": values['nome'],
            "sabor": values['sabor'],
            "borda": values['borda'],
            "id_ingredientes": ingredientes,
            "preco": preco
        }

    def mostrar_pizzas(self, pizzas):
        column = [[sg.Text('Detalhes', font=("Helvica", 15))]]
        for pizza in pizzas:
            column.extend([
                [sg.Text('- - - -')],
                [sg.Text('ID:' + str(pizza.id))],
                [sg.Text('Nome:' + pizza.nome)],
                [sg.Text('Sabor:' + pizza.sabor)],
                [sg.Text('Borda:' + pizza.borda)],
                [sg.Text('Ingredientes:' + ",".join([str(x) for x in pizza.id_ingredientes]))],
                [sg.Text('Preço:' + str(pizza.preco))],
            ])
        column.append([sg.Button('Voltar')])
        layout = [[sg.Column(column, scrollable=True, vertical_scroll_only=True)]]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()
