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
                ft.Text("""A história do povo Kiriri começou a ser contada a partir dos primeiros contatos com os europeus. O povo Kiriri foi encontrado espalhado pelo interior do Nordeste brasileiro, predominantemente entre as margens do São Francisco e as do Rio Acaraú, um extenso território, do Ceará à Paraíba e até uma porção setentrional do sertão baiano (Dantas, Sampaio e Carvalho (1992, p. 432). Nas palavras de Galindo (2017, p. 95), “o gentílico cariri designa um grupo étnico de larga dispersão geográfica do Nordeste brasileiro 
                Foi nas terras dos Kiriri que os primeiros jesuítas se instalaram, na segunda metade do século XVII, no sertão nordestino. É possível observar que em toda área do circuito missionário, foi com os povos de fala Kiriri (Cariri/Kariri/Quiriri) que os jesuítas se concentraram em desenvolver seus conhecimentos linguísticos. O fato de essa ser a língua escolhida para a catequese indica a importância dela, como uma língua falada em grande expansão territorial, como o era o Tupi Antigo, falado no litoral, por diferentes grupos. Capistrano de Abreu e Thomas Pompeu Sobrinho destacam os cariris como dominantes (Pompeu Sobrinho, 1934, tomo II, pp. 289-305). A exemplo do tupi no litoral, a língua cariri tornou-se ferramenta que franqueava aos religiosos a interação com uma fração expressiva dos habitantes nativos no rio São Francisco, mesmo privando da identidade de uma coletividade de povos a eles não aparentados (Galindo, 2017, p. 62)"
                O povo Kiriri é um dos únicos povos indígenas do sertão que teve sua língua registrada naquela época. É o único povo do semiárido cujos dados da língua podem ser recuperados por meio das obras produzidas pelos missionários: A Arte de Grammatica da Lingua Brasilica da Nação Kariri (Mamiani, 1699) e o Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri (Mamiani, 1798), com o registro da variedade Kipeá, e o Katecismo Indico da Lingua Kariris (Nantes, 1709), que registra a variedade Dzubukuá. O avanço dos estudos linguísticos permitiu a identificação de quatro povos de língua aparentada, agrupados em uma família, a família linguística Kiriri, o que inclui o Kamurú, o Sapuyá ou Pedra Branca, o Kipeá e o Dzubukuá (Cf. Von Martius, 1867, Adam,1897, Santos, 2020).
                O povo esteve sob influência de diversos fatores durante a colonização, os conflitos com os fazendeiros, que dominavam os indígenas para os tornar mãos de obra, forçando o povo a aprender português, o forte contato e influência dos Jesuítas nas aldeias, com a catequese, dentre outros fatores. Como as aldeias, a criação de gado também seguia o curso dos rios, principalmente o do São Francisco, então a região se tornou uma rota de ligação entre o sertão e o litoral, o que criou um fluxo de pessoas forçando os Kiriris a usarem o português para fins comerciais e comunicativos. Todos esses fatores, em muitos casos, resultaram também no genocídio de milhares de Kiriris, principalmente os que resistiam e tentaram reivindicar seus espaços de luta contra a dominação. Dessa forma, ao longo dos últimos séculos, a língua Kiriri se tornou uma língua adormecida, fazendo com que a comunidade descendente, que poderia ser bilíngue, passasse a ser monolíngue, apresentando apenas uma memória de alguns dados lexicais da sua língua.
                A luta do povo Kiriri atualmente não é apenas por questões territoriais, ou por reconhecimento social, mas também, há um forte e inspirador movimento pela retomada linguística. Nesse afã, diferentes projetos têm sido propostos e é nesse contexto que este projeto emerge, tendo definido como objetivo geral elaborar um aplicativo para tradução lexical do português para uma língua indígena brasileira, a língua Kiriri, registrada no século XVII, com base nos dados registrados na Arte de Grammatica da Língua Brazílica da Nação Kiriri (1699) e no Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri (1698), do padre jesuíta Ludovico Vicenzo Mamiani.
                Pretende-se oferecer à comunidade Kiriri, do semiárido baiano, um recurso tecnológico que pode ser utilizado nas escolas indígenas, como parte integrante do projeto de retomada da língua indígena ancestral e pela comunidade indígena como um todo.""", size=18),
                ft.TextButton("Voltar", on_click=lambda e: page.go("/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        
            scroll=ft.ScrollMode.AUTO,
            expand=True,
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
                ft.Text("Este trabalho tem como objetivo trazer conhecimento e dar visibilidade a  esta"
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