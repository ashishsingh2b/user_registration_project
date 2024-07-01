from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def register_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return render(request, 'register.html', {'form': form, 'user_profile': user_profile})
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})

# def registration_success(request):
#     return render(request, 'registration_success.html')
