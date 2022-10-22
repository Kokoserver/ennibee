from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "firstname",
        "lastname",
        "date_joined",
        "last_login",
        "is_active",
    )
    list_display_links = ("email", "firstname", "lastname")
    list_per_page = 10
    readonly_fields = ("date_joined", "last_login")
    list_filter = ("email", "firstname", "lastname", "is_active")
    filter_horizontal = ()
    ordering = ("-date_joined",)
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
