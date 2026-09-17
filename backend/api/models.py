from django.db import models
class Traducao(models.Model):

    # Novos campos 
    kiriri_antigo = models.TextField(blank=True)
    interp_fonetica = models.TextField(blank=True)
    atualizacao_escrita = models.TextField(blank=True)
    sentido = models.TextField(blank=True)
    referencia = models.TextField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kiriri_antigo or self.idioma_kiriri
