from django import forms
from .models import Cliente, Imovel

class LocacaoFilterForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False, label='Cliente')
    imovel = forms.ModelChoiceField(queryset=Imovel.objects.all(), required=False, label='Imóvel')
    data_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Data de Início')
    data_fim = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Data de Fim')
    ativo = forms.ChoiceField(choices=[('', 'Todos'), (True, 'Ativa'), (False, 'Cancelada')], required=False, label='Status')


class ImovelFilterForm(forms.Form):
    codigo = forms.CharField(max_length=20, required=False, label='Código')
    disponivel = forms.ChoiceField(choices=[('', 'Todos'), (True, 'Disponível'), (False, 'Alugado')], required=False, label='Status')
    tipo = forms.CharField(max_length=50, required=False, label='Tipo')
    preco_min = forms.DecimalField(required=False, label='Preço mínimo')
    preco_max = forms.DecimalField(required=False, label='Preço máximo')

