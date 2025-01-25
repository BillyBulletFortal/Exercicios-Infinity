#media de numeros sem usar funçao sum e sem usar o imputa para receber os numeros

numeros = [2,4,6,8]

def calculamedia(valor):
    soma = 0
    for i in valor:
    
        soma += i

    media = soma/len(valor)

    return(f"a media é {media}")

print(calculamedia(numeros))


lista = [5,9,8,4,1,10]
print(calcularMedia(lista_de_numeros=lista))

print(calcularMedia(lista_de_numeros=[10,50,60,70,80]))

print(calcularMedia([2,4,5]))

lista_tal = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista_tal.append(numero)
    
print(calcularMedia(lista_de_numeros=lista_tal))