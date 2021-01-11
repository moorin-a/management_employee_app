from .models import Staff
from django import forms

class InfoForm(forms.Form):
    name = forms.CharField(label='名前')
    email = forms.EmailField(label='Email')
    gender = forms.IntegerField(label='0:男性 1:女性')

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'gender']
