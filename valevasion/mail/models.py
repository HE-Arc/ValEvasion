from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mail(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser': True}, related_name='admin')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subject = models.CharField(max_length=255)
    content = models.TextField()
