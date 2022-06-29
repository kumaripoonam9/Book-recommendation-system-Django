from django.forms import ModelForm
from manager.models import Person


class RegisterForm(ModelForm):

    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    password = forms.CharField(widget=PasswordInput)
    password2 = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)


class Meta:
    model = Person
    fields = ["firstname", "lastname", "email", "password", "password2"]
