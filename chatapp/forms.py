from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from.models import CustomUser,Sharks
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=('email',)

class AddSharkForm(forms.Form):
    class Meta:
        model:Sharks
        fields='__all__'

class UpdateSharkForm(forms.Form):
    class Meta:
        model:Sharks
        fields='__all__'
        