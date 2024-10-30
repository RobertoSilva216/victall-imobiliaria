from django import forms
from .models import Cliente, Imovel, Locacao

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['codigo', 'descricao', 'tipo', 'preco', 'imagem']

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'data_inicio']
