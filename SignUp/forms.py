from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='Name of Applicant', max_length=50)
    email = forms.EmailField(label='Email@abc.xyz', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
