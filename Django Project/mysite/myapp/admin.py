from django.contrib import admin
from .models import UserProfile
from .models import ContactInformation

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)

class ContactInformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactInformation, ContactInformationAdmin)