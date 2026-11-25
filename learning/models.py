from django.db import models
from django.contrib.auth.models import User


DIFFICULTY_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]

CATEGORY_CHOICES = [
    ('html_fundamentals', 'HTML Fundamentals'),
    ('html_elements', 'HTML Elements'),
    ('css_box_model', 'CSS Box Model'),
    ('flexbox', 'Flexbox'),
    ('css_grid', 'CSS Grid'),
    ('css_positioning', 'CSS Positioning'),
    ('css_properties', 'CSS Properties'),
]


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    content = models.TextField(help_text='HTML content of the lesson body')
    code_example = models.TextField(blank=True, help_text='Example HTML/CSS code to display')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.title

    def get_difficulty_badge_class(self):
        mapping = {
            'beginner': 'badge-beginner',
            'intermediate': 'badge-intermediate',
            'advanced': 'badge-advanced',
        }
        return mapping.get(self.difficulty, 'badge-beginner')


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f'{self.lesson.title} → {self.title}'


class StudentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    completed = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        status = 'Completed' if self.completed else 'In Progress'
        return f'{self.user.username} — {self.lesson.title} ({status})'
