from django.shortcuts import render , get_object_or_404 , redirect
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
            queryset = queryset.filter(idioma_kiriri__iexact=palavra)

        elif palavra and idioma == "portugues":
            queryset = queryset.filter(idioma_portugues__iexact=palavra)

        return queryset


# 🔥 TEM QUE FICAR FORA DA CLASSE
def traducao_list(request):
    consulta = request.GET.get("q")

    traducoes = Traducao.objects.all()

    if consulta:
        traducoes = traducoes.filter(
            Q(idioma_kiriri__icontains=consulta) |
            Q(idioma_portugues__icontains=consulta)
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
        idioma_kiriri = request.POST.get("idioma_kiriri")
        idioma_portugues = request.POST.get("idioma_portugues")

        Traducao.objects.create(
            idioma_kiriri=idioma_kiriri,
            idioma_portugues=idioma_portugues
        )

        return redirect('traducao_list')

    return render(request, "api/cadastrar.html")

def editar_traducao(request, id):
    traducao = get_object_or_404(Traducao, id=id)

    if request.method == "POST":
        traducao.idioma_kiriri = request.POST.get("idioma_kiriri")
        traducao.idioma_portugues = request.POST.get("idioma_portugues")
        traducao.save()

        return redirect('traducao_list')

    return render(request, "api/editar.html", {
        "traducao": traducao
    })

def deletar_traducao(request, id):
    traducao = get_object_or_404(Traducao, id=id)
    traducao.delete()
    return redirect('traducao_list')

def home(request):
    return HttpResponse("Bem-vindo à API do Tradutor!")