from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Lesson, StudentProgress, CATEGORY_CHOICES


def dashboard(request):
    lessons = Lesson.objects.all()
    total_lessons = lessons.count()

    completed_count = 0
    recent_progress = []
    if request.user.is_authenticated:
        completed_count = StudentProgress.objects.filter(
            user=request.user, completed=True
        ).count()
        recent_progress = StudentProgress.objects.filter(
            user=request.user
        ).select_related('lesson').order_by('-last_accessed')[:5]

    progress_pct = int((completed_count / total_lessons) * 100) if total_lessons > 0 else 0

    # Group lessons by category for recommended topics
    categories = {}
    for lesson in lessons[:12]:
        cat = lesson.get_category_display()
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(lesson)

    context = {
        'total_lessons': total_lessons,
        'completed_count': completed_count,
        'progress_pct': progress_pct,
        'recent_progress': recent_progress,
        'categories': categories,
        'active_page': 'dashboard',
    }
    return render(request, 'dashboard.html', context)


def lesson_list(request):
    category = request.GET.get('category', '')
    difficulty = request.GET.get('difficulty', '')

    lessons = Lesson.objects.all()
    if category:
        lessons = lessons.filter(category=category)
    if difficulty:
        lessons = lessons.filter(difficulty=difficulty)

    completed_ids = set()
    if request.user.is_authenticated:
        completed_ids = set(
            StudentProgress.objects.filter(
                user=request.user, completed=True
            ).values_list('lesson_id', flat=True)
        )

    context = {
        'lessons': lessons,
        'category_choices': CATEGORY_CHOICES,
        'selected_category': category,
        'selected_difficulty': difficulty,
        'completed_ids': completed_ids,
        'active_page': 'lessons',
    }
    return render(request, 'learning/lesson_list.html', context)


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    topics = lesson.topics.all()

    # Track access
    if request.user.is_authenticated:
        progress, _ = StudentProgress.objects.get_or_create(
            user=request.user, lesson=lesson
        )
        progress.last_accessed = timezone.now()
        progress.save(update_fields=['last_accessed'])

    # Related lessons in same category
    related = Lesson.objects.filter(category=lesson.category).exclude(pk=pk)[:4]

    context = {
        'lesson': lesson,
        'topics': topics,
        'related_lessons': related,
        'active_page': lesson.category,
    }
    return render(request, 'learning/lesson_detail.html', context)


@login_required
def mark_complete(request, pk):
    if request.method == 'POST':
        lesson = get_object_or_404(Lesson, pk=pk)
        progress, _ = StudentProgress.objects.get_or_create(
            user=request.user, lesson=lesson
        )
        progress.completed = not progress.completed
        progress.save()
        return JsonResponse({'completed': progress.completed})
    return JsonResponse({'error': 'Invalid method'}, status=405)


@login_required
def my_progress(request):
    all_lessons = Lesson.objects.all()
    progress_records = {
        p.lesson_id: p
        for p in StudentProgress.objects.filter(user=request.user).select_related('lesson')
    }
    total = all_lessons.count()
    completed = sum(1 for p in progress_records.values() if p.completed)
    pct = int((completed / total) * 100) if total > 0 else 0

    context = {
        'lessons': all_lessons,
        'progress_records': progress_records,
        'total': total,
        'completed': completed,
        'pct': pct,
        'active_page': 'progress',
    }
    return render(request, 'learning/progress.html', context)
