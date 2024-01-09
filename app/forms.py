from django import forms
from .models import Colis

class ColisForm(forms.ModelForm):
    class Meta:
        model = Colis
        fields = ['titre', 'description', 'source', 'destination', 'proprietaire', 'contact', 'etat',]
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'proprietaire': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
         
        }


# forms.py

class CodeColisForm(forms.Form):
    code_colis = forms.CharField(
        label='Code du colis',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
