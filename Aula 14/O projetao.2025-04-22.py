#Imagine que você foi contratado para desenvolver um sistema inovador de
#gerenciamento de reservas para um hotel boutique em uma cidade turística.

#O hotel, conhecido como "Refúgio dos Sonhos"

#, precisa de um sistema que
#permita gerenciar a disponibilidade dos quartos, as reservas dos hóspedes e
#os dados dos clientes de forma eficiente e intuitiva.

#Sua missão é criar uma aplicação interativa que atenda a essas necessidades
#utilizando Programação Orientada a Objetos (POO) e a biblioteca Flet para
#a interface gráfica.

"""Atributos do cliente:
Nome
Telefone
E-mail
ID único
"""


'''colas
class quarto:
  def __init__(self, number:str, vacancy:bool, reserva:int):
    self.number = number
    self.vacancy = vacancy
    self.reserva = reserva
    
  def comer(self, comida:str):
    return f"O cachorro {self.number} comeu {comida}"
  def dormir(self):
    return f"O cachorro {self.number} dormiu"
  def acordar(self):
    return f"O cachorro {self.number} acordou"


class hospede:
  def __init__(self, nome, vacancy, peso, idade, pedigree:bool):
    super().__init__(nome, vacancy, peso, idade)
    self.pedigree = pedigree
  def emitirSom(self):
    return "Au auuu"
  def pegarBolinha(self):
    return f"O cachorro {self.nome} pegou a bolinha"

class reserva:
  def __init__(self, nome, raca, peso, idade, porte:str):
    super().__init__(nome, raca, peso, idade)
    self.porte = porte
 def reservar(self):
    if self.reserva == False:
        self.reserva = True
        return  f"O quarto {self.number}  foi RESERVADO"
    else:
      return f"Confira os dados, este quarto já está RESERVADO"
    
    def liberar(self):
        if self.reserva == True:
           self.reserva = False
           return  f"O quarto {self.number}  está LIVRE para ser reservado"
        else:
            return f"Confira os dados, este quarto já está reservado"
  
class conta:
  def __init__(self, nome, raca, peso, idade):
    super().__init__(nome, raca, peso, idade)
  def emitirSom(self):
    return "piu piu"
  def voar(self):
    return f"O passaro {self.nome} voou"

cachorrim = Cachorro(nome="Spike", raca="Pitbull", peso=12.5, idade=4, pedigree=True)
gatim = Gato(nome="Floquinho", raca="Angorá", peso=4.8, idade=7, porte="médio")
passarim = Passaro(nome="PiuPiu", raca="Canário", peso=0.4, idade=2)
porquim = Animal(nome="Baby", raca="Bacon", peso=60, idade=1)

print(cachorrim.emitirSom())
print(gatim.emitirSom())
print(passarim.emitirSom())

'''











"""

class Cliente:
  def __init__(self, username:str, email:str, senha:str):
    self.username = username
    self.email = email
    self.senha = senha
  def mostrarInfos(self):
    return f"{self.username}  |  {self.email}  |  {self.senha}"

user1 = Cliente(username="Cleitim", email="cleitim_da_tuf@email.com", senha="DeusEhFiel")
user2 = Cliente(username="Toim", email="toim_da_cearamo@email.com", senha="123456")
user1.email = 10
user1.senha = "a"
print(user1.mostrarInfos())
print(user2.mostrarInfos())

"""










"""
class Cliente:
  def __init__(self, username:str, email:str, senha:str):
    self.username = username
    self.__email = email
    self.__senha = senha
    
  def mostrarEmail(self):
    senha_digitada = input("Digite sua senha atual: ")
    if senha_digitada == self.__senha:
      return self.__email
    else:
      return "sai dai doido. ACESSO NEGADO"
    
  def mudarEmail(self, novo_email):
    senha_digitada = input("Digite sua senha atual: ")
    if senha_digitada == self.__senha:
      if "@" in novo_email:
        self.__email = novo_email
        return f"Email alterado com sucesso seu novo email é {novo_email}"
      else:
        return "Email de formato inválido"
    else:
      return "sai dai doido. ACESSO NEGADO"
    

user1 = Cliente(username="Cleitim", email="cleitim_da_tuf@email.com", senha="DeusEhFiel")
user2 = Cliente(username="Toim", email="toim_da_cearamo@email.com", senha="123456")

print(user1.mostrarEmail())
print(user1.mudarEmail("10@gmail.com"))
print(user1.mostrarEmail())
"""








lista_de_clientes = []



class Cliente: #objeto cliente do hotel
    def __init__(self, nome:str, telefone:str, email:str, id_unico:int):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = id_unico

    def adiciona_cliente(self):
        nome = input("Digite o nome do cliente")
        telefone = input("Digite o telefone do cliente")
        email = input("Digite o email do cliente")
        
        novo_cliente = Cliente(nome=nome, telefone=telefone, email=email, id_unico=self.id_unico)
        
        self.id_unico += 1
        
        self.lista_de_clientes.append[novo_cliente]

        return f"Cliente adicionado com sucesso"
  

class Quarto: #objeto quarto do hotel
  def __init__(self, numero:str, tipo:str, preco:float, disponibilidade:bool):
    self.numero = numero
    self.tipo = tipo
    self.preco = preco
    self.disponibilidade = disponibilidade

class Reserva: #objeto reserva do hotel
    def __init__(self, cliente:Cliente, quarto:Quarto, data_inicio:str, data_fim:str):
        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = "Reservado"
   
    

  
def verCliente(self):
    pass
def editarCliente(self):
    pass
def excluirCliente(self):
    pass







#loja1 = Concessionaria(nome="Paraiso dos Carros")

while True:
  menu = input("""
      Escolha uma opção:
      1 - Gestão de Clientes
      2 - Gestão de Quartos
      3 - Gestão de Reservas
      0 - Sair
    """)
  match menu:
    case "1":
      submenu_cliente = input("""
        Escolha uma opção:
        1 - Adicionar Cliente
        2 - Ver todos os Clientes
        3 - Editar Cliente
        4 - Excluir Cliente
        0 - Voltar
          """)
      match submenu_cliente:
        
        case "1":
          novo_cliente = Cliente.adiciona_cliente()
          print(novo_cliente)
                
        case "2":
          loja1.verCliente()
        case "3":
          print(loja1.editarCliente())
        case "4":
          print(loja1.excluirCliente())
        case "0":
          break
        case _:
          print("Opção inválida")
    case "2":
      submenu_carro = input("""
        Escolha uma opção:
        1 - Adicionar Carro
        2 - Ver todos os Carros
        3 - Editar Carro
        4 - Excluir Carro
        0 - Voltar
          """)
      match submenu_carro:
        case "1":
          print(loja1.adicionaCarro())
        case "2":
          loja1.verCarro()
        case "3":
          print(loja1.editarCarro())
        case "4":
          print(loja1.excluirCarro())
        case "0":
          break
        case _:
          print("Opção inválida")
    case "3":
      submenu_aluguel = input("""
        Escolha uma opção:
        1 - Adicionar Aluguel
        2 - Ver todos os Alugueis
        3 - Editar Aluguel
        4 - Excluir Aluguel
        0 - Voltar
          """)
      match submenu_aluguel:
        case "1":
          print(loja1.adicionaAluguel())
        case "2":
          loja1.verAluguel()
        case "3":
          print(loja1.editarAluguel())
        case "4":
          print(loja1.excluirAluguel())
        case "0":
          break
        case _:
          print("Opção inválida")
    case "0":
      break
    case _:
      print("Opção inválida")

