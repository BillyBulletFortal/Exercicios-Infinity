# Desenvolva um aplicativo de gerenciamento de tarefas
# em python. Crie duas classes, Tarefa e Projeto, com uma
# associação unidirecional. Permita que as tarefas sejam
# associadas a projetos e que você possa listar as tarefas
# de um projeto em particular.



class Tarefa:
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

class Projeto:
    def __init__(self, nome):
        self.__nome = nome
        self.__tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.__tarefas.append(tarefa)

    def listar_tarefas(self):
        print(f"Tarefas do projeto {self.__nome}:")
        for tarefa in self.__tarefas:
            print(f"- {tarefa._Tarefa__nome}: {tarefa._Tarefa__descricao}")

projeto1 = Projeto("Lista de Compras")
item1 = input("Digite o primeiro item da lista:   > ")
item2 = input("Digite o segundo item da lista:  > ")
item3 = input("Digite o terceiro item da lista:  > ")

tarefa1 = Tarefa("Item 1 =   ", item1)
tarefa2 = Tarefa("Item 2 =   ", item2)
tarefa3 = Tarefa("Item 3 =   ", item3)

# Adicionando as tarefas ao projeto
projeto1.adicionar_tarefa(tarefa1)  
projeto1.adicionar_tarefa(tarefa2)
projeto1.adicionar_tarefa(tarefa3)
projeto1.listar_tarefas()
