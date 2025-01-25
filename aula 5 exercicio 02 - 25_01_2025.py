#FAÇA UMA FUNÇÃO QUE PEDE (OU RECEBE) O 
# NOME E A IDADE DE UMA PESSOA E RETORNA A 
# CONDIÇÃO DE VOTO DAQUELA PESSOA. EX:ntra a idade e diz se vota

def titulo(idade):
    if idade >= 70:
        condição = "facultativo"
    elif idade >= 18:
        condição = "obrigatorio"
    elif idade >= 16:
        condição = "facultativo menor"
    else:
        condição = "proibido"
    return condição

valor = int(input("digite a idade:  >> "))

print(f"A sua condição eleitoral é:  >>  {titulo(valor)}")


