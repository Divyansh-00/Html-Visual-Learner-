from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:pk>/complete/', views.mark_complete, name='mark_complete'),
    path('progress/', views.my_progress, name='my_progress'),
]
