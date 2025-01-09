from django import forms
from django.core.exceptions import ValidationError

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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if (password and confirm_password) and (password != confirm_password):
            raise ValidationError('Пароли не совпадают')
        
        return cleaned_data


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
    