#flet é usado para aplicativos desktop
#o tkinter ja esta instalado mas é muito ruin e mais dificil de usar
#widgets são os botoes campos etc para janelas de aplicativos
#programa com flet que pede para o susuario digitar 4 notas
#aprovado com media 7


import flet as ft

def main(pagina:ft.Page):
    def EnviarDados(e):
        media = (float(n1.value)+float(n2.value)+float(n3.value)+float(n4.value))/4
        if media >= 7:
            resposta.value = (f"Sua média foi {media}  e está APROVADO")
        else:
            resposta.value = (f"Sua média foi {media}  e está REPROVADO")
        resposta.update()


    pagina.title = "Calcula Média"

    mensagem=ft.Text(value="Digite as notas do aluno")
    n1 = ft.TextField(label="NOTA 1")
    n2 = ft.TextField(label="NOTA 2")
    n3 = ft.TextField(label="NOTA 3")
    n4 = ft.TextField(label="NOTA 1")
    
    resposta = ft.Text(value="")


    botao_enviar = ft.ElevatedButton(text="MÉDIA", on_click=EnviarDados)
    pagina.add(n1,n2,n3,n4, botao_enviar,resposta)

ft.app(target=main)