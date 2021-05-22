from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']

class RemoveUserForm(forms.Form):
    email = forms.EmailField(max_length=60)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=80)
    password = forms.CharField(max_length=60)