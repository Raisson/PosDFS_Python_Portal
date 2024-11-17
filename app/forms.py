from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Projetos, Atividades

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','phone_number']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        profile = UserProfile(user=user,phone_number=self.cleaned_data['phone_number'])
        profile.save()
        return user
    
class ProjetoForm(ModelForm):
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
    )
    class Meta:
        model = Projetos
        fields = ['nome','descricao','prioridade','data_inicio','data_fim']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AtividadeForm(ModelForm):
    status_atividade = forms.ChoiceField(choices=Atividades.STATUS, label='Status', widget=forms.Select(attrs={'class': 'form-control'})) # Para campo select
    class Meta:
        model = Atividades
        fields = ['nome','projeto','user','status_atividade','prioridade','descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }