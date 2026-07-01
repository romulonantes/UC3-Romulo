from django import forms
from .models import Fabricante, Produto

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'idTxtNomeFabricante',
                'name': 'nomeFabricante',
                'required': True,
                'minlength': '1',
                'maxlength': '70',
                'placeholder': 'Digite o nome do fabricante'
            })
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip()
        if not nome:
            raise forms.ValidationError('O nome do fabricante é obrigatório.')
        return nome

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_compra', 'preco_venda', 'cor', 'data_fabricacao', 'imagem', 'fabricante']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','id': 'idTxtNomeProduto','name': 'nomeProduto','required': True,'maxlength': '70'}),
            'preco_compra': forms.NumberInput(attrs={'class': 'form-control','id': 'idTxtPrecoCompra','name': 'precoCompra','required': True,'step': '0.01'}),
            'preco_venda': forms.NumberInput(attrs={'class': 'form-control','id': 'idTxtPrecoVenda','name': 'precoVenda','required': True,'step': '0.01'}),
            'cor': forms.Select(attrs={'class': 'form-select','id': 'idBSelCorProduto','name': 'corProduto','required': True}),
            'data_fabricacao': forms.DateInput(attrs={'class': 'form-control','id': 'idTxtDataFabricacao','name': 'dataFabricacao','type': 'date','required': True}),
            'imagem': forms.TextInput(attrs={'class': 'form-control','id': 'idTxtImagemProduto','name': 'imagemProduto','required': True,'maxlength': '25','placeholder': 'ex: tenis01.jpg'}),
            'fabricante': forms.Select(attrs={'class': 'form-select','id': 'idBSelFabricanteProduto','name': 'fabricanteProduto','required': True}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome'].strip()
        if not nome:
            raise forms.ValidationError('O nome do produto é obrigatório.')
        return nome

    def clean_imagem(self):
        imagem = self.cleaned_data['imagem'].strip()
        if not imagem:
            raise forms.ValidationError('O nome da imagem é obrigatório.')
        return imagem
