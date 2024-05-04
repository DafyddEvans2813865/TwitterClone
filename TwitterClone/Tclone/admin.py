from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Define the inline profile admin
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]

#remove default groups and user 
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)


