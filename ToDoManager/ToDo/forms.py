from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
    )

class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )
