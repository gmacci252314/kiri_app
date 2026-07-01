import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/api/traducoes/"


def main(page: ft.Page):
    page.title = "Tradutor Kiri"
    page.padding = 20

    # -------- MENU --------
    def tela_menu():
        return ft.Column(
            [
                ft.Text("Tradutor Kiri", size=30, weight=ft.FontWeight.BOLD),

                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.PEOPLE,
                            icon_size=50,
                            tooltip="Povo Kiriri",
                            on_click=lambda e: page.go("/kiriri"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.INFO,
                            icon_size=50,
                            tooltip="Sobre o Projeto",
                            on_click=lambda e: page.go("/projeto"),
                        ),
                        ft.IconButton(
                            icon=ft.icons.TRANSLATE,
                            icon_size=50,
                            tooltip="Tradutor",
                            on_click=lambda e: page.go("/tradutor"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40,
                ),
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

        resultado = ft.Text(size=20, weight=ft.FontWeight.BOLD)

        def inverter_idiomas(e):
            origem = dropdown_origem.value
            destino = dropdown_destino.value

            dropdown_origem.value = destino
            dropdown_destino.value = origem

            page.update()

        def traduzir(e):
            palavra = txt_input.value.strip().lower()

            origem = dropdown_origem.value
            destino = dropdown_destino.value

            resultado.value = ""
            encontrou = False

            try:
                resposta = requests.get(API_URL)

                if resposta.status_code == 200:
                    traducoes = resposta.json()

                    for item in traducoes:

                        # Português -> Kiriri
                        if (
                            origem == "português"
                            and destino == "kiriri"
                            and item["idioma_portugues"].lower() == palavra
                        ):
                            resultado.value = f"Tradução: {item['idioma_kiriri']}"
                            encontrou = True
                            break

                        # Kiriri -> Português
                        elif (
                            origem == "kiriri"
                            and destino == "português"
                            and item["idioma_kiriri"].lower() == palavra
                        ):
                            resultado.value = f"Tradução: {item['idioma_portugues']}"
                            encontrou = True
                            break

                    if not encontrou:
                        resultado.value = f"A palavra '{palavra}' não foi encontrada."

                else:
                    resultado.value = "Erro ao acessar a API."

            except Exception as erro:
                resultado.value = f"Erro: {erro}"

            page.update()

        return ft.Column(
            [
                ft.Text("Tradutor Kiriri", size=25, weight=ft.FontWeight.BOLD),

                txt_input,

                ft.Row(
                    [
                        dropdown_origem,
                        ft.IconButton(icon=ft.icons.SWAP_HORIZ, on_click=inverter_idiomas),
                        dropdown_destino,
                        ft.ElevatedButton("Traduzir", on_click=traduzir),
                    ],
                    spacing=10,
                ),

                resultado,

                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ]
        )

    # -------- KIRIRI --------
    def tela_kiriri():
        return ft.Column(
            [
                ft.Text("História do povo Kiriri", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("... (seu texto completo aqui) ...", size=18),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
            scroll=ft.ScrollMode.AUTO,
        )

    # -------- PROJETO --------
    def tela_projeto():
        return ft.Column(
            [
                ft.Text("Página sobre o Projeto", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("... (texto do projeto) ...", size=18),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
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