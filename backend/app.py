import flet as ft


async def main(page: ft.Page):
    page.title = "Tradutor Kiri"

    # -------- MENU --------
    def tela_menu():
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.PEOPLE,
                            icon_size=40,
                            on_click=lambda e: page.go("/kiriri"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.INFO,
                            icon_size=40,
                            on_click=lambda e: page.go("/projeto"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.TRANSLATE,
                            icon_size=40,
                            on_click=lambda e: page.go("/tradutor"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # -------- TRADUTOR --------
    def tela_tradutor():
        txt_input = ft.TextField(label="Texto a traduzir", width=400)

        dropdown_origem = ft.Dropdown(
            label="Idioma de origem",
            width=200,
            options=[
                ft.dropdown.Option("português"),
                ft.dropdown.Option("kiriri"),
            ],
            value="português",
        )

        dropdown_destino = ft.Dropdown(
            label="Idioma de destino",
            width=200,
            options=[
                ft.dropdown.Option("português"),
                ft.dropdown.Option("kiriri"),
            ],
            value="kiriri",
        )

        traduzir_fake = ft.Text("Traduzir", size=16, weight=ft.FontWeight.BOLD)
        resultado = ft.Text(size=16)

        return ft.Column(
            [
                ft.Text("Tela Tradutor", size=25),
                txt_input,
                ft.Row([dropdown_origem, dropdown_destino, traduzir_fake], spacing=10),
                resultado,
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ]
        )

    # -------- KIRIRI --------
    def tela_kiriri():
        return ft.Column(
            [
                ft.Text("Página Kiriri"),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # -------- PROJETO --------
    def tela_projeto():
        return ft.Column(
            [
                ft.Text("Página Projeto"),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # -------- ROTAS --------
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(ft.View("/", [tela_menu()]))

        elif page.route == "/tradutor":
            page.views.append(ft.View("/tradutor", [tela_tradutor()]))

        elif page.route == "/kiriri":
            page.views.append(ft.View("/kiriri", [tela_kiriri()]))

        elif page.route == "/projeto":
            page.views.append(ft.View("/projeto", [tela_projeto()]))

        page.update()

    page.on_route_change = route_change

    page.go("/")


ft.app(target=main)