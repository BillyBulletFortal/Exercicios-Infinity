#
#FAÇA UMA FUNÇÃO QUE RECEBE UM NOME E RETORNA QUANTAS VOGAIS E QUANTAS CONSOANTES TEM NO NOME.
#
#FAÇA UM LOOP DE REPETIÇÃO PARA USAR ESSA FUNÇÃO 3 VEZES.



def contarVogaisConsoantes():
    vogais = 'aáâãeéêẽiíîĩoóôõuúûũ'
    consoantes = 'bcdfghjklmnñpqrstvxywzç'
    cont_vogais = 0
    cont_consoantes = 0
    
    nome = input("Digite seu nome: ")
    
    for letra_da_vez in nome:
        if letra_da_vez.lower() in vogais:
            cont_vogais += 1
        elif letra_da_vez.lower() in consoantes:
            cont_consoantes += 1
    return f"Seu nome tem {cont_vogais} vogais e {cont_consoantes} consoantes"


for i in range(3):
    print(contarVogaisConsoantes())
