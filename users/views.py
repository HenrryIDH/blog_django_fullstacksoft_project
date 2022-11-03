from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm, UserUpdateForm
from django.contrib import messages
from .models import Profile

# from .signals import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegistrationForm(request.POST or None)
    # if request.method == 'POST':

    if request.user.is_authenticated:
        messages.warning(request, "You have already an account!")
        return redirect('home')

    if form.is_valid():
        form.save()
        # user = form.save()
        # Profile.objects.create(user=user)
        messages.success(request, "User created successfully")
        return redirect('home')

    context = {
        "form" : form
    }

    return render(request, 'users/register.html', context)

def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileForm(request.POST or None, instance=request.user.profile, files=request.FILES)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, "Updated Profile!")
        return redirect(request.path)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "users/profile.html", context)
