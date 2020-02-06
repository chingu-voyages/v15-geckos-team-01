from django.urls import path, include
#from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.load_home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
    path('faq', views.load_faq, name='faq'),
    path('contact', views.load_contact, name='contact'),
    path('', include('metrics.urls'), name='metrics'),
]

#path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name='change-password'),