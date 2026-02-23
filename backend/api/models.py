from django.db import models
class Traducao(models.Model):
    texto_original = models.TextField()
    idioma_origem = models.CharField(max_length=50)
    idioma_destino = models.CharField(max_length=50)

    idioma_portugues = models.TextField()
    idioma_kiriri = models.TextField()
    texto_traduzido = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto_original[:50]
