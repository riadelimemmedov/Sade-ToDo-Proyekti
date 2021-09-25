from django import forms
from .models import *

class CreateToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ['description']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['description']