from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', '情绪', '所得')
    search_fields = ('情绪', '所得', '更好', '生理', '想做')

