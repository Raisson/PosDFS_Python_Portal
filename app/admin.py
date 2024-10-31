from django.contrib import admin

# Register your models here.

from .models import Projetos, Atividades

admin.site.register(Projetos)
admin.site.register(Atividades)
