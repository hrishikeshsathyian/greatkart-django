from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','username','password','last_name','last_login','is_active','date_joined')
    filter_horizontal = ()
    list_display_links = ('first_name',)
    list_filter = ()
    readonly_fields=('date_joined','last_login')
    #makes password read-only
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
