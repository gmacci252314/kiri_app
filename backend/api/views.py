from rest_framework import viewsets
from .models import Traducao
from .serializers import TraducaoSerializer
from django.http import HttpResponse


class TraducaoViewSet(viewsets.ModelViewSet):
    queryset = Traducao.objects.all()
    serializer_class = TraducaoSerializer


def home(request):
    return HttpResponse("Bem-vindo à API do Tradutor!")