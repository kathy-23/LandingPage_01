from django import forms

class addForum(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
class addComent(forms.Form):
    content= forms.CharField(max_length=400)