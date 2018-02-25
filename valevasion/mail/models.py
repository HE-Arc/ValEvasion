from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Mail(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def save(request):
        form = Mail(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            receiver = form.cleaned_data['receiver']
            sender = request.user.email
            send_mail(subject, message, 'laurent.gander@he-arc.ch', 'laurent.gander7@gmail.com')
