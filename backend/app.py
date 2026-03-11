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
                ft.Text("História do povo Kiriri", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("A história desse povo começa a ser contada a partir do primeiro contato com os portugueses. O povo estaria espalhado  pelo interior " \
                "entre as margens do São Francisco e as do Rio Acaracu, um extenso território, do Ceará à Paraíba e até uma porção setentrional do sertão baiano.", size=18),
                ft.Text("Foi nas terras dos Kiriri que os primeiros jesuítas se instalaram, " \
                "na segunda metade do século XVII.  " \
                "É possível observar que em toda área do circuito missionário, " \
                "foi com os povos de fala Cariri ou Kiriri ou Kariri ou Quiriri " \
                "que os jesuítas se concentraram em desenvolver seus conhecimentos linguísticos.",  size=18),
                ft.Text("O povo Kiriri é um dos únicos povos indígenas do sertão que " \
                 "teve sua língua registrada naquela época e que não foram praticamente extintos. " \
                 "É o único povo do semiárido, cujo conhecimento da língua são herdados da Gramática- " \
                 "A Artes de Grammatica da Lingua Brasilica da Nação Kariri e Catecismo - " \
                 "Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri escritos " \
                 "pelo italiano Padre Mamiani e pelo Catecismo-  Katecismo Indico da Lingua Kariris, " \
                 "escrito pelo capuchinho francês Frei Bernardo de Nantes. " \
                 "É necessário pontuar que o Mamiani escreveu sobre o dialeto Kipeá, enquanto " \
                 "Nantes escreve sobre o Dzubukuá. Com o passar do tempo, os pesquisadores " \
                 "descobriram mais dialetos do Kiriri: o Kamurú e Sapuyá ou Pedra Branca.", size=18),
                ft.Text("Como se deu o processo de substituição da língua Kiriri pelo Português?", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("O povo esteve sob influência de diversos fatores durante sua colonização, " \
                "os conflitos com os fazendeiros, que dominavam os indígenas para os tornar mãos de obra, " \
                "forçando o povo a aprender português.  " \
                "O forte contato e influência dos Jesuítas nas aldeias, " \
                "que catequizavam os indígenas. Como as aldeias, a criação de gado também seguia o " \
                "curso dos rios, principalmente o do São Francisco, então a região se tornou uma rota de ligação entre o sertão e o litoral, o que criou um fluxo de pessoas forçando os Kiriris a usarem o português para fins comerciais e comunicativos. Todos esses fatores, em muitos casos, resultaram também no genócidio de milhares de Kiriris, principalmente os que resistiam e tentaram reivindicar seus espaços de lutas contra a dominação. ", size=18),
                ft.Text("Dessa forma, o Kiriri se tornou uma língua adormecida  fazendo com que uma comunidade que poderia ser bilíngue passe a ser monolíngue, possuindo apenas poucos dados de uma memória de sua língua nativa.", size=18),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # -------- PROJETO --------
    def tela_projeto():
        return ft.Column(
            [
                ft.Text("Página sobre o Projeto", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(
                "O presente projeto tem como objetivo a elaboração de um aplicativo para tradução lexical "
                "do português para uma língua indígena brasileira, a língua Kiriri, registrada no século XVII. "
                "Pretende-se utilizar o corpus do 'Pequeno Dicionário da Língua Kiriri' em elaboração a partir "
                "dos dados registrados na Arte de Grammatica da Língua Brazílica da Nação Kiriri (1699) e no "
                "Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri (1698), de autoria do padre "
                "jesuíta Ludovico Vicenzo Mamiani. Pretende-se oferecer à comunidade Kiriri, do semiárido baiano, "
                "um recurso tecnológico que pode ser utilizado nas escolas indígenas como parte do projeto de "
                "retomada da língua indígena ancestral.",
                size=18
                ),
                ft.Text("Este trabalho tem como objetivo trazer conhecimento e dar visibilidade a esta"
                "língua ao tempo em que se insere como projeto de revitalização linguística,"
                "desempenhando um papel social e político fundamental ao fortalecimento da identidade"
                "histórica, cultural e linguística do povo Kiriri.", size=18),
                ft.Text("O nome “Kiri”, para o App, é selecionado como homenagem ao povo Kiriri,"
                "referindo-à àrvore chamada Kiri, que inspira o nome adotado pela etnia. Nasce com a"
                "intenção de atuar junto à comunidade, além de promover a disseminação da língua"
                "indígena Kiriri, um conhecimento necessário à comunidade que se encontra em situação"
                "de retomada linguística.", size=18),
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