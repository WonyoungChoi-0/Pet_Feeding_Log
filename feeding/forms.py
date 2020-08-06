from django import forms
from feeding.models import Feeding_Entry

class Feeding_Entry_Form(forms.ModelForm):
    class Meta():
        model = Feeding_Entry
        fields = '__all__'
