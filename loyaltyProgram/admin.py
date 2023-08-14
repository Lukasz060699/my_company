from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# dla moderatorów
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user"]


admin.site.register(UserProfile, UserProfileAdmin)
