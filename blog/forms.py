from django import forms

from blog.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', ]


class ComentarioForm(forms.Form):
    autor = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
            }
        )
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Deixe seu comentário',
            }
        )
    )
