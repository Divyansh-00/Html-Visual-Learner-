from django.urls import path
from . import views

app_name = 'visualizer'

urlpatterns = [
    path('box-model/', views.box_model, name='box_model'),
    path('flexbox/', views.flexbox, name='flexbox'),
    path('css-grid/', views.css_grid, name='css_grid'),
    path('positioning/', views.positioning, name='positioning'),
    path('css-properties/', views.css_properties, name='css_properties'),
    path('elements/', views.elements, name='elements'),
]
