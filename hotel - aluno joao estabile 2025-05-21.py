from datetime import datetime
import flet as ft

# Funções de formatação (iguais às suas) 
def formatacep(cep):
    lista_cep = list(cep)
    lista_cep.insert(2, '.')
    lista_cep.insert(6, '-')
    return ''.join(lista_cep)

def formataCPF(cpf):
    lista_cpf = list(cpf)
    lista_cpf.insert(3, '.')
    lista_cpf.insert(7, '.')
    lista_cpf.insert(11, '-')
    return ''.join(lista_cpf)

def formata_fone(fone):
    lista_fone = list(fone)
    lista_fone.insert(0, '(')
    lista_fone.insert(3, ')')
    lista_fone.insert(5, ' ')
    lista_fone.insert(10, '-')
    return ''.join(lista_fone)

# Classes 
class Endereco:
    def __init__(self, rua, numero, complemento, cep, bairro, cidade, pais):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.pais = pais

    def __str__(self):
        endereco_completo = f"Logradouro: {self.rua}, {self.numero}"
        if self.complemento:
            endereco_completo += f" - {self.complemento}"
        endereco_completo += f"\nBairro: {self.bairro} - Cidade: {self.cidade} / {self.pais}"
        endereco_completo += f"\nCEP: {formatacep(self.cep)}"
        return endereco_completo

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = formata_fone(telefone)
        self.email = email

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True

class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Ativa"
        quarto.disponivel = False

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.disponivel = True

# Gerenciador de Reservas 
class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []
        self.clientes = []
        self.reservas = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def verificar_disponibilidade(self):
        return [q for q in self.quartos if q.disponivel]

    def criar_reserva(self, cliente, numero_quarto, checkin, checkout):
        quarto = next((q for q in self.quartos if q.numero == numero_quarto and q.disponivel), None)
        if quarto:
            reserva = Reserva(cliente, quarto, checkin, checkout)
            self.reservas.append(reserva)
            return reserva
        return None

    def cancelar_reserva_por_numero(self, numero_quarto):
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto and reserva.status == "Ativa":
                reserva.cancelar()
                return True
        return False

    def listar_reservas(self):
        return self.reservas

    def listar_clientes(self):
        return self.clientes


#-----------------------------------------------------------------------------------------------------------------

#=================
# INICIO DA INTERFACE FLET 
#=================


def main(page: ft.Page): 
    page.title = "Hotel Refúgio dos Sonhos - Reservas"
    page.bgcolor = "#ffff99"  # Definir a cor de fundo da página usando um valor de cor do Flet

    

    sistema = GerenciadorDeReservas()
    sistema.adicionar_quarto(Quarto(101, "Single", 200))
    sistema.adicionar_quarto(Quarto(102, "Double", 350))
    sistema.adicionar_quarto(Quarto(201, "Suite", 500))

    nome = ft.TextField(label="Nome", hover_color="#cceecc", color="#000000", bgcolor="#ffffff",) 
    telefone = ft.TextField(label="Telefone", hover_color="#cceecc", color="#000000", bgcolor="#ffffff", )
    email = ft.TextField(label="Email", hover_color="#cceecc", color="#000000", bgcolor="#ffffff", )
    numero_quarto = ft.TextField(label="Número do Quarto", hover_color="#cceecc", color="#000000", bgcolor="#ffffff", )
    checkin = ft.TextField(label="Check-in (AAAA-MM-DD)", hover_color="#cceecc", color="#000000", bgcolor="#ffffff", )
    checkout = ft.TextField(label="Check-out (AAAA-MM-DD)", hover_color="#cceecc", color="#000000", bgcolor="#ffffff", )
    numero_cancelamento = ft.TextField(label="Número do Quarto para Cancelar Reserva", hover_color="#eeaaee", color="#ff1111", bgcolor="#ffffff", )

    resultado = ft.Text()

    def reservar_click(e):
        try:
            data_checkin = datetime.strptime(checkin.value, "%Y-%m-%d").date()
            data_checkout = datetime.strptime(checkout.value, "%Y-%m-%d").date()
            numero = int(numero_quarto.value)

            if data_checkout <= data_checkin:
                resultado.value = "A data de check-out deve ser posterior à de check-in."
                page.update()
                return

            cliente = Cliente(nome.value, telefone.value, email.value) #precisa de filtro de validação do email
            sistema.adicionar_cliente(cliente)
            reserva = sistema.criar_reserva(cliente, numero, data_checkin, data_checkout)

            if reserva:
                resultado.value = f"Reserva realizada com sucesso para {cliente.nome} no quarto {numero}!"
            else:
                resultado.value = "Quarto indisponível ou número inválido."

        except ValueError:
            resultado.value = "Dados inválidos. Verifique o número do quarto e datas no formato AAAA-MM-DD."
        page.update()

    def listar_disponiveis(e):
        disponiveis = sistema.verificar_disponibilidade()
        if disponiveis:
            lista_quartos = "\n".join([f"Quarto {q.numero} - {q.tipo} - R${q.preco}" for q in disponiveis])
            resultado.value = "Quartos disponíveis:\n" + lista_quartos
        else:
            resultado.value = "Nenhum quarto disponível."
        page.update()

    def cancelar_click(e):
        try:
            numero = int(numero_cancelamento.value)
            sucesso = sistema.cancelar_reserva_por_numero(numero)
            if sucesso:
                resultado.value = f"Reserva do quarto {numero} cancelada com sucesso."
            else:
                resultado.value = "Reserva não encontrada ou já cancelada."
        except ValueError:
            resultado.value = "Número inválido."
        page.update()

    def listar_reservas_click(e):
        reservas = sistema.listar_reservas()
        if reservas:
            texto = "\n".join([
                f"{r.cliente.nome} - Quarto {r.quarto.numero} - {r.checkin} a {r.checkout} - Status: {r.status}"
                for r in reservas
            ])
            resultado.value = "Reservas:\n" + texto
        else:
            resultado.value = "Nenhuma reserva encontrada."
        page.update()

    def listar_clientes_click(e): #PRECISA FORMATAR O TELEFONE E CPF - incluir dados completos com cpf e endereço
        clientes = sistema.listar_clientes()
        if clientes:
            texto = "\n".join([
                f"{c.nome} - Telefone: {c.telefone} - Email: {c.email}"
                for c in clientes
            ])
            resultado.value = "Clientes:\n" + texto
        else:
            resultado.value = "Nenhum cliente cadastrado."
        page.update()

    page.add(
    
        ft.Text("Sistema de Reservas - Refúgio dos Sonhos", size=24, weight="bold"),
        nome, telefone, email,
        numero_quarto, checkin, checkout,
        ft.Row([
            ft.ElevatedButton(text="Reservar", color="#000000", bgcolor="#66cc33", on_click=reservar_click), #ft.ElevatedButton(text="Insira o nome de sua cidade!", on_click=inserir)
            ft.ElevatedButton("Verificar Disponibilidade", on_click=listar_disponiveis)
        ]),
        ft.Divider(),
        numero_cancelamento,
        ft.ElevatedButton("Cancelar Reserva",  color="#FFFFFF", bgcolor="#EE1111", on_click=cancelar_click),
        ft.Divider(),
        ft.Row([
            ft.ElevatedButton("Listar Reservas", color="#000000", bgcolor="#66cc33",  on_click=listar_reservas_click),
            ft.ElevatedButton("Listar Clientes", color="#000000", bgcolor="#66cc33",  on_click=listar_clientes_click)
        ]),
        ft.Divider(),
        resultado
        )

ft.app(target=main)
