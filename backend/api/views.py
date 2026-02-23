from rest_framework import viewsets
from .models import Traducao
from .serializers import TraducaoSerializer
from deep_translator import GoogleTranslator
from django.http import HttpResponse

# ViewSet da API
class TraducaoViewSet(viewsets.ModelViewSet):
    queryset = Traducao.objects.all()
    serializer_class = TraducaoSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        texto = validated_data.get("texto_original")
        origem = validated_data.get("idioma_origem")
        destino = validated_data.get("idioma_destino")

        traduzido = GoogleTranslator(source=origem, target=destino).translate(texto)

    # Define os campos conforme idioma
        if origem == "português":
            idioma_portugues = texto
            idioma_kiriri = traduzido
        else:
            idioma_portugues = traduzido
            idioma_kiriri = texto

    # Salva todos os campos obrigatórios do model
        serializer.save(
        texto_traduzido=traduzido,
        idioma_portugues=idioma_portugues,
        idioma_kiriri=idioma_kiriri
    )

# View para a raiz /
def home(request):
    return HttpResponse("Bem-vindo à API do Tradutor!")