from django import forms
from django.contrib.auth.models import User
from .models import User


# Form to register a new user
class ContactForm(forms.Form):
    first_name = forms.CharField(required=False, max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    mail = forms.EmailField(label='Your email', max_length=50)
    address = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(widget=forms.PasswordInput())

# Form to login an existing user
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


# Form to edit the details of the current user
class EditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    address = forms.CharField(max_length=80, required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address')
