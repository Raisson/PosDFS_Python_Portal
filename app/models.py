from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # phone = models.CharField(max_length=20)
    # phone_number = models.CharField(max_length=20)

class Projetos(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False, help_text='Informe o nome')
    # preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    def __str__(self):
        return self.nome



class Atividades(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE, related_name='atividades')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    nome = models.CharField(max_length=200, blank=False, null=False, help_text='Informe o nome')
    STATUS = [
        ('PENDENTE', "PENDENTE"),
        ('EXECUTANDO', "EXECUTANDO"),
        ('FINALIZADO', "FINALIZADO"),
    ]
    status_atividade = models.CharField(
        max_length=12,
        choices=STATUS,
        default='PENDENTE',
    )
    # preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()