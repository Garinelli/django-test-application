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

class CreateTaskForm(forms.Form):
    PRIORITY_CHOICES = [
        ('Н', 'Низкий'),
        ('С', 'Средний'),
        ('В', 'Высокий')
    ]

    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Заголовок задачи'})
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Описание задачи'})
    )
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        required=True
    )
    