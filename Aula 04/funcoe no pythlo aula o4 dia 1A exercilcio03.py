# FAÇA UM PROJETO DE UMA BIBLIOTECA
# O SISTEMA DEVE PERMITIR QUE:
# ADICIONE UM NOVO LIVRO
# VEJA TODOS OS LIVROS ADICIONADOS
# EXCLUA UM LIVRO ADICIONADO

# CADA LIVRO TEM QUE TER:
# ID, TITULO, GENERO, QTDE_PAGINAS, PRECO.

# USEM FUNÇÕES, LISTA, DICIONÁRIO, FOR, WHILE, IF.

Biblioteca = []

while True:
    menu = input("""
        Escolha uma opção:
        1 - Adicionar Novo Livro
        2 - Ver Todos os Livros
        3 - Excluir Livro
        4 - Sair
    """)
    match menu:
        case "1": #ADICIONAR UM NOVO LIVRO - O case vai ser chamar a função que recebera o codigo abaixo


            id =  input("Identificador único: ===>    ")
            titulo =  input("Título: ===>    ")
            genero =  input("Gênero: ===>    ")
            qtd =  input("Estoque: ===>    ")
            paginas =  input("Numero de páginas: ===>    ")
            preco =  input("Preço: ===>    ")

            livro = {
                "Identificador": id,
                "Titulo": titulo,
                "Gênero": genero,
                "Estoque": qtd,
                "Páginas":  paginas,
                "Preço": preco   
            }

            Biblioteca.append(livro)
            Print("Novo livro adicionado com sucesso") #vau ser return dentro de uma funçao
    
        case "2" #Listar todos os livros



#.................>>>>>>>>>SOLUÇÃO DO PROFESSOR<<<<<<<<<<<<<<<<<<<<<..........................

lista_de_livros = []
id = 1



def adicionarLivro():
    global id
    
    titulo = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
    paginas = int(input("Digite a quantidade de páginas do livro: "))
    preco = float(input("Digite preço do livro: "))

    novo_livro = {
        "Id": id,
        "Título": titulo,
        "Gênero": genero,
        "Quantidade Paginas": paginas,
        "Preço": preco
    }
    
    id += 1
    lista_de_livros.append(novo_livro)
    return f"Livro {titulo} foi adicionado com sucesso"


def mostrarTodos():
    for livro_da_vez in lista_de_livros:
        print(f"""
            Id: {livro_da_vez['Id']}
            Título: {livro_da_vez['Título']}
            Gênero: {livro_da_vez['Gênero']}
            Quantidade de Páginas: {livro_da_vez['Quantidade Páginas']}
            Preço: {livro_da_vez['Preço']}
            """)



def excluirLivro():
        id_do_livro_excluido = int(input("Digite o ID do livro que você quer excluir: "))
            
        for livro_da_vez in lista_de_livros:
            if livro_da_vez["Id"] == id_do_livro_excluido:
                lista_de_livros.remove(livro_da_vez)
                return f"Livro {livro_da_vez['Título']} excluído com sucesso"



while True:
    menu = input("""
        Escolha uma opção:
        1 - Adicionar livro
        2 - Ver todos livros
        3 - Excluir livro
        0 - Sair
    """)
    
    match menu:
        case "1":
            print(adicionarLivro())
        case "2":
            mostrarTodos()
        case "3":
            print(excluirLivro())
        case "0":
            break
        case _:
            print("Opção inválida")



    

# cola abaixolista_de_carros = []

# while True:
#     menu = input("""
#         Escolha uma opção:
#         1 - Adicionar Novo Carro
#         2 - Ver Todos os Carros
#         3 - Excluir Carro
#         4 - Sair
#     """)
#     match menu:
#         case "1":
#             marca = input("Digite a marca do carro: ")
#             modelo = input("Digite o modelo do carro: ")
#             ano = int(input("Digite o ano do carro: "))
#             cor = input("Digite a cor do carro: ")
#             preco = float(input("Digite o preço do carro: "))
#             placa = input("Digite o preço do carro: ")
            
#             novo_carro = {
#                 "Marca": marca,
#                 "Modelo": modelo,
#                 "Ano": ano,
#                 "Cor": cor,
#                 "Preço": preco,
#                 "Placa": placa
#             }
            
#             lista_de_carros.append(novo_carro)
#             print("Carro adicionado com sucesso.")
#         case "2":
#             for carro_da_vez in lista_de_carros:
#                 print(f"""
#                 ==============================
#                 Marca: {carro_da_vez['Marca']} | Modelo: {carro_da_vez['Modelo']}
#                 Ano: {carro_da_vez['Ano']} | Cor: {carro_da_vez['Cor']}
#                 Preço: R$ {carro_da_vez['Preço']}
#             """)
                
#         case "3":
#             placa_do_carro_que_eu_quero_deletar = input("Digite a placa do carro que você quer deletar: ")
            
#             carro_encontrado = False
            
#             for carro_da_vez in lista_de_carros:
#                 if carro_da_vez['Placa'] == placa_do_carro_que_eu_quero_deletar:
#                     carro_encontrado = True
#                     lista_de_carros.remove(carro_da_vez)
#                     print("Carro deletado com sucesso.")

#             if carro_encontrado == False:
#                 print("Carro não foi encontrado")
                
#         case "4":
#             print("Fim do programa")
#             break
#         case _:
#             print("Opção inválida.")


# para estudar:
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR:
# nome, idade, altura, profissão
# ARMAZENE TODAS AS INFORMAÇÕES EM UM DICIONÁRIO.


# SOLUÇÃO 1

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))
# profissao = input("Digite sua profissão: ")

# dados_pessoais = {
#     "Nome": nome,
#     "Idade": idade,
#     "Altura": altura,
#     "Profissão": profissao
# }

# print(dados_pessoais)





# SOLUÇÃO 2

# dados_pessoais = {
#     "Nome": input("Digite seu nome: "),
#     "Idade": int(input("Digite sua idade: ")),
#     "Altura": float(input("Digite sua altura: ")),
#     "Profissão": input("Digite sua profissão: ")
# }


# print(dados_pessoais)





# SOLUÇÃO 3

# dados_pessoais = {}
# dados_pessoais['Nome'] = input("Digite seu nome: ")
# dados_pessoais['Idade'] = int(input("Digite sua idade: "))
# dados_pessoais['Altura'] = float(input("Digite sua altura: "))
# dados_pessoais['Profissão'] = input("Digite sua profissão: ")
# print(dados_pessoais)





# SOLUÇÃO 4 
# dados_pessoais = {}

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))
# profissao = input("Digite sua profissão: ")

# dados_pessoais['Nome'] = nome
# dados_pessoais['Idade'] = idade
# dados_pessoais['Altura'] = altura
# dados_pessoais['Profissão'] = profissao
# print(dados_pessoais)






# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 CORES E GUARDE ELA EM UMA LISTA.

# lista_de_cores = []

# for i in range(5):
#     cor = input("Digite uma cor: ")
#     lista_de_cores.append(cor)

# print(lista_de_cores)




# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DITITAR UM NÚMERO ILIMITADO DE CORES E GUARDE ELA EM UMA LISTA.
# DICA: FAÇAM UM MENU (USANDO WHILE TRUE)



# SOLUÇÃO 1 USANDO IF

# lista_de_cores = []

# while True:
#     menu = input("""
#         Escolha uma opção:
#         1 - Adicionar Cor
#         2 - Sair
#     """)
#     if menu == "1":
#         cor = input("Digite uma cor: ")
#         lista_de_cores.append(cor)
#     elif menu == "2":
#         break
#     else:
#         print("Opção inválida")

# print(lista_de_cores)





# SOLUÇÃO 2 USANDO MATCH

# lista_de_cores = []

# while True:
#     menu = input("""
#         Escolha uma opção:
#         1 - Adicionar Cor
#         2 - Sair
#     """)
#     match menu:
#         case "1":
#             cor = input("Digite uma cor: ")
#             lista_de_cores.append(cor)
#         case "2":
#             break
#         case _:
#             print("Opção inválida")

# print(lista_de_cores)