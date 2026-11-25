from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('playground/', views.playground, name='playground'),
    path('exercises/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercises/<int:pk>/check/', views.check_answer, name='check_answer'),
    path('projects/', views.my_projects, name='my_projects'),
    path('projects/save/', views.save_project, name='save_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]
