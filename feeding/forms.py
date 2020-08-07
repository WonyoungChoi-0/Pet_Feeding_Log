from django import forms
from feeding.models import Feeding_Entry, Pet

class Feeding_Entry_Form(forms.ModelForm):
    class Meta():
        model = Feeding_Entry
        fields = '__all__'

class Pet_Form(forms.ModelForm):
    class Meta():
        model = Pet
        fields = ('name', 'species', 'age', 'diet', 'profile_pic')
        labels={
            'profile_pic': ('Pet Profile Picture'),
        }
