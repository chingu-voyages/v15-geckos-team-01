from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.load_home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('success', views.load_loggedIn, name='success'),
]