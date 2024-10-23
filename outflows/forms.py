from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowsForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantily', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantily': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantily': 'Quantidade',
            'description':  'Descrição',
        }

    def clean_quantily(self):
        quantily = self.cleaned_data.get('quantily')
        product = self.cleaned_data.get('product')

        if quantily > product.quantily:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantily} unidades;'
            )

        return quantily
