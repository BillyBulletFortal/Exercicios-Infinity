#flet é usado para aplicativos desktop
#o tkinter ja esta instalado mas é muito ruin e mais dificil de usar
#widgets são os botoes campos etc para janelas de aplicativos
#programa com flet que pede para o susuario digitar 4 notas
#aprovado com media 7


import flet as ft

def main(pagina:ft.Page):
    def enviarDados(e):
        print(f"Olá {entrada_nome.value} você tem {entrada_idade.value} anos")

        if int(entrada_idade.value) >= 18:
            resposta.value = (f"{entrada_nome.value} você é maior de idade")
        else:
            resposta.value = (f"{entrada_nome.value} você é menor de idade")
        
        resposta.update()
        

    pagina.title= "Primeira Página"
    mensagem=ft.Text(value="Meu primeiro código com flet")
    entrada_nome = ft.TextField(label="NOME")
    entrada_idade = ft.TextField(label="IDADE")
    botao_enviar = ft.ElevatedButton(text="ENVIAR", on_click=enviarDados)
    resposta = ft.Text(value="")


    pagina.add(mensagem,entrada_nome,entrada_idade,botao_enviar,resposta)




ft.app(target=main)