from django.db import models

# Create your models here.

class Mail(models.Model):
    receiver = models.EmailField()
    sender = models.EmailField()
    subject = models.TextField()
    content = models.TextField()
