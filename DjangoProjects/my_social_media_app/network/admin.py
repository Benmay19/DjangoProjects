from django.contrib import admin
from .models import Post, User, Profile
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "timestamp")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "username")

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)