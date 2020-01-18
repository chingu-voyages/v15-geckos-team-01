from django.shortcuts import render

#from django.urls import reverse_lazy
#from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from GeckoOneHome.forms import SignUpForm

from django.contrib.auth import get_user_model
User = get_user_model()




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)



            login(request, user)
            return redirect('metrics')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




def load_home(request):

    return render(request, 'GeckoOneHome/index.html')

