from django.contrib import admin
from .models import Login


# Register your models here.

class LoginFormAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'secondname', 'email', 'mobile', 'gender', 'date_of_birth', 'qualification',
                    'password', 'rpassword', 'district']

admin.site.register(Login, LoginFormAdmin)