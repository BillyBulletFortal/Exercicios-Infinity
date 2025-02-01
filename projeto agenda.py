# Estrutura de Dados
# Cada tarefa será representada por um dicionário com as seguintes chaves:

# nome: Nome da tarefa.

# descricao: Descrição da tarefa.

# prioridade: Prioridade da tarefa (alta, média, baixa).

# categoria: Categoria da tarefa (trabalho, estudo, lazer, etc.).

# concluida: Status da tarefa (True ou False).

# Funções
# Vamos criar as seguintes funções:

# adicionar_tarefa: Adiciona uma nova tarefa à lista de Agenda.

# listar_tarefas: Lista todas as Agenda.

# marcar_concluida: Marca uma tarefa como concluída.

# exibir_por_prioridade: Exibe Agenda filtradas por prioridade.

# exibir_por_categoria: Exibe Agenda filtradas por categoria.

# menu: Exibe o menu de comandos e permite ao usuário interagir com o programa.




# Função para adicionar

# Lista para armazenar as Agenda
Agenda = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    nome = input("Nome da tarefa: ==>    ")
    descricao = input("Descrição da tarefa:==>    ")
    prioridade = input("Prioridade (A (alta)  , M (média),   B (baixa):==>    ").upper()
    categoria = input("Categoria:==>    ").lower()
    
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    print(f"CONFIRA OS DADOS: {tarefa['nome']} - {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']}  ")
    Agenda.append(tarefa)
    return "Tarefa adicionada com sucesso."

   # print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para listar todas as Agenda
def listar_Agenda():
    if not Agenda:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Agenda de Tarefas ---")
        for i, tarefa in enumerate(Agenda):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. {tarefa['nome']} - {tarefa['descricao']} "
                  f"(Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status})")

def marcar_concluida():
    listar_Agenda()  # Agora usa listar_Agenda em vez de listar_tarefas
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
        if 0 <= indice < len(Agenda):
            Agenda[indice]["concluida"] = True
            print(f"Tarefa '{Agenda[indice]['nome']}' marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        
def lista_prioridade():
  
            
    prioridade = input("Digite a prioridade (A = alta, M = média, B = baixa): ").upper()
    Agenda_filtradas = [tarefa for tarefa in Agenda if tarefa["prioridade"] == prioridade]
    
    if not Agenda_filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")
    else:
        print(f"\n--- Tarefas com Prioridade '{prioridade.capitalize()}' ---")
        for tarefa in Agenda_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} "
                  f"(Categoria: {tarefa['categoria']}, Status: {status})")
            
        
def lista_categoria():
    while True:
        menu = input("""
        Escolha uma categoria
        1 - Trabalho
        2 - Educação
        3 - Lazer
        """)
        match menu:
            case "1":
                categoria_buscada = "Trabalho" 
                break
            case "2":
                categoria_buscada = "Educação" 
                break
            case "3":
                categoria_buscada = "Lazer" 
                break
            case _:
                print("Opção inválida")
                
                

    Agenda_filtradas = [tarefa for tarefa in Agenda if tarefa["categoria"] == categoria_buscada]
    
    if not Agenda_filtradas:
        print("Não existe a categoria ou a digitação esta imprecisa")
    else:
        print(f"\n--- Tarefas da categoria '{categoria_buscada.capitalize()}' ---")
        for tarefa in Agenda_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status}")
        
    
#Corpo do Programa

while True:
    menu = input("""
    Escolha uma opção
    1 - Adicionar Tarefa
    2 - Listar tarefas
    3 - Marcar tarefa como concluida
    4 - Listar por prioridade
    5 - Listar por categoria
    0 - Sair
    """)
    match menu:
        case "1":
            print(adicionar_tarefa())
        case "2":
            print(listar_Agenda())
        case "3":
            print(marcar_concluida())
        case "4":
            print(lista_prioridade())
        case "5":
            print(lista_categoria())
        case "0":
            break
        case _:
            print("Opção inválida")
            



        