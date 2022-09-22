from rest_framework.serializers import ModelSerializer
from .models import Morador, Pessoa

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','nome', 'data_de_nascimento', 'documento', 'tipo_documento')


class MoradorSerializer(ModelSerializer):
    pessoa = PessoaSerializer()
    class Meta:
        model = Morador
        fields = ('id', 'apto', 'pessoa')

    def create(self, validated_data):
        pessoa_data = validated_data.get('pessoa')
        pessoa = Pessoa.objects.create(**pessoa_data)
        apto = validated_data.get('apto')
        morador = Morador.objects.create(apto=apto, pessoa=pessoa)
        return morador
