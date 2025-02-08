def parOuImpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
    
def positivoNegativoNeutro(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Neutro"


def maiorIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    

def checarFaixaEtaria(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade <= 65:
        return "Adulto"
    else:
        return "Idoso"
    

def calcularMedia(lista_de_numeros):
    soma_total = 0
    for numero_da_vez in lista_de_numeros:
        soma_total += numero_da_vez
    media = soma_total / len(lista_de_numeros)
    return media


def encontrarMaior(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero_da_vez in lista_de_numeros:
        if numero_da_vez > maior_numero:
            maior_numero = numero_da_vez
    return maior_numero

def encontrarMenor(lista_de_numeros):
    menor_numero = lista_de_numeros[0]
    for numero_da_vez in lista_de_numeros:
        if numero_da_vez < menor_numero:
            menor_numero = numero_da_vez
    return menor_numero