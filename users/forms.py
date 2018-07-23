from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(max_length=255,
                            widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class' : 'form-control'}))