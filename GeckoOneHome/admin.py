from django.contrib import admin

from GeckoOneHome.models import MyUser

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(MyUser, UserProfileAdmin)


