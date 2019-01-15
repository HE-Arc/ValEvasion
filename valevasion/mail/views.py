from django.shortcuts import render, redirect
from django.core.mail import send_mail
import logging

from .forms import MailForm

logger = logging.getLogger(__name__)

# Create your views here.

def mail_new(request):
    form = MailForm(request.POST)
    if form.is_valid():
        receiver = form.cleaned_data['receiver'].email
        sender = request.user.email
        subject = form.cleaned_data['subject']
        content = form.cleaned_data['content']
        send_mail(subject, content, sender, [receiver,sender], fail_silently=False)
        return redirect('mail-new')
    return render(request, 'mail/mail_form.html', {'form': form})
