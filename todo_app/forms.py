from django import forms
from .models import *

class CreateToDoForm(forms.ModelForm):#modelden istifade ederek hazirlayacam bu formu ona gore forms.ModelFormdan istifade etdim eger sifirdan bir form yaratmag isteyiremse onfa forms.Formdan istifade etmeliyem

    class Meta:
        model = ToDo
        fields = ['description']


class UpdateForm(forms.ModelForm):#eger Model istifade ederek bir form yaradiramsa onda ModelFormlardan istifade etmek lazimdir yox eger oz formumu yaratmag isteyiremse  0 dan onda forms.Formdan istifade etmek lazimdir
    class Meta:
        model = ToDo
        fields = ['description']