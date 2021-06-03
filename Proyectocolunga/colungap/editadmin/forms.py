from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .models import Miembro
class AddUserForm(UserCreationForm):
    telefono = forms.CharField(max_length=12)
    cargo = forms.CharField(max_length=80)
    organizacion = forms.CharField(max_length=80)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email':'Correo',
            'password':'Contraseña'
        }
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(AddUserForm, self)
        email=self.data['email']
        user.save()
        usuario=User.objects.get(email=email)
        print(email)
        user_profile = Miembro(user_id=usuario.id ,telefono=self.cleaned_data['telefono'], 
            cargo=self.cleaned_data['cargo'],organizacion=self.cleaned_data['organizacion'])
        user_profile.save()
        return user, user_profile



class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=80)
    telefono = forms.CharField(max_length=12)
    cargo = forms.CharField(max_length=80)
    organizacion = forms.CharField(max_length=80)
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        required=False,
        widget=forms.PasswordInput,
)
    class Meta:
        labels={
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email':'Correo',
            'password':'Contraseña'
        }