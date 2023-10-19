from django import forms
from apps.galeria.models import Fotografia

# é feito dessa forma quando já existe um model
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        # O atributo chamado exclude, nele vamos indicar os inputs que não queremos exibidos. 
        # Vamos inserir nele o publicada. Como o exclude indica uma lista, colocaremos entre colchetes.
        exclude = ['publicar',]
        # Aqui se personaliza os labels dos campos do model
        labels = {
            'descricao' : 'Descrição',
            'usuario' : 'Usuário',
        }
        # O widgets serve para indicar quais inputs devem aparecer no formulário. 
        # Pois precisamos definir quais classes do CSS devem operar em cada uma delas, além de outras coisas menores. 
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_cadastro': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'                    
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }