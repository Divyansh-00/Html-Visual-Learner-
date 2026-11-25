from django.contrib import admin
from .models import Lesson, Topic, StudentProgress


class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'order', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'description')
    list_editable = ('order', 'difficulty')
    ordering = ('category', 'order')
    inlines = [TopicInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')
    list_filter = ('lesson__category',)
    search_fields = ('title', 'description')


@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'last_accessed')
    list_filter = ('completed', 'lesson__category')
    search_fields = ('user__username', 'lesson__title')
