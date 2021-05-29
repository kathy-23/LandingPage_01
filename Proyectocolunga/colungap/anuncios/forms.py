from django import forms

class addanuncio(forms.Form):
    titulo = forms.CharField(max_length=200)
    comentario = forms.CharField(max_length=2000)
    