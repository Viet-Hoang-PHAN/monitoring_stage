from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from administration.models import Profile

#Add user model form
class ProfileInLine(admin.StackedInline):
	model = Profile
	can_delete = False

#User admin need ProfileInLine too 
class UserAdmin(BaseUserAdmin):
	inlines= [ProfileInLine]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)