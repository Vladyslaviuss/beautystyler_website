from django.contrib import admin

from . import models


@admin.register(models.ActionStatistic)
class ActionStatisticAdmin(admin.ModelAdmin):
    list_display = ("session_key", "path", "count_of_visits", "time_of_visit")
    date_hierarchy = "time_of_visit"
    list_filter = ("time_of_visit",)
    list_editable = ("count_of_visits",)
    list_per_page = 50

