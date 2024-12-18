from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

TIPOS_PRIORIDADES = [
    ('BAIXA', "BAIXA"),
    ('MEDIA', "MEDIA"),
    ('ALTA', "ALTA"),
]
class Projetos(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False, help_text='Informe o nome')
    prioridade = models.CharField(
        max_length=12,
        choices=TIPOS_PRIORIDADES,
        default='BAIXA',
    )
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    @property
    def percentual_concluido(self):
        atividades = self.atividades.all()  # Relacionamento inverso
        total_atividades = atividades.count()
        atividades_concluidas = atividades.filter(status_atividade="FINALIZADO").count()

        if total_atividades == 0:
            return 0  # Evita divisão por zero
        return int((atividades_concluidas / total_atividades) * 100)
    
    def __str__(self):
        return self.nome


class Atividades(models.Model):
    projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE, related_name='atividades')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    nome = models.CharField(max_length=200, blank=False, null=False, help_text='Informe o nome')
    prioridade = models.CharField(
        max_length=12,
        choices=TIPOS_PRIORIDADES,
        default='BAIXA',
    )
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
    descricao = models.TextField()
    def __str__(self):
        return self.nome