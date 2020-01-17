from django.shortcuts import render

#from django.urls import reverse_lazy
#from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from GeckoOneHome.forms import SignUpForm



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




def load_home(request):

    return render(request, 'GeckoOneHome/index.html')

