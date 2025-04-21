"""
Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. 
O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. 
Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. 
Crie um método depositar que permita             adicionar um valor ao saldo,    um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), 
e um método exibir_saldo       que exiba o saldo atual da conta. 
Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.
"""

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor: float):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido. Verifique o valor e o saldo disponível.")


    def get_titular(self):
        return self._titular   

    def get_saldo(self):
        return self._saldo     
    





""" fazer um menu para o usuario escolher a opção desejada """

# Função para exibir menu interativo
def menu_interativo():
    
    print("Escolha uma opção:")
    print("1 - Abrir Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Saldo")
    print("0 - Sair")

    return input("Digite o número da opção desejada:  ")
  


# Loop principal do programa
while True:
    opcao = menu_interativo()
    
    if opcao == "1":  # Cadastrar cliente
        print("Digite os dados do titular da conta:/n")
        titular = input("Nome completo: ")
        saldo_inicial = float(input("Saldo inicial: "))
        conta = ContaBancaria(titular, saldo_inicial)
        print(f"Cliente {conta.get_titular()} cadastrado com sucesso!")
        
        
    
    elif opcao == "2":  # Fazer depósito
        print("\nDepositar:")
        entrada = float(input("Valor a depositar: "))    
        conta.depositar(entrada)
        print(f"O novo saldo de {conta.get_titular()} é R$ {conta.get_saldo():.2f}!")  
        

    elif opcao == "3":  # Fazer saque
        print("\nSacar:")
        entrada = float(input("Valor a sacar: "))
        conta.sacar(entrada)
        print(f"O novo saldo de {conta.get_titular()} é R$ {conta.get_saldo():.2f}!")
        
        
    
           
    elif opcao == "4":  # Exibe o nome do titular com seu saldo
        print(f"O saldo de {conta.get_titular()} é de R$ {conta.get_saldo():.2f}") 
        
        

    elif opcao == "0":  # Sair
        print("Obrigado por preferir nossos serviços!")
        break
    
    
    else:
        print("Opção inválida. Tente novamente.")


