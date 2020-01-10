from django.shortcuts import render

# Create your views here.


def load_home(request):
    name1="Sophia"
    name2="Jordon"
    name3=". Dj ."
    name4="Nellie"
    return render(request, 'GeckoOneHome/home.html', {'chingu1':name1, 'chingu2':name2, 'chingu3':name3, 'chingu4':name4})


def load_loggedIn(request):
    return render(request, 'loggedIn/loggedIn.html')