from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    CATEGORY_CHOICES = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('flexbox', 'Flexbox'),
        ('grid', 'CSS Grid'),
        ('layout', 'Layout'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='html')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    starter_html = models.TextField(blank=True, default='')
    starter_css = models.TextField(blank=True, default='')
    # JSON field: {"property": "value", ...}
    expected_properties = models.JSONField(default=dict, help_text='CSS property:value pairs to check')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.title


class SavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_projects')
    project_name = models.CharField(max_length=200)
    html_code = models.TextField(blank=True, default='')
    css_code = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.user.username} — {self.project_name}'
