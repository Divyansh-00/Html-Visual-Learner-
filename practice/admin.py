from django.contrib import admin
from .models import Exercise, SavedProject


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'order', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'description')
    list_editable = ('order', 'difficulty')
    ordering = ('category', 'order')


@admin.register(SavedProject)
class SavedProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'user', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('project_name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
