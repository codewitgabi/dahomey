from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "content"]
    list_filter = ["date_created"]
    search_fields = ["title", "content"]
    list_per_page = 10
    ordering = ["-date_created", "last_updated"]


admin.site.register(Todo, TodoAdmin)

