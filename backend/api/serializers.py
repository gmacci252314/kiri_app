from rest_framework import serializers
from .models import Traducao

class TraducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traducao
        fields = '__all__'
        read_only_fields = ['criado_em',]