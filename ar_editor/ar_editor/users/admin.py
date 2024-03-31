from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'email_verify', 'first_name', 'last_name', 'free_models_count', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('email_verify', 'free_models_count')}),
    # Добавление полей к полям для редактирования
    )
