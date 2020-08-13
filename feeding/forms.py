from django import forms
from feeding.models import Feeding_Entry, Pet
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Feeding_Entry_Form(forms.ModelForm):
    class Meta():
        model = Feeding_Entry
        fields = ('date', 'notes')

class Pet_Form(forms.ModelForm):
    class Meta():
        model = Pet
        fields = ('name', 'species', 'age', 'diet', 'profile_pic')
        labels={
            'profile_pic': ('Pet Profile Picture'),
        }

class User_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=256, required=True)
    last_name = forms.CharField(max_length=256, required=True)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
        labels={
            'username': ('Email'),
        }
        help_texts = {
            'username': None,
        }

    def clean_username(self):
        email = self.cleaned_data['username']

        if '@' not in str(email):
            raise ValidationError("Not a valid email")

        users = User.objects.all()

        for user in users:
            if user.username == email:
                raise ValidationError("Email already in system")

        return email

class User_Login(forms.Form):
    email = forms.CharField(max_length=256, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
