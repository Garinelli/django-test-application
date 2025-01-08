from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Низкий', 'Н'),
        ('Средний', 'С'),
        ('Высокий', 'В')
    ]


    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=7,
        choices=PRIORITY_CHOICES
    )

    class Meta:
        db_table = 'tasks'
        