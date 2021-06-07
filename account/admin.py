from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdminConfig(UserAdmin):
    search_fields = ('email', 'full_name', 'username')
    ordering = ('-created_on',)
    list_display = ('email', 'full_name', 'username', 'is_active', 'is_staff','created_on','updated_on')
    fieldsets = (
        (None, {'fields':('email', 'username','full_name')}),
        ('Permissions', {'fields':('is_staff', 'groups')}),
        ('Status', {'fields':('is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide', ),
            'fields':('email', 'full_name', 'username', 'is_active', 'is_staff', 'password1', 'password2', 'groups')
            }),
    )

admin.site.register(Account, AccountAdminConfig)