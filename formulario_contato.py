import flet as ft


def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    nome = ft.TextField(label="Nome", width=300, border_radius=20, bgcolor=ft.colors.WHITE54, 
                        text_style=ft.TextStyle(color=ft.colors.BLACK))
    
    email = ft.TextField(label="Email", width=300, border_radius=20, bgcolor=ft.colors.WHITE54, 
                         text_style=ft.TextStyle(color=ft.colors.BLACK))
    
                            # codigo de acesso é qualquer coisa aleatoria (so para implementar mesmo)
    codigo_acesso = ft.TextField(label="Codigo de acesso", width=300, border_radius=20, bgcolor=ft.colors.WHITE54, 
                                 text_style=ft.TextStyle(color=ft.colors.BLACK), password= True)
    
    mensagem = ft.TextField(label="Mensagem", multiline=True, min_lines=3, max_lines=5, width=300, border_radius=20, 
                            bgcolor=ft.colors.WHITE54, text_style=ft.TextStyle(color=ft.colors.BLACK))

    sucesso_msg = ft.Text("", color="green")
    nome_exibido = ft.Text("")
    email_exibido = ft.Text("")
    codigo_acesso_axibido =ft.Text("")
    mensagem_exibida = ft.Text("")

    def enviar_form(e):
        if nome.value and email.value and codigo_acesso.value and  mensagem.value:
            sucesso_msg.value = "Formulário enviado com sucesso 💹"
            sucesso_msg.color = "green"
            nome_exibido.value = f"📌 Nome: {nome.value.capitalize()}"
            codigo_acesso_axibido.value = f"👁‍🗨 Codigo de acesso: {codigo_acesso.value}"
            email_exibido.value = f"📧 Email: {email.value}"
            mensagem_exibida.value = f"📭 Mensagem: {mensagem.value.capitalize()}"
        else:
            sucesso_msg.value = "Por favor, preencha todos os campos."
            sucesso_msg.color = "red"

        page.update()

    botao_enviar = ft.ElevatedButton(content=ft.Text("📬-Enviar-📪",size=40,height=70, width= 260) , on_click=enviar_form)

    page.add(
        ft.Column(
            controls=[
                nome, 
                email,
                codigo_acesso, 
                mensagem, 
                botao_enviar, 
                sucesso_msg,
                ft.Divider(),
                nome_exibido,
                email_exibido,
                codigo_acesso_axibido,
                mensagem_exibida
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
