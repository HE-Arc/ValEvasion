from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import MailForm


# Create your views here.

def mail_new(request):
    form = MailForm(request.POST)
    if form.is_valid():
        sender = request.user.email
        subject = form.cleaned_data['subject']
        content = form.cleaned_data['content']
        send_mail(subject, content, sender, ['laurent.gander7@gmail.com'], fail_silently=False)
        return redirect('mail-new')
    return render(request, 'mail/mail_form.html', {'form': form})
