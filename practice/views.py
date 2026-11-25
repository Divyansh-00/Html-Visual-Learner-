import json
import re
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Exercise, SavedProject


def exercise_list(request):
    category = request.GET.get('category', '')
    difficulty = request.GET.get('difficulty', '')
    exercises = Exercise.objects.all()
    if category:
        exercises = exercises.filter(category=category)
    if difficulty:
        exercises = exercises.filter(difficulty=difficulty)
    context = {
        'exercises': exercises,
        'category_choices': Exercise.CATEGORY_CHOICES,
        'active_page': 'practice',
    }
    return render(request, 'practice/exercise_list.html', context)


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    context = {
        'exercise': exercise,
        'active_page': 'practice',
        'expected_json': json.dumps(exercise.expected_properties),
    }
    return render(request, 'practice/exercise_detail.html', context)


@csrf_exempt
@require_POST
def check_answer(request, pk):
    """
    Compare submitted CSS against expected_properties.
    Uses flexible regex and string normalization to match CSS property values.
    """
    exercise = get_object_or_404(Exercise, pk=pk)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    submitted_css = data.get('css', '')
    expected = exercise.expected_properties  # dict

    def normalize_val(val_str):
        if not val_str:
            return ''
        v = str(val_str).strip().lower()
        v = v.rstrip(';')
        # collapse whitespace
        v = re.sub(r'\s+', ' ', v)
        # remove spaces around parentheses, commas
        v = re.sub(r'\s*([(),])\s*', r'\1', v)
        # normalize rgba alpha e.g. 0.1 to .1 or vice versa if needed
        v = v.replace('0.', '.')
        return v

    results = {}
    all_correct = True

    for prop, expected_val in expected.items():
        pattern = rf'{re.escape(prop)}\s*:\s*([^;}}]+)'
        match = re.search(pattern, submitted_css, re.IGNORECASE)
        if match:
            found_val = match.group(1).strip()
            norm_found = normalize_val(found_val)
            norm_exp = normalize_val(expected_val)
            correct = norm_found == norm_exp
        else:
            correct = False
            found_val = None
        results[prop] = {'correct': correct, 'found': found_val, 'expected': expected_val}
        if not correct:
            all_correct = False

    return JsonResponse({'all_correct': all_correct, 'results': results})


def playground(request):
    return render(request, 'practice/playground.html', {'active_page': 'playground'})


@login_required
def save_project(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        project_id = data.get('project_id')
        if project_id:
            try:
                project = SavedProject.objects.get(pk=project_id, user=request.user)
            except SavedProject.DoesNotExist:
                return JsonResponse({'error': 'Project not found'}, status=404)
            project.project_name = data.get('project_name', project.project_name)
            project.html_code = data.get('html_code', project.html_code)
            project.css_code = data.get('css_code', project.css_code)
            project.save()
        else:
            project = SavedProject.objects.create(
                user=request.user,
                project_name=data.get('project_name', 'Untitled Project'),
                html_code=data.get('html_code', ''),
                css_code=data.get('css_code', ''),
            )
        return JsonResponse({'success': True, 'project_id': project.pk, 'project_name': project.project_name})
    return JsonResponse({'error': 'Invalid method'}, status=405)


@login_required
def my_projects(request):
    projects = SavedProject.objects.filter(user=request.user)
    context = {
        'projects': projects,
        'active_page': 'playground',
    }
    return render(request, 'practice/my_projects.html', context)


@login_required
def delete_project(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(SavedProject, pk=pk, user=request.user)
        project.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid method'}, status=405)
