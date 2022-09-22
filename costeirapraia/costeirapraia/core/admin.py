from django.contrib import admin
from .models import ControleAcesso, Morador, Veiculo, Visitante

# Register your models here.

admin.site.register(ControleAcesso)
admin.site.register(Morador)
admin.site.register(Veiculo)
admin.site.register(Visitante)