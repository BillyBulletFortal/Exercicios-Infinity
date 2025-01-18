#somente no python function se chama def

VERSÃO 1

def checarIdade():
    idade = int(input("Digite sua idade: "))
    
    if idade >= 18:
        print(f"Você tem {idade} anos e já pode ser preso")
    else:
        print(f"Você tem  {idade} anos e vai pra FEBEM")


for i in range(10):
    checarIdade()




VERSÃO 2

def checarIdade(idade):    
    if idade >= 18:
        print(f"Você tem {idade} anos e já pode ser preso")
    else:
        print(f"Você tem  {idade} anos e vai pra FEBEM")

for i in range(10):
    idade = int(input("Digite sua idade: "))
    checarIdade(idade)


VERSÃO FINAL (É A QUE VAMOS USAR)


def checarIdade():
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        return f"Você tem {idade} anos e já pode ser preso"
    else:
        return f"Você tem  {idade} anos e vai pra FEBEM"


for i in range(10):
    print(checarIdade())

