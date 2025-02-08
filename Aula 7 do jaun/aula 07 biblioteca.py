#1 - RECEBER UM NÚMERO E RETORNAR SE ESSE NÚMERO É PAR OU IMPAR

def paridade(num):
    if num % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"

#2 - RECEBER UM NÚMERO E RETORNAR SE ESSE NÚMERO POSITIVO, NEGATIVO OU NEUTRO

def polaridade(num):
    if num  > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "neutro"
    
#3 - RECEBER UMA IDADE E RETORNAR SE ESSA IDADE É MAIOR OU MENOR DE IDADE.    


def maioridade(num):
    if num  >= 18:
        return "maior"
    else:
        return "menor"

#4 - RECEBER UMA IDADE E RETORNAR SE ESSA IDADE É CRIANÇA, ADOLESCENTE, ADULTO OU IDOSO.

def legalidade(num):
    if num  <= 12:

        return "maior"
    elif
    else:
        return "menor"




#5 - RECEBER UMA LISTA DE NÚMEROS E RETORNAR QUAL É A MÉDIA DESSES NÚMEROS.(SEM USAR O SUM)

def calc_media(sequencia):
    
        somatoria = 0
        for fator in sequencia:
            somatoria += fator
        media=somatoria/len(sequencia)
        return media
        
#6 - RECEBER UMA LISTA DE NÚMEROS E RETORNAR QUAL É O MAIOR NÚMERO DA LISTA (SEM USAR O MAX)

def encontrarmaior(listadenumeros):
    maior = listadenumeros[0]
    for i in listadenumeros:
        if i > maior:
            maior = i
    return  maior

#7 - RECEBER UMA LISTA DE NÚMEROS E RETORNAR QUAL É O MENOR NÚMERO DA LISTA (SEM USAR O MIN)


#CORPO DO PROGRAMA
parametros = [2,4,6,8,10]
print(f"os parametros retornam média:  {calc_media(parametros)}")

   
