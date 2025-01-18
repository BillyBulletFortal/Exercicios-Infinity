#FFAÇA UMA FUNÇÃO QUE PERGUNTA QUAL A IDADE DA PESSOA E CHEQUE SE ELE É:
#CRIANÇA
#ADOLESCENTE
#ADULTO
#IDOSO

#AÇA UM LOOP DE REPETIÇÃO QUE USE ESSA FUNÇÃO 5 VEZES.




def checagem():
    idade = int(input("Digite a idade: ===>  "))

    if idade >= 70:
        return f"Você tem {idade} Classificado como IDOSO"
    elif idade >= 18:
        return f"Você tem {idade} Classificado como ADULTO"
    elif idade >= 15:
        return f"Você tem {idade} Classificado como ADOLESCENTE"
    else:
        return f"Você tem  {idade} Classificado como CRIANÇA"


for i in range(5):
    print(checagem())

