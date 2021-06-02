from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email':'Correo',
            'password':'Contraseña'
        }

class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=80)
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
)
    class Meta:
        labels={
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email':'Correo',
            'password':'Contraseña'
        }