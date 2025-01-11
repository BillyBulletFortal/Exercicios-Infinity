#use os codigos dos carros e adicione mais uma opcao no menu


lista_de_carros = []

while True:
    menu = input("""
        Escolha uma opção:
        1 - Adicionar Novo Carro
        2 - Ver Todos os Carros
        3 - Deletar Carro
        4 - Sair
    """)
    match menu:
        case "1":
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano do carro: "))
            cor = input("Digite a cor do carro: ")
            preco = float(input("Digite o preço do carro: "))
            
            novo_carro = {
                "Marca": marca,
                "Modelo": modelo,
                "Ano": ano,
                "Cor": cor,
                "Preço": preco
            }
            
            lista_de_carros.append(novo_carro)
            print("Carro adicionado com sucesso.")
        
        case "2":
            for carro_da_vez in lista_de_carros:
                print(f"""
                ==============================
                Marca: {carro_da_vez['Marca']} | Modelo: {carro_da_vez['Modelo']}
                Ano: {carro_da_vez['Ano']} | Cor: {carro_da_vez['Cor']}
                Preço: R$ {carro_da_vez['Preço']}
            """)
        
        case "3":
            modelo_para_deletar = input("Digite o modelo do carro que deseja deletar: ")
            for carro_da_vez in lista_de_carros:
                if (carro_da_vez['Modelo']).upper() == modelo_para_deletar.upper():
                    lista_de_carros.remove(carro_da_vez)
                    print("Carro deletado com sucesso.")
                    break
            else:
                print("Carro não encontrado.")
    
        case "4":
            print("Fim do programa")
            break
        case _:
            print("Opção inválida.")
