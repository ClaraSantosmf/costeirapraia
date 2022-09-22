from django.db import models

# Create your models here.


class Veiculo(models.Model):
    placa = models.CharField("placa", max_length=12)
    modelo = models.CharField("modelo", max_length=20)
    cor = models.CharField("cor", max_length=30)
    proprietario = models.ForeignKey("Pessoa", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'


class Pessoa(models.Model):
    class TipoDocumento(models.TextChoices):
        CPF = ('CPF', 'CPF')
        PASSAPORTE = ('PASSAPORTE', 'Passaporte')

    nome = models.CharField("Nome", max_length=100)
    data_de_nascimento = models.DateField("Data de nascimento")
    documento = models.CharField("Nº documento", max_length=50)
    tipo_documento = models.CharField("Tipo de documento", max_length=50, choices=TipoDocumento.choices)


class Visitante(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)
    apto = models.CharField("APTO", max_length=5, null=True, blank=True)
    prestador_servico = models.BooleanField("Prestador de Serviço", default=False)


class Morador(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)
    apto = models.CharField("APTO", max_length=5)

    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'


class ControleAcesso(models.Model):
    class EntradaSaida(models.TextChoices):
        ENTRADA = ('ENTRADA', 'Entrada')
        SAIDA = ('SAIDA', 'Saída') 

    entrada_saida = models.CharField("Entrada e saída", max_length=10, choices=EntradaSaida.choices)
    horario = models.DateTimeField("Horário", auto_now_add=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Controle de acesso'
        verbose_name_plural = 'Controles de acessos'
