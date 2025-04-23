"""
Sistema de Gerenciamento de Reservas - Hotel Refúgio dos Sonhos
Descrição: Sistema básico para gerenciar quartos, clientes e reservas usando POO
"""



#====================
#INICIO DO PROJETO
#====================


def formatacep(self): #formata o CEP para imprimir
    
        lista_cep = list(self)
        lista_cep.insert(2,'.')
        lista_cep.insert(6,'-')
        return  ''.join(lista_cep) #.join: É um método de strings que pega uma sequência (como uma lista ou tupla) de strings e as une em uma única string.

def formataCPF(self): #formata o CPF para imprimir
    
        lista_cpf = list(self)
        lista_cpf.insert(3,'.')
        lista_cpf.insert(7,'.')
        lista_cpf.insert(11,'-')
        return  ''.join(lista_cpf)
    
def formata_fone(self): #formata o numero de telefone para imprimir
    
        lista_fone = list(self)
        lista_fone.insert(0,'(')
        lista_fone.insert(3,')')
        lista_fone.insert(5,' ')
        lista_fone.insert(10,'-')
        return  ''.join(lista_fone) #.join: É um método de strings que pega uma sequência (como uma lista ou tupla) de strings e as une em uma única string.
    
class Endereco:
    """
    Classe que representa um endereço completo
          
    """
    def __init__(self, rua: str, numero: str, complemento: str, cep: str, 
                 bairro: str, cidade: str, pais: str):
       
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.pais = pais
   
   

    def __str__(self) -> str:
        """
        Retorna o endereço formatado como string
        """
        endereco_completo = f"Logradouro: {self.rua}, {self.numero}"
        if self.complemento:  #só sera incluido complemento se existir
            endereco_completo += f" - {self.complemento}"
        endereco_completo += f"\nBairro: {self.bairro} - Cidade: {self.cidade} / {self.pais}"
        endereco_completo += f"\nCEP: {formatacep(self.cep)}"
        return endereco_completo

    def to_dict(self) -> dict:
        """
        Retorna o endereço como dicionário
        """
        return {
            'rua': self.rua,
            'numero': self.numero,
            'complemento': self.complemento,
            'cep': self.cep,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'pais': self.pais
        }

    
    
def Registra_endereco() -> Endereco:
    """
    Função que coleta os dados de endereço via input do usuário
    Retorna:
        Endereco: Objeto da classe Endereco com os dados fornecidos
    """
    print("\nCadastro de Endereço:")
    rua = input("Rua/Avenida: ")
    numero = input("Número: ")
    complemento = input("Complemento (opcional): ")
    cep = input("CEP (00.000-000): ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    pais = input("País [Enter para Brasil]: ") or "Brasil"  # Valor padrão
    

    # Cria e retorna o objeto Endereco
    return Endereco(
        rua=rua,
        numero=numero,
        complemento=complemento,
        cep=cep,
        bairro=bairro,
        cidade=cidade,
        pais=pais
    )
    


 
    
class Cliente:
    """
        Classe que representa um hóspede do hotel
        Nota do Aluno: acrescentei uma biblioteca Enderco para guardar o enderço do cliente, foi necessario gerar
        a o objeto de cadastramento de endereço.
    """
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: Endereco):
        """
        Método construtor da classe Cliente
        Parâmetros:
            nome (str): Nome completo do cliente
            cpf (str): CPF do cliente (apenas números)
            telefone (str): Telefone para contato
        """
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco  # Precisa chamar o metodo de entrada de endereço
    
    def __str__(self):
        """
        Método especial que define como o objeto será exibido quando convertido para string
        """
        cpf_formatado = formataCPF(self.cpf)
        fone_formatado = formata_fone(self.telefone)
        return f"Cliente: {self.nome}\nCPF: {cpf_formatado} \nTel: {fone_formatado} \nEnd: {self.endereco}"


class Quarto:
    """
    Classe que representa um quarto do hotel
    """
    def __init__(self, numero, tipo, preco_diaria, capacidade):
        """
        Método construtor da classe Quarto
        Parâmetros:
            numero (int): Número do quarto
            tipo (str): Tipo do quarto (ex: Standard, Luxo, Premium)
            preco_diaria (float): Preço por diária do quarto
            capacidade (int): Quantidade máxima de hóspedes
        """
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.capacidade = capacidade
        self.disponivel = True  # Inicialmente todos os quartos estão disponíveis
    
    def __str__(self):
        """
        Método especial para exibir informações do quarto
        """
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} (R${self.preco_diaria:.2f}/noite, {self.capacidade} pessoas) - {status}"


class Reserva:
    """
    Classe que representa uma reserva no hotel
    """
    def __init__(self, cliente, quarto, data_checkin, data_checkout):
        """
        Método construtor da classe Reserva
        Parâmetros:
            cliente (Cliente): Objeto da classe Cliente
            quarto (Quarto): Objeto da classe Quarto
            data_checkin (str): Data de entrada no formato DD/MM/AAAA
            data_checkout (str): Data de saída no formato DD/MM/AAAA
        """
        self.cliente = cliente
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = checkout
        quarto.disponivel = False  # Ao criar reserva, quarto fica indisponível
    
    def calcular_valor_total(self, diarias):
        """
        Calcula o valor total da reserva
        Parâmetros:
            diarias (int): Quantidade de diárias
        Retorna:
            float: Valor total da reserva
        """
        return diarias * self.quarto.preco_diaria
    
    def __str__(self):
        """
        Método especial para exibir informações da reserva
        """
        return f"Reserva para {self.cliente.nome} no {self.quarto} | Check-in: {self.data_checkin} | Check-out: {self.data_checkout}"


class Hotel:
    """
    Classe principal que representa o hotel e gerencia todas as operações
    """
    def __init__(self, nome):
        """
        Método construtor da classe Hotel
        Parâmetros:
            nome (str): Nome do hotel
        """
        self.nome = nome
        self.quartos = []
        self.clientes = []
        self.reservas = []
    
    def adicionar_quarto(self, quarto):
        """
        Adiciona um quarto à lista de quartos do hotel
        Parâmetros:
            quarto (Quarto): Objeto da classe Quarto
        """
        self.quartos.append(quarto)
    
    def cadastrar_cliente(self, nome, cpf, telefone, endereco):
        """
        Cria e adiciona um novo cliente à lista de clientes
        Parâmetros:
            nome (str): Nome do cliente
            cpf (str): CPF do cliente
            telefone (str): Telefone do cliente
            entrar o endereço envolve chamar o metodo endereco
        Retorna:
            Cliente: O objeto cliente criado
        """
        cliente_novo = Cliente(nome, cpf, telefone, endereco)
        
        self.clientes.append(cliente_novo)
        return cliente_novo
    
    def listar_clientela(self):
        print(20*"=")
        print("TODOS OS CLIENTES")
        print(20*"=")
        for item in self.clientes:
            print(item)
            print(20*"-")
        print(20*"=")
        print("FIM DA LISTA")
        print(20*"=")
    
    def buscar_quartos_disponiveis(self):
        """
        Retorna uma lista com todos os quartos disponíveis
        Retorna:
            list: Lista de objetos Quarto disponíveis
        """
        return [quarto for quarto in self.quartos if quarto.disponivel]
    
    def fazer_reserva(self, cliente, numero_quarto, data_checkin, data_checkout):
        """
        Realiza uma reserva no hotel
        Parâmetros:
            cliente (Cliente): Objeto Cliente
            numero_quarto (int): Número do quarto desejado
            data_checkin (str): Data de entrada
            data_checkout (str): Data de saída
        Retorna:
            Reserva: Objeto Reserva criado ou None se não for possível
        """
        # Procura o quarto pelo número
        quarto = next((q for q in self.quartos if q.numero == numero_quarto), None)
        
        if quarto and quarto.disponivel:
            reserva = Reserva(cliente, quarto, data_checkin, data_checkout)
            self.reservas.append(reserva)
            return reserva
        return None
    
    def listar_reservas(self):
        """
        Exibe todas as reservas ativas do hotel 
        """
                
        print(20*"=")
        print("LISTA DE RESERVAS")
        print(20*"=")
        
        for reserva in self.reservas:
            print(reserva)
            print(20*"-")

        
        print(20*"=")
        print("LISTA ENCERRADA")
        print(20*"=")


        
       
        
# Função para exibir menu interativo
def menu_interativo():
    """
    Exibe um menu interativo no console para o usuário
    """
    print("\nBem-vindo ao Sistema do Hotel Refúgio dos Sonhos!")
    print("1. Cadastrar cliente")
    print("2. Listar quartos disponíveis")
    print("3. Fazer reserva")
    print("4. Listar todas as reservas")
    print("5. Listar todos os clientes" )
    print("0. Sair")
    return input("Escolha uma opção: ")


# Exemplo de uso do sistema
if __name__ == "__main__":
    # Cria o hotel
    hotel = Hotel("Refúgio dos Sonhos")
    
    # Adiciona alguns quartos (normalmente isso viria de um banco de dados)
    hotel.adicionar_quarto(Quarto(101, "Standard", 150.00, 2))
    hotel.adicionar_quarto(Quarto(102, "Standard", 150.00, 2))
    hotel.adicionar_quarto(Quarto(201, "Luxo", 250.00, 3))
    hotel.adicionar_quarto(Quarto(202, "Luxo", 250.00, 3))
    hotel.adicionar_quarto(Quarto(301, "Premium", 400.00, 4))
    
    # Loop principal do programa
    while True:
        opcao = menu_interativo()
        
        if opcao == "1":  # Cadastrar cliente
            print("\nCadastro de Cliente")
            nome = input("Nome completo: ")
            cpf = input("CPF (apenas números): ")
            telefone = input("Telefone: ")
            endereco = Registra_endereco()
            cliente = hotel.cadastrar_cliente(nome, cpf, telefone,endereco)
            print(f"Cliente {cliente.nome} cadastrado com sucesso!")
            
         
        
        elif opcao == "2":  # Listar quartos disponíveis
            print("\nQuartos Disponíveis:")
            disponiveis = hotel.buscar_quartos_disponiveis()
            for quarto in disponiveis:
                print(quarto)
        
        elif opcao == "3":  # Fazer reserva
            print("\nNova Reserva")
            cpf = input("CPF do cliente: ")
            # Busca cliente pelo CPF (simplificado para exemplo)
            cliente = next((c for c in hotel.clientes if c.cpf == cpf), None)
            
            if cliente:
                print("Quartos disponíveis:")
                disponiveis = hotel.buscar_quartos_disponiveis()
                for quarto in disponiveis:
                    print(quarto)
                
                numero_quarto = int(input("Número do quarto desejado: "))
                checkin = input("Data de check-in (DD/MM/AAAA): ")
                checkout = input("Data de check-out (DD/MM/AAAA): ")
                
                reserva = hotel.fazer_reserva(cliente, numero_quarto, checkin, checkout)
                if reserva:
                    print(f"Reserva confirmada! {reserva}")
                else:
                    print("Não foi possível fazer a reserva. Quarto indisponível ou não encontrado.")
            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")
        
        elif opcao == "4":  # Listar reservas
            hotel.listar_reservas()
            
        elif opcao == "5":  # Listar todos os clientes
            hotel.listar_clientela()
        
        elif opcao == "0":  # Sair
            print("Obrigado por usar o sistema do Hotel Refúgio dos Sonhos!")
            break
        
                
        else:
            print("Opção inválida. Tente novamente.")
            
            
#====================
#FIM DO PROJETO
#====================    
# 
