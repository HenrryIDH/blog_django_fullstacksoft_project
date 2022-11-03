from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email == "":
            raise forms.ValidationError('Enail is required')

        if User.objects.filter(email=email).exist():
            raise forms.ValidationError(
                'Email should be unique. That Email is registered!')

        return email

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bios', 'image')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


    def clean_email(self):
        email = self.email.get('email')
    
        if email == "":
            raise forms.ValidationError("Email is required")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Emails should be unique. That email is registered!")

        return email

class PasswordResetEmailCheck(PasswordResetForm):
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email == "":
            raise forms.ValidationError("Email is required")

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered!")

        return email

