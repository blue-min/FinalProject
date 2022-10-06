from django import forms

class CreateB(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)