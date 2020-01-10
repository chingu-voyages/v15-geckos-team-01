from django.shortcuts import render
#from django import forms
from django.contrib.auth.forms import UserCreationForm
#from .custom_form import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect


class SignUp(generic.CreateView):
    #form_class = CustomUserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




def load_home(request):
    name1="Sophia"
    name2="Jordon"
    name3=". Dj ."
    name4="Nellie"
    return render(request, 'GeckoOneHome/home.html', {'chingu1':name1, 'chingu2':name2, 'chingu3':name3, 'chingu4':name4})

