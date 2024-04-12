from django.contrib import admin
from .models import Profile,User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'username')
    search_fields = ('full_name', 'email', 'username')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'user')
    search_fields = ('full_name', 'gender', 'user')



admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

