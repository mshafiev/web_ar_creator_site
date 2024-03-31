# admin.py
from django.contrib import admin
from .models import ModelStats


@admin.register(ModelStats)
class ModelDisplayStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_name', 'description','remaining_displays', 'displays_today', 'displays_this_week',
                    'displays_all_time',)
    search_fields = ('user__username', 'project_name')


