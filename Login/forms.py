from django import forms


class LogInForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
