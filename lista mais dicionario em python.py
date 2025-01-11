# o usuario deve ser capaz de cdastrar quantos carros precisar
# é uma lista de dicioinarios

lista_carros = []
matricula = int(0)
cadastro = {}
controle = 0 

while True:
    controle = input("Digite N para novo carro ou S para sair ==>  ")

    if controle.upper() == "S":
        print(f"foram cadastrados os carros:    {lista_carros}")
        break
    else:
        matricula += 1
        
        cadastro = {
        "Matricula": matricula,
        "Marca": input("Marca: "),
        "Modelo": input("Modelo: "),
        "Ano": input("Ano: "),
        "Cor": input("Cor: "),
        "Preço": input("Preço: ")
    
         }
        lista_carros.append(cadastro)
          