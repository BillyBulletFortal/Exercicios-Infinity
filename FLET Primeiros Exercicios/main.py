#flet é usado para aplicativos desktop
#o tkinter ja esta instalado mas é muito ruin e mais dificil de usar
#widgets são os botoes campos etc para janelas de aplicativos



import flet as ft

def main(pagina:ft.Page):
    pagina.title= "Primeira Página"
    mensagem=ft.Text(value="Meu primeiro código com flet")
    entrada_nome = ft.Text(label="NOME")
    entrada_idade = ft.Text(label="IDADE")
    botao_enviar = ft.ElevatedButton(text="ENVIAR")
    pagina.add(mensagem,entrada_nome,entrada_idade,botao_enviar)


ft.app(target=main)