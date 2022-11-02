from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm, UserUpdateForm
from django.contrib import messages
from .models import Profile
