from django import forms

class addForum(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=2000)
class addComent(forms.Form):
    content= forms.CharField(max_length=400)