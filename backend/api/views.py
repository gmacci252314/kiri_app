from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Traducao
from .serializers import TraducaoSerializer
from django.http import HttpResponse
from django.db.models import Q


class TraducaoViewSet(viewsets.ModelViewSet):
    queryset = Traducao.objects.all()
    serializer_class = TraducaoSerializer

    def get_queryset(self):
        queryset = Traducao.objects.all()

        palavra = self.request.query_params.get("palavra")
        idioma = self.request.query_params.get("idioma")

        if palavra and idioma == "kiriri":
            queryset = queryset.filter(kiriri_antigo__iexact=palavra)

        elif palavra and idioma == "portugues":
            queryset = queryset.filter(sentido__iexact=palavra)

        return queryset


def traducao_list(request):
    consulta = request.GET.get("q")
    traducoes = Traducao.objects.all()

    if consulta:
        traducoes = traducoes.filter(
            Q(kiriri_antigo__icontains=consulta) |
            Q(sentido__icontains=consulta)
        )

    return render(
        request,
        "api/traducao_list.html",
        {
            "traducoes": traducoes,
            "consulta": consulta,
        }
    )


def cadastrar_traducao(request):

    if request.method == "POST":

        kiriri_antigo = request.POST.get("kiriri_antigo")
        interp_fonetica = request.POST.get("interp_fonetica")
        atualizacao_escrita = request.POST.get("atualizacao_escrita")
        sentido = request.POST.get("sentido")
        referencia = request.POST.get("referencia")

        # Verifica se a combinação de léxico e sentido já existe
        if Traducao.objects.filter(
            kiriri_antigo__iexact=kiriri_antigo,
            sentido__iexact=sentido
        ).exists():

            return render(
                request,
                "api/cadastrar.html",
                {
                    "erro": "Léxico já está cadastrado na base de dados."
                },
            )
        
        Traducao.objects.create(
            kiriri_antigo=kiriri_antigo,
            interp_fonetica=interp_fonetica,
            atualizacao_escrita=atualizacao_escrita,
            sentido=sentido,
            referencia=referencia
        )

        return redirect("traducao_list")

    return render(request, "api/cadastrar.html")


def editar_traducao(request, id):

    traducao = get_object_or_404(Traducao, id=id)

    if request.method == "POST":

        kiriri_antigo = request.POST.get("kiriri_antigo")
        interp_fonetica = request.POST.get("interp_fonetica")
        atualizacao_escrita = request.POST.get("atualizacao_escrita")
        sentido = request.POST.get("sentido")
        referencia = request.POST.get("referencia")

        # Verifica se já existe outro registro
        # com a mesma combinação de léxico e sentido
        if Traducao.objects.filter(
            kiriri_antigo__iexact=kiriri_antigo,
            sentido__iexact=sentido
        ).exclude(id=id).exists():

            return render(
                request,
                "api/editar.html",
                {
                    "traducao": traducao,
                    "erro": "Léxico já está cadastrado na base de dados."
                },
            )

        traducao.kiriri_antigo = kiriri_antigo
        traducao.interp_fonetica = interp_fonetica
        traducao.atualizacao_escrita = atualizacao_escrita
        traducao.sentido = sentido
        traducao.referencia = referencia

        traducao.save()

        return redirect("traducao_list")

    return render(
        request,
        "api/editar.html",
        {
            "traducao": traducao
        }
    )


def deletar_traducao(request, id):

    traducao = get_object_or_404(Traducao, id=id)

    traducao.delete()

    return redirect("traducao_list")


def home(request):
    return HttpResponse("Bem-vindo à API do Tradutor!")