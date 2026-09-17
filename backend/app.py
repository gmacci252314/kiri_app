import flet as ft
import requests


API_URL = "http://127.0.0.1:8000/api/traducoes/"


def main(page: ft.Page):
    page.title = "Tradutor Kiri"
    page.padding = 20

    # -------- MENU --------
    def tela_menu():
        print("Entrou na tela_menu")

        return ft.Column(
            [
                ft.Text(
                    "Tradutor Kiri",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

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

        txt_input = ft.TextField(
            label="Texto a traduzir",
            width=400
        )

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

        resultado = ft.Text(
            size=20,
            weight=ft.FontWeight.BOLD
        )

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
                            and item["sentido"].lower() == palavra
                        ):
                            resultado.value = (
                                f"Tradução: {item['kiriri_antigo']}"
                            )
                            encontrou = True
                            break

                        # Kiriri -> Português
                        elif (
                            origem == "kiriri"
                            and destino == "português"
                            and item["kiriri_antigo"].lower() == palavra
                        ):
                            resultado.value = (
                                f"Tradução: {item['sentido']}"
                            )
                            encontrou = True
                            break

                    if not encontrou:
                        resultado.value = (
                            f"A palavra '{palavra}' não foi encontrada."
                        )

                else:
                    resultado.value = "Erro ao acessar a API."

            except Exception as erro:
                resultado.value = f"Erro: {erro}"

            page.update()

        return ft.Column(
            [
                ft.Text(
                    "Tradutor Kiriri",
                    size=25,
                    weight=ft.FontWeight.BOLD
                ),

                txt_input,

                ft.Row(
                    [
                        dropdown_origem,

                        ft.IconButton(
                            icon=ft.icons.SWAP_HORIZ,
                            on_click=inverter_idiomas
                        ),

                        dropdown_destino,

                        ft.ElevatedButton(
                            "Traduzir",
                            on_click=traduzir
                        ),
                    ],
                    spacing=10,
                ),

                resultado,

                ft.TextButton(
                    "Voltar",
                    on_click=lambda e: page.go("/")
                ),
            ]
        )

    # -------- KIRIRI --------
    def tela_kiriri():
        return ft.Column(
            [
                ft.Text(
                    "História do povo Kiriri",
                    size=20,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "No período da colonização brasileira, as regiões litorâneas de Pernambuco e da Bahia possuíam um ambiente propício para as plantações de Pau-Brasil, devido ao solo fértil e aos bons portos ali presentes. Mais tarde, os colonos avançaram para o interior do Brasil, rumo ao sertão, especialmente após as invasões holandesas e francesas, que ameaçaram o domínio português sobre a já explorada região litorânea e sobre as “inexploradas” terras do sertão. "
                    "Sendo assim, após a expulsão dos holandeses e franceses, a Coroa iniciou o fortalecimento da exploração e conquista do semiárido brasileiro, através das doações das Sesmarias para fazendeiros e o envio de Jesuítas para catequizar os povos indígenas que viviam na região (Dantas, Sampaio e Carvalho, 1992, pp. 431-456). "
                    "É nesse contexto, nos primeiros contatos dos jesuítas com os indígenas, que começam a surgir os registros sobre o povo Kiriri, especialmente sobre a sua língua. Este povo, segundo a historiografia, estava espalhado pelo interior do semiárido, entre as margens do Rio São Francisco e as do Rio Acaraú. De toda área, os missionários se concentraram em desenvolver seus conhecimentos linguísticos sobre o povo Kiriri. Dois deles foram os responsáveis por registrar variedades dessa língua, ainda durante colonização. O Kipeá foi registrado pelo padre jesuíta Ludoico Vicenzo Mamiani, no século XVII, no Catecismo da doutrina christãa na lingua brasilica da naçam Kiriri, em 1698 e na Arte de grammatica da lingua brasilica da Naçam kiriri, e em 1699. Além disso, o Dzubukuá foi registrado no Catecismo da lingua Kariris, pelo Fr. Bernado Nantes, no século XVIII, em 1707, reimpresso em edição facsimilar, por Julio Platzman, em 1896, apresentando as semelhanças e diferenças com o Kipeá. "
                    "O Kiriri virou a ferramenta que ligava os religiosos a uma boa parte dos indígenas do sertão brasileiro, sendo esta a língua da catequese no sertão. Contudo, por diversos fatores, houve a substituição linguística do Kiriri pela Língua Portuguesa, como os conflitos com os fazendeiros que dominavam os indígenas para os tornar mãos-de-obra, forçando-os a aprender o português, o genocídio de milhares de indígenas que tentaram reivindicar seus espaços ou lutar contra a dominação religiosa ou aquelas vindas dos fazendeiros. Outra forte influência, foi a criação de gado, uma vez que como as aldeias seguiam o curso dos rios, principalmente o do Rio São Francisco, a região se tornou uma rota de ligação entre o sertão e o litoral, criando um fluxo intenso de pessoas, o que fez com que os Kiriris passassem a usar o português para fins comerciais (Santos, 2020, p.66)."
                    "Foi assim, que com o passar dos séculos, a língua Kiriri se tornou uma língua adormecida, fazendo com que suas comunidades descendentes guardassem apenas uma esparsa memória de dados lexicais. Foi a partir do próprio desejo da comunidade que nasceu a presente proposta, cujo o objetivo principal é dar visibilidade social para o povo e para a língua Kiriri procurando assegurar e fortalecer aspectos identitários, culturais, linguísticos e históricos.",
                    size=17
                ),

                ft.Text(
                    "Referências Bibliográficas",
                    size=16,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "DANTAS, Beatriz G.; SAMPAIO, José Augusto L.; CARVALHO, Maria Rosário G. de. Os povos indígenas no Nordeste brasileiro: um esboço histórico. In: CUNHA, Manuela Carneiro da (org.). História dos índios no Brasil. São Paulo: Companhia das Letras, Secretaria Municipal de Cultura, FAPESP, 1992, pp. 431-456."
                    "FERNANDES, Giovanna M. ; AZEVEDO, Micheline Maria C.; IVO, Ivana Pereira, 2026 (No prelo)"
                    "MAMIANI, Luiz Vincencio. Arte de Grammatica da Lingua Brazilica da Naçam Kiriri. Lisboa: Miguel Deslandes, 1699."
                    "MAMIANI, Luiz Vincencio. Arte de Grammatica da Lingua Brazilica da Nação Kiriri. 2a. edição (com notas introdutórias de Batista Caetano de Almeida Nogueira). Rio de Janeiro: Bibliotheca Nacional, 1877 [1699]."
                    "MAMIANI, Luiz Vincencio. Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri. Lisboa: Miguel Deslandes, 1698."
                    "MAMIANI, Luiz Vincencio. 1942 [1698]. Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri. Lisboa. (Edição fac-similar, Rio de Janeiro: Biblioteca Nacional)."
                    "NANTES, Frei Bernardo de. Catecismo Indico da Língua Kariris. Lisboa: Valentim da Costa Deslandes, 1709."
                    "NANTES, Frei Bernardo de. Catecismo Indico da Língua Kariris. Lisboa: Valentim da Costa Deslandes. Edição Faximilar por Julio Platzmann. Leipzig. B. G. Teubner, 1896 [1709]."
                    "SANTOS, Ane Luíse Silva Mecenas. O Trato da Perpétua Tormenta: a conversão Kiriri nos sertões dentro da América portuguesa. Aracaju: Editora Diário Oficial do Estado de Sergipe - EDISE, 2020, pp. 29-160.",
                    size=12,
                    weight=ft.FontWeight.BOLD
                ),

                ft.TextButton(
                    "Voltar",
                    on_click=lambda e: page.go("/")
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )

    # -------- PROJETO --------
    def tela_projeto():
        return ft.Column(
            [
                ft.Text(
                    "Página sobre o Projeto",
                    size=40,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "O Aplicativo Kiri é uma ferramenta tecnológica concebida como parte do projeto de "
                    "retomada linguística da língua Kiriri. A solução tecnológica consiste em um tradutor lexical "
                    "para o Kiriri Antigo, língua descrita no século XVII. Como fundamentação teórica, o projeto se "
                    "baseia em duas áreas de conhecimento, a Linguística, especificamente a Linguística Sistêmico-Funcional "
                    "(Halliday e Matthiessen, 2014) e a Tecnologia da Informação, principalmente os pressupostos teóricos "
                    "e metodológicos da Tecnologia Social (Dagnino, 2014), que inspira a criação de métodos, produtos e "
                    "técnicas desenvolvidas a partir da perspectiva e total colaboração das comunidades envolvidas, para "
                    "sanar questões de exclusão social e tecnológica. Baseada em uma metodologia ancorada em aspectos interdisciplinares, "
                    "de natureza qualitativa, documental e aplicada. Sendo assim, pensando na adesão do aplicativo pelo "
                    "povo Kiriri, por terem acesso a dispositivos móveis em língua portuguesa, o aplicativo foi desenvolvido "
                    "por meio dos frameworks gratuitos: Django e Flutter e com o Flet como biblioteca de criação de interface. "
                    "Para o corpus inicial do projeto foram empregados os dados linguísticos registrados na "
                    "Arte de Grammatica da Língua Brazílica da Nação Kiriri (Mamiani, 1699) e no "
                    "Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri (Mamiani, 1698). "
                    "Por meio do aplicativo, espera-se auxiliar a comunidade indígena na educação escolar "
                    "indígena e no processo de retomada linguística de sua língua ancestral. Palavras-chave: Línguas Indígenas, Kiriri Antigo, Retomada Linguística, Linguística, Tecnologia Social.",
                    size=17
                ),

                ft.Text(
                    "Referências Bibliográficas",
                    size=17,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "DAGNINO, Renato. Tecnologia social: contribuições conceituais e metodológicas. Campina Grande: EDUEPB; Florianópolis: Insular, 2014, pp. 71 – 108."
                    "DANTAS, Beatriz G.; SAMPAIO, José Augusto L.; CARVALHO, Maria Rosário G. de. Os povos indígenas no Nordeste brasileiro: um esboço histórico. In: CUNHA, Manuela Carneiro da (org.). História dos índios no Brasil. São Paulo: Companhia das Letras, Secretaria Municipal de Cultura, FAPESP, 1992, pp. 431-456."
                    "FERNANDES, Giovanna M. ; AZEVEDO, Micheline Maria C.; IVO, Ivana Pereira, 2026 (No prelo)"
                    "HALLIDAY, Michael Alexander Kirkwood; MATTHIESSEN, Christian Matthias Ingemar Martin. *Halliday's introduction to functional grammar. 4.ed. London: Routledge, 2014."
                    "MAMIANI, Luiz Vincencio. Arte de Grammatica da Lingua Brazilica da Naçam Kiriri. Lisboa: Miguel Deslandes, 1699."
                    "MAMIANI, Luiz Vincencio. Arte de Grammatica da Lingua Brazilica da Nação Kiriri. 2a. edição (com notas introdutórias de Batista Caetano de Almeida Nogueira). Rio de Janeiro: Bibliotheca Nacional, 1877 [1699]."
                    "MAMIANI, Luiz Vincencio. Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri. Lisboa: Miguel Deslandes, 1698."
                    "MAMIANI, Luiz Vincencio. 1942 [1698]. Catecismo da Doutrina Christãa na Lingua Brasilica da Nação Kiriri. Lisboa. (Edição fac-similar, Rio de Janeiro: Biblioteca Nacional)."
                    "SANTOS, Ane Luíse Silva Mecenas. O Trato da Perpétua Tormenta: a conversão Kiriri nos sertões dentro da América portuguesa. Aracaju: Editora Diário Oficial do Estado de Sergipe - EDISE, 2020, pp. 29-160.",
                    size=14,
                    weight=ft.FontWeight.BOLD
                ),

                ft.TextButton(
                    "Voltar",
                    on_click=lambda e: page.go("/")
                ),
            ]
        )

    # -------- ROTAS --------
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [tela_menu()]
                )
            )

        elif page.route == "/tradutor":
            page.views.append(
                ft.View(
                    "/tradutor",
                    [tela_tradutor()]
                )
            )

        elif page.route == "/kiriri":
            page.views.append(
                ft.View(
                    "/kiriri",
                    [tela_kiriri()]
                )
            )

        elif page.route == "/projeto":
            page.views.append(
                ft.View(
                    "/projeto",
                    [tela_projeto()]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)