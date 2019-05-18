from django import forms


class RegisterForm(forms.Form):
    img = forms.FileField(label='')
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'login-inputname', 'placeholder': 'Full Name'}), label='')
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'login-inputname', 'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login-inputname', 'placeholder': 'Password'}), label='')
    repassword = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login-inputname', 'placeholder': 'Confirm PAssword'}), label='')
    phone_no = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'login-inputname', 'placeholder': '+91 9999999'}), label='')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'login-inputname','placeholder':'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-inputname', 'placeholder':'Password'}), label='')


class CartForm(forms.Form):
    quantity = forms.IntegerField(label='quantity', min_value=1, max_value=10)
