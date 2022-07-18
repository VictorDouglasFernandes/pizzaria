from tela.tela import Tela
import PySimpleGUI as sg


class TelaPizza(Tela):
    def __init__(self):
        self.__window = None

    def menu(self):
        layout = [
            [sg.Text('Tela sistema', font=("Helvica", 25))],
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

    def pegar_id_ingredientes(self):
        while True:
            try:
                print("Separados por vírgula x,y,z,...")
                id_ingredientes = input("ID ingredientes: ")
                id_ingredientes = [
                    int(id) for id in id_ingredientes.split(",")
                ]
                return id_ingredientes
            except:
                print("Valor inválido")

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
        print(values)
        # print("==== Adicionar Pizza ====")
        # nome = input("Nome: ")
        # sabor = input("Sabor: ")
        # borda = input("Borda: ")
        # id_ingredientes = self.pegar_id_ingredientes()
        # while True:
        #     try:
        #         preco = float(input("Preço: "))
        #         break
        #     except:
        #         print("Valor inválido")

        # return {
        #     "nome": nome,
        #     "sabor": sabor,
        #     "borda": borda,
        #     "id_ingredientes": id_ingredientes,
        #     "preco": preco
        # }

    def pegar_nome_sabor_borda(self):
        nome = input("Nome: ")
        sabor = input("Sabor: ")
        borda = input("Borda: ")
        return {"nome": nome, "sabor": sabor, "borda": borda}

    def alterar(self):
        print("==== Alterar Pizza ====")
        nome = input("Nome: ")
        sabor = input("Sabor: ")
        borda = input("Borda: ")
        id_ingredientes = self.pegar_id_ingredientes()
        while True:
            try:
                preco = float(input("Preço: "))
                break
            except:
                print("Valor inválido")
        return {
            "nome": nome,
            "sabor": sabor,
            "borda": borda,
            "id_ingredientes": id_ingredientes,
            "preco": preco
        }

    def mostrar_pizza(self, pizza):
        layout = [
            [sg.Text('Detalhes', font=("Helvica", 15))],
            [sg.Text('ID:' + str(pizza.id))],
            [sg.Text('Nome:' + pizza.nome)],
            [sg.Text('Sabor:' + pizza.sabor)],
            [sg.Text('Borda:' + pizza.borda)],
            [sg.Text('Ingredientes:' + ",".join([str(x) for x in pizza.id_ingredientes]))],
            [sg.Text('Preço:' + str(pizza.preco))],
            [sg.Button('Voltar')]
        ]
        self.__window = sg.Window('Sistema Pizzaria').Layout(layout)
        self.__window.Read()
        self.__window.close()

    def mensagem(self, mensagem: str):
        print(mensagem)
