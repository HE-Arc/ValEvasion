from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.shortcuts import redirect

@login_required
def index(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_home')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'users/account_home.html', {'form': form})

@login_required
def travels(request):
    return render(request, 'users/account_travels.html')


@login_required
def settings(request):
    return render(request, 'users/account_settings.html')
