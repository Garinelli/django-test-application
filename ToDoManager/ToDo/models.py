from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)