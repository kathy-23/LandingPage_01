from django import forms

class addanuncio(forms.Form):
    titulo = forms.CharField(max_length=200)
    comentario = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))